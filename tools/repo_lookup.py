#!/usr/bin/env python3
# reqs: pip install pyyaml
import argparse, json, os, re, sys, time
from pathlib import Path, PurePosixPath
try:
    import yaml  # PyYAML
except Exception as e:
    print("ERROR: PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise

FRONT_DELIM = re.compile(r"^---\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")

def to_posix(p: Path) -> str:
    return str(PurePosixPath(p.as_posix()))

def load_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def parse_front_matter(text: str):
    lines = text.splitlines()
    if not lines or not FRONT_DELIM.match(lines[0]):
        return {}
    # find closing ---
    for i in range(1, min(len(lines), 1000)):  # safety cap
        if FRONT_DELIM.match(lines[i]):
            yml = "\n".join(lines[1:i])
            try:
                data = yaml.safe_load(yml) or {}
                return data if isinstance(data, dict) else {}
            except Exception:
                return {}
    return {}

def slugify(s: str) -> str:
    s = s.strip().lower()
    # drop inline code backticks
    s = s.replace("`", "")
    # remove apostrophes and punctuation except spaces/hyphens/underscores
    s = re.sub(r"[^\w\s\-]", "", s, flags=re.UNICODE)
    # underscores count as hyphens in our anchors
    s = s.replace("_", "-")
    # collapse whitespace to single hyphens
    s = re.sub(r"\s+", "-", s)
    # collapse repeated hyphens
    s = re.sub(r"-{2,}", "-", s)
    return f"#{s}"

def extract_anchors(text: str):
    anchors = []
    in_code = False
    fence_re = re.compile(r"^```")
    for line in text.splitlines():
        if fence_re.match(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADING_RE.match(line)
        if m:
            title = m.group(2)
            anchors.append(slugify(title))
    return anchors

def scan_repo(root: Path):
    id_to_path = {}
    path_to_links = {}
    path_to_anchors = {}
    for p in root.rglob("*.md"):
        try:
            text = load_text(p)
        except Exception:
            continue
        data = parse_front_matter(text)
        posix_path = to_posix(p.relative_to(root))
        # anchors
        path_to_anchors[posix_path] = extract_anchors(text)
        # links
        links = data.get("links") if isinstance(data, dict) else None
        if isinstance(links, dict):
            # normalize to posix relpaths
            norm = {}
            for k, v in links.items():
                if isinstance(v, str):
                    norm[k] = str(PurePosixPath(v))
            path_to_links[posix_path] = norm
        else:
            path_to_links[posix_path] = {}
        # id
        _id = data.get("id") if isinstance(data, dict) else None
        if isinstance(_id, str) and _id:
            id_to_path[_id] = posix_path
    return {
        "generated_at": int(time.time()),
        "root": to_posix(root.resolve()),
        "id_to_path": id_to_path,
        "path_to_links": path_to_links,
        "path_to_anchors": path_to_anchors,
    }

def read_cache(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        print("ERROR: cannot read cache. Run 'build' first.", file=sys.stderr)
        sys.exit(2)

def write_cache(cache, out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

def cmd_build(args):
    root = Path(args.root).resolve()
    cache = scan_repo(root)
    write_cache(cache, Path(args.out))
    print(f"Wrote {args.out} ({len(cache['id_to_path'])} IDs, "
          f"{len(cache['path_to_links'])} files).")

def load_and_cache(args):
    cache = read_cache(Path(args.cache))
    return cache

def cmd_find_id(args):
    cache = load_and_cache(args)
    path = cache["id_to_path"].get(args.id)
    print(json.dumps(path))

def cmd_get_links(args):
    cache = load_and_cache(args)
    path = normalize_rel(args.path, cache)
    links = cache["path_to_links"].get(path, {})
    print(json.dumps(links, ensure_ascii=False, indent=2))

def cmd_search_paths(args):
    cache = load_and_cache(args)
    # emulate glob over keys
    import fnmatch
    matches = sorted([p for p in cache["path_to_links"].keys()
                      if fnmatch.fnmatch(p, args.glob)])
    print(json.dumps(matches, ensure_ascii=False, indent=2))

def cmd_anchors(args):
    cache = load_and_cache(args)
    path = normalize_rel(args.path, cache)
    anchors = cache["path_to_anchors"].get(path, [])
    print(json.dumps(anchors, ensure_ascii=False, indent=2))

def normalize_rel(path_arg: str, cache) -> str:
    # Allow absolute or relative; always return posix relative to cache["root"]
    root = Path(cache["root"])
    p = Path(path_arg)
    if p.is_absolute():
        try:
            rel = p.relative_to(root)
            return str(PurePosixPath(rel.as_posix()))
        except Exception:
            return str(PurePosixPath(p.as_posix()))
    else:
        return str(PurePosixPath(p.as_posix()))

def cmd_verify_backlink(args):
    cache = load_and_cache(args)
    # resolve ID to path
    target_path = cache["id_to_path"].get(args.id)
    if not target_path:
        print(json.dumps({"result": "INCONCLUSIVE", "reason": "ID_NOT_FOUND"}))
        sys.exit(1)
    overview = normalize_rel(args.overview, cache)
    links = cache["path_to_links"].get(overview)
    if links is None:
        print(json.dumps({"result": "INCONCLUSIVE", "reason": "OVERVIEW_NOT_INDEXED"}))
        sys.exit(1)
    found = any((str(v) == target_path) for v in links.values())
    res = {"result": "FOUND" if found else "MISSING",
           "overview": overview, "target_path": target_path}
    print(json.dumps(res, ensure_ascii=False, indent=2))
    sys.exit(0 if found else 1)

def main():
    ap = argparse.ArgumentParser(prog="repo_lookup", description="Front-matter link + anchor indexer")
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("build", help="Scan repo and write cache")
    a.add_argument("--root", default=".", help="Repo root")
    a.add_argument("--out", default=".cache/repo_lookup.json", help="Cache path")
    a.set_defaults(func=cmd_build)

    a = sub.add_parser("find-id", help="Find path by ID")
    a.add_argument("id")
    a.add_argument("--cache", default=".cache/repo_lookup.json")
    a.set_defaults(func=cmd_find_id)

    a = sub.add_parser("get-links", help="Get links mapping for a file")
    a.add_argument("path")
    a.add_argument("--cache", default=".cache/repo_lookup.json")
    a.set_defaults(func=cmd_get_links)

    a = sub.add_parser("search-paths", help="Glob search over indexed file paths")
    a.add_argument("glob")
    a.add_argument("--cache", default=".cache/repo_lookup.json")
    a.set_defaults(func=cmd_search_paths)

    a = sub.add_parser("anchors", help="List anchor slugs for headings in a file")
    a.add_argument("path")
    a.add_argument("--cache", default=".cache/repo_lookup.json")
    a.set_defaults(func=cmd_anchors)

    a = sub.add_parser("verify-backlink", help="Check if overview links back to an ID's page")
    a.add_argument("--id", required=True)
    a.add_argument("--overview", required=True, help="Path to overview page")
    a.add_argument("--cache", default=".cache/repo_lookup.json")
    a.set_defaults(func=cmd_verify_backlink)

    args = ap.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
