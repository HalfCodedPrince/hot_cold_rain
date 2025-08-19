#!/usr/bin/env python3
# tools/generate_indices_and_digest.py
import re, sys, argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ROOT = Path(".").resolve()

def read_text(p): return p.read_text(encoding="utf-8", errors="replace")

def find_anthology(explicit: str|None):
    if explicit:
        p = Path(explicit)
        if not p.is_absolute():
            p = ROOT / p
        if p.exists():
            return p.resolve()
        print(f"[warn] --anth '{explicit}' not found", file=sys.stderr)

    # auto-search common locations (root, tools, upload_ready)
    candidates = [
        ROOT / "front_matter_anthology.md",
        ROOT / "tools" / "front_matter_anthology.md",
        ROOT / "tools" / "upload_ready" / "front_matter_anthology.md",
    ]
    for p in candidates:
        if p.exists():
            return p.resolve()
    return None

# ---- parse anthology blocks ----
BLOCK_RE = re.compile(r'(?m)^##\s+(.+?)\s*$')

def parse_blocks(text: str):
    out = []
    parts = BLOCK_RE.split(text)
    for i in range(1, len(parts), 2):
        path = parts[i].strip()
        body = parts[i+1]
        fields = {}
        for line in body.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r'^([A-Za-z0-9_]+):\s*(.*)$', line)
            if not m:
                continue
            k, v = m.group(1), m.group(2).strip()
            fields[k] = v
        out.append((path, fields))
    return out

def parse_list(v: str):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1]
        return [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
    return [v] if v else []

def microcard(path, fields):
    rid = fields.get('id','')
    name = fields.get('name', rid)
    tags = fields.get('tags','')
    if tags:
        gloss = ", ".join(parse_list(tags)[:3])
    else:
        m = re.search(r'\(([^)]+)\)', name)
        gloss = m.group(1) if m else ""
    return rid, name, gloss, path

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"[ok] wrote {path}")

def md_entities_index(cat, items, today):
    title_id = {
        'people':'INDEX:PEOPLE',
        'factions':'INDEX:FACTIONS',
        'places':'INDEX:PLACES',
        'regions':'INDEX:REGIONS'
    }[cat]
    title_name = {
        'people':'People — One-Liners & Links',
        'factions':'Factions — One-Liners & Links',
        'places':'Places — One-Liners & Links',
        'regions':'Regions — One-Liners & Links'
    }[cat]
    lines = ["---", f"id: {title_id}", f"name: {title_name}", "status: Stable", f"updated: {today}", "---", ""]
    for rid,name,gloss,path in sorted(items, key=lambda x: x[3].lower()):
        gl = f" — {gloss}" if gloss else ""
        lines.append(f"- [{rid}] **{name}**{gl}  \n  → {path}")
    return "\n".join(lines) + "\n"

def md_systems_digest(systems, today):
    groups = defaultdict(list)
    for rid,name,gloss,path in systems:
        parts = path.split('/')
        family = parts[2] if len(parts) > 2 else "general"
        if family.endswith(".md"):
            family = "general"
        groups[family].append((rid,name,gloss,path))

    lines = ["---","id: PACK:SYSTEMS-DIGEST","name: Systems Digest — Claims & Links","status: Stable",f"updated: {today}","---",""]
    lines += ["This digest lists each system page with its ID and canonical path. Keep claims in the source pages; this file is compact routing.", ""]
    for family in sorted(groups.keys()):
        lines += [f"## {family.title()}", ""]
        for rid,name,gloss,path in sorted(groups[family], key=lambda x: x[3].lower()):
            lines += [f"### {name}", f"`{rid}` — {path}"]
            if gloss: lines += [f"- Tags: {gloss}"]
            lines += [""]
    return "\n".join(lines) + "\n"

def main():
    ap = argparse.ArgumentParser(description="Generate entity indices and systems digest from front_matter_anthology.md")
    ap.add_argument("--anth", default="", help="Path to front_matter_anthology.md (optional)")
    args = ap.parse_args()

    anth = find_anthology(args.anth)
    if not anth:
        print("[error] front_matter_anthology.md not found in ./, tools/, or tools/upload_ready/; use --anth PATH", file=sys.stderr)
        sys.exit(2)

    print(f"[info] using anthology: {anth}")
    text = read_text(anth)
    blocks = parse_blocks(text)
    today = datetime.utcnow().strftime("%Y-%m-%d")

    by_cat = defaultdict(list)
    systems = []
    for path, fields in blocks:
        if path.startswith("canon/entities/"):
            parts = path.split('/')
            if len(parts)>=3 and parts[2] in ('people','factions','places','regions'):
                by_cat[parts[2]].append(microcard(path, fields))
        elif path.startswith("canon/systems/"):
            systems.append(microcard(path, fields))

    wrote = 0
    if by_cat['people']:
        wrote += 1
        write(ROOT / "canon/entities/people/index.md",  md_entities_index('people',  by_cat['people'],  today))
    if by_cat['factions']:
        wrote += 1
        write(ROOT / "canon/entities/factions/index.md",md_entities_index('factions',by_cat['factions'],today))
    if by_cat['places']:
        wrote += 1
        write(ROOT / "canon/entities/places/index.md",  md_entities_index('places',  by_cat['places'],  today))
    if by_cat['regions']:
        wrote += 1
        write(ROOT / "canon/entities/regions/index.md", md_entities_index('regions', by_cat['regions'], today))

    if systems:
        wrote += 1
        write(ROOT / "canon/systems/systems_digest.md", md_systems_digest(systems, today))

    print(f"[done] generated {wrote} file(s).")

if __name__ == "__main__":
    main()
