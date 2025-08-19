#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate markdown links/anchors across the repo:
- checks relative file targets exist (GitHub-like, case-sensitive by default)
- supports repo-root style links like 'canon/...', 'tools/...', and '/canon/...'
- checks anchors (#fragment) using GitHub-ish slug rules (can downgrade to warnings)
- parses inline links, reference-style links, images, and front-matter `links:` (dict or list)
- treats ID-like values in `links:` (e.g., PERS:..., FAC:...) as non-file references (skipped)
- outputs TSV report and non-zero exit if any errors
- can (re)emit tools/link_targets.tsv with inbound counts
"""

import argparse, csv, os, re, sys, unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

# ---------- Config ----------
ROOTED_PREFIXES_DEFAULT = ["canon", "tools", "docs", "notes", "_assets", "_static"]

# ---------- FS helpers ----------

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def listdir_names(path: Path):
    try:
        return set(os.listdir(path))
    except FileNotFoundError:
        return set()

def path_exists_case_sensitive(p: Path) -> bool:
    """
    Emulate GitHub case-sensitive paths on case-insensitive FS.
    True only if every segment matches exact case on disk.
    """
    parts = p.parts
    if not parts:
        return False
    cur = Path(parts[0])
    if not cur.exists():
        return False
    for seg in parts[1:]:
        names = listdir_names(cur)
        if seg not in names:
            return False
        cur = cur / seg
    return True

# ---------- Repo-root helpers ----------

def is_repo_rooted(pstr: str, rooted_prefixes=None):
    rooted_prefixes = rooted_prefixes or ROOTED_PREFIXES_DEFAULT
    p = pstr.replace("\\", "/")
    p = p.lstrip("./")
    if p.startswith("/"):
        return True  # absolute-from-repo-root style '/canon/...'
    return any(p == pre or p.startswith(pre + "/") for pre in rooted_prefixes)

# ---------- Front matter parsing (minimal but robust) ----------

def split_front_matter(md: str):
    if not md.startswith("---"):
        return None, md
    lines = md.splitlines()
    # find closing '---' line
    for i in range(1, min(len(lines), 500)):
        if lines[i].strip() == "---":
            fm = "\n".join(lines[1:i])
            body = "\n".join(lines[i+1:])
            return fm, body
    return None, md

ID_LIKE = re.compile(r"^[A-Z]{2,6}:[A-Z0-9][A-Z0-9:\-_.]*$")  # e.g., PERS:..., FAC:..., ERA-XX,...

def parse_fm_minimal(fm: str):
    """
    Tiny YAML-ish parser for top-level keys we care about (esp. 'links').
    Defers container type until it sees children, so 'links:' can become a list or dict.
    """
    out = {}
    current_key = None
    for raw in fm.splitlines():
        line = raw.rstrip("\r\n")
        if not line or line.lstrip().startswith("#"):
            continue

        m = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            current_key = key

            # Inline list: key: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1]
                out[key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
                continue

            # Inline scalar: key: value
            if val:
                out[key] = val.strip().strip("'\"")
                continue

            # Bare key (no inline value): container unknown yet
            out[key] = None
            continue

        if current_key is None:
            continue

        # List item: "  - value"
        lm = re.match(r"^\s*-\s+(.*)$", line)
        if lm:
            if out[current_key] is None or not isinstance(out[current_key], list):
                out[current_key] = []
            out[current_key].append(lm.group(1).strip().strip("'\""))
            continue

        # Dict item: "  subkey: value"
        dm = re.match(r"^\s+([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if dm:
            k2, v2 = dm.group(1), dm.group(2).strip()
            if out[current_key] is None or not isinstance(out[current_key], dict):
                out[current_key] = {}
            out[current_key][k2] = v2.strip().strip("'\"")
            continue

    return out

# ---------- Markdown parsing ----------

MD_INLINE_LINK = re.compile(r'(!?)(\[(?:[^\]]|\\\])*\])\(([^)\s]+)(?:\s+"[^"]*")?\)')
MD_REF_DEF   = re.compile(r'^\s*\[([^\]]+)\]:\s*(\S+)(?:\s+"[^"]*")?\s*$', re.MULTILINE)
MD_REF_USE   = re.compile(r'\[([^\]]+)\]\[([^\]]+)\]')  # [text][label]
MD_AUTOLINK  = re.compile(r'<(?!mailto:)([^ >]+)>')
HEADING      = re.compile(r'^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$', re.MULTILINE)

def github_slugify(text: str, dedupe_counter: Counter):
    s = text.strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r'[^\w\s\-]', '', s)   # drop punctuation except hyphen/underscore
    s = re.sub(r'\s+', '-', s)        # spaces -> hyphens
    s = re.sub(r'-{2,}', '-', s).strip('-')
    n = dedupe_counter[s]
    dedupe_counter[s] += 1
    return s if n == 0 else f"{s}-{n}"

def collect_anchors(md_path: Path):
    try:
        text = read_text(md_path)
    except Exception:
        return set()
    _, body = split_front_matter(text)
    if body is None:
        body = text
    anchors = set()
    seen = Counter()
    for m in HEADING.finditer(body):
        heading_text = m.group(2)
        slug = github_slugify(heading_text, seen)
        anchors.add(slug)
    return anchors

def extract_links(md_path: Path):
    """
    Yield (raw_target, is_image, line_idx, kind) from the file content.
    Includes:
      - inline markdown links
      - reference-style links
      - autolinks <...> (non-http)
      - front-matter `links:` dict/list (skips ID-like values e.g., PERS:..., FAC:...)
    """
    text = read_text(md_path)
    fm_text, body = split_front_matter(text)
    if fm_text:
        fm = parse_fm_minimal(fm_text)
        if "links" in fm:
            links_val = fm["links"]
            # dict form
            if isinstance(links_val, dict):
                for v in links_val.values():
                    if isinstance(v, str) and v:
                        if ID_LIKE.match(v):  # skip IDs
                            continue
                        yield v, False, 1, "fm:links"
                    elif isinstance(v, list):
                        for vv in v:
                            if isinstance(vv, str) and vv and not ID_LIKE.match(vv):
                                yield vv, False, 1, "fm:links"
            # list form
            elif isinstance(links_val, list):
                for v in links_val:
                    if isinstance(v, str) and v and not ID_LIKE.match(v):
                        yield v, False, 1, "fm:links"

    # inline: [text](target)
    for m in MD_INLINE_LINK.finditer(text):
        bang, _, target = m.group(1), m.group(2), m.group(3)
        is_image = (bang == "!")
        line_idx = text[:m.start()].count("\n") + 1
        yield target, is_image, line_idx, "inline"

    # reference defs and uses
    ref_defs = {m.group(1): m.group(2) for m in MD_REF_DEF.finditer(text)}
    for m in MD_REF_USE.finditer(text):
        lbl = m.group(2)
        if lbl in ref_defs:
            target = ref_defs[lbl]
            line_idx = text[:m.start()].count("\n") + 1
            yield target, False, line_idx, "ref"

    # autolinks <path>
    for m in MD_AUTOLINK.finditer(text):
        target = m.group(1).strip()
        if "://" not in target and not target.lower().startswith("mailto:"):
            line_idx = text[:m.start()].count("\n") + 1
            yield target, False, line_idx, "autolink"

# ---------- Classification ----------

def classify_target(raw: str):
    """
    Return (kind, path_str, fragment)
    kind in {"external","anchor","path"}
    """
    raw = unquote(raw)  # decode %20 etc.
    if raw.startswith("#"):
        return "anchor", "", raw[1:]
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.\-]*://', raw) or raw.startswith("mailto:"):
        return "external", raw, ""
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    if "#" in raw:
        p, frag = raw.split("#", 1)
    else:
        p, frag = raw, ""
    return "path", p, frag

# ---------- Core validation ----------

def validate(repo_root: Path, out_tsv: Path, emit_link_targets,
             include_images=True, case_sensitive=True,
             rooted_prefixes=None, warn_anchors=False):
    rows = []
    problems = 0
    anchors_cache = {}  # Path -> set(slugs)

    md_files = sorted(repo_root.rglob("*.md"))
    for src in md_files:
        for raw_target, is_image, line_idx, kind in extract_links(src):
            if is_image and not include_images:
                continue

            kind2, pstr, frag = classify_target(raw_target)
            status = "OK"
            note = ""
            resolved = ""

            if kind2 == "external":
                status = "OK-EXTERNAL"
                resolved = pstr

            elif kind2 == "anchor":
                # anchor within same file
                anchors = anchors_cache.get(src)
                if anchors is None:
                    anchors = collect_anchors(src)
                    anchors_cache[src] = anchors
                if frag not in anchors:
                    status = "WARN-MISSING-ANCHOR" if warn_anchors else "ERR-MISSING-ANCHOR"
                    note = "anchor not found in source file"
                resolved = f"{src.relative_to(repo_root)}#{frag}".replace("\\", "/")

            else:
                # path target
                pnorm = pstr.replace("\\", "/").lstrip("./")
                # treat '/...' as repo-root
                if pnorm.startswith("/"):
                    pnorm = pnorm[1:]

                base = repo_root if is_repo_rooted(pnorm, rooted_prefixes) else src.parent
                tgt = (base / pnorm).resolve()

                try:
                    rel_to_repo = tgt.relative_to(repo_root.resolve())
                except Exception:
                    rel_to_repo = tgt
                resolved = str(rel_to_repo).replace("\\", "/")

                # existence & case
                if not tgt.exists():
                    # try directory index.md / README.md if it's a directory path
                    alt_index = tgt / "index.md"
                    alt_readme = tgt / "README.md"
                    if alt_index.exists():
                        tgt = alt_index
                        resolved = str(alt_index.relative_to(repo_root)).replace("\\", "/")
                    elif alt_readme.exists():
                        tgt = alt_readme
                        resolved = str(alt_readme.relative_to(repo_root)).replace("\\", "/")
                    else:
                        status = "ERR-MISSING-FILE"
                elif case_sensitive and not path_exists_case_sensitive(tgt):
                    status = "ERR-CASE-MISMATCH"
                    note = "different letter casing than on disk"

                # anchor check (only if file exists and is markdown)
                if status.startswith("OK") and frag:
                    if tgt.suffix.lower() == ".md":
                        anchors = anchors_cache.get(tgt)
                        if anchors is None:
                            anchors = collect_anchors(tgt)
                            anchors_cache[tgt] = anchors
                        if frag not in anchors:
                            status = "WARN-MISSING-ANCHOR" if warn_anchors else "ERR-MISSING-ANCHOR"
                    else:
                        note = (note + "; " if note else "") + "fragment on non-markdown target"

            if status.startswith("ERR"):
                problems += 1
            rows.append([
                str(src.relative_to(repo_root)).replace("\\", "/"),
                line_idx, kind, raw_target, resolved, status, note
            ])

    # write report
    out_tsv.parent.mkdir(parents=True, exist_ok=True)
    with out_tsv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["source", "line", "kind", "raw_target", "resolved", "status", "note"])
        w.writerows(rows)

    # optionally emit link_targets.tsv
    if emit_link_targets:
        counts = Counter()
        for r in rows:
            resolved = r[4]
            if resolved and not r[5].startswith("ERR"):  # count only non-error targets
                counts[resolved] += 1
        emit_link_targets.parent.mkdir(parents=True, exist_ok=True)
        with emit_link_targets.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t")
            w.writerow(["target_path", "inbound_refs"])
            for tgt, cnt in counts.most_common():
                w.writerow([tgt, cnt])

    return problems, len(rows)

# ---------- CLI ----------

def main():
    ap = argparse.ArgumentParser(description="Validate Markdown links/anchors across a repo")
    ap.add_argument("--root", default=".", help="Repo root (default: current dir)")
    ap.add_argument("--out", default="tools/link_report.tsv", help="Where to write the TSV report")
    ap.add_argument("--emit-link-targets", default="", help="Optionally (re)write tools/link_targets.tsv")
    ap.add_argument("--no-images", action="store_true", help="Skip validating image file links")
    ap.add_argument("--no-case", action="store_true", help="Disable case-sensitive checks (Windows-friendly)")
    ap.add_argument("--rooted-prefixes", default=",".join(ROOTED_PREFIXES_DEFAULT),
                    help="Comma-separated list treated as repo-root-anchored (default: canon,tools,docs,notes,...)")
    ap.add_argument("--warn-anchors", action="store_true",
                    help="Downgrade missing anchors to warnings instead of errors")

    args = ap.parse_args()
    repo_root = Path(args.root).resolve()
    out_tsv = Path(args.out)
    emit_lt = Path(args.emit_link_targets) if args.emit_link_targets else None
    rooted = [s for s in (args.rooted_prefixes or "").split(",") if s]

    problems, total = validate(
        repo_root,
        out_tsv,
        emit_lt,
        include_images=not args.no_images,
        case_sensitive=not args.no_case,
        rooted_prefixes=rooted,
        warn_anchors=args.warn_anchors,
    )

    print(f"[done] scanned: {repo_root}")
    print(f"[done] links found: {total} — problems: {problems}")
    print(f"[done] report: {out_tsv}")
    if emit_lt:
        print(f"[done] link_targets.tsv: {emit_lt}")

    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
