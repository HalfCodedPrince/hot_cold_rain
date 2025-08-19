#!\usr\bin\env python3
# tools\router_lite.py

# python -u tools\router_lite.py
import csv, sys
from pathlib import Path
from collections import Counter

def sniff_delim(sample: str, default="\t"):
    try:
        return csv.Sniffer().sniff(sample, delimiters="\t,;|").delimiter
    except Exception:
        return default

def load_link_counts(tsv_path: Path):
    if not tsv_path.exists():
        print(f"[error] {tsv_path} not found", file=sys.stderr); sys.exit(2)
    text = tsv_path.read_text(encoding="utf-8", errors="replace")
    delim = sniff_delim(text[:5000])
    counts = Counter()
    for row in csv.reader(text.splitlines(), delimiter=delim):
        if not row: continue
        target = row[-1].strip()
        if target and not target.lower().startswith("http"):
            # normalize ./prefix
            while target.startswith("./"): target = target[2:]
            counts[target] += 1
    return counts

def write_router_lite(out_path: Path, counts, top: int):
    lines = [f"# Router (Top {top} by inbound refs)"]
    for target, cnt in counts.most_common(top):
        lines.append(f"- {target} — {cnt} refs")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[ok] wrote {out_path}")

if __name__ == "__main__":
    repo = Path(".").resolve()
    link_tsv = repo / "tools" / "link_targets.tsv"   # change if yours lives elsewhere
    out_md   = repo / "tools" / "router_index.md"
    TOP = 150

    counts = load_link_counts(link_tsv)
    write_router_lite(out_md, counts, TOP)
