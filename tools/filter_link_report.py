#!/usr/bin/env python3
# tools/filter_link_report.py
import argparse, csv
from pathlib import Path
from collections import Counter, defaultdict

def main():
    ap = argparse.ArgumentParser(description="Filter link_report.tsv to errors/warnings and make a summary")
    ap.add_argument("--in", dest="inp", default="tools/link_report.tsv", help="input TSV")
    ap.add_argument("--out", dest="out", default="tools/link_errors.tsv", help="filtered TSV output")
    ap.add_argument("--md", dest="md", default="tools/link_summary.md", help="optional Markdown summary")
    ap.add_argument("--status-prefix", default="ERR-", help="prefix to keep (e.g., 'ERR-' or 'WARN-'; use 'ERR|WARN' to keep both)")
    args = ap.parse_args()

    src = Path(args.inp); dst = Path(args.out); mdp = Path(args.md)
    rows = []
    with src.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        hdr = r.fieldnames or []
        if "status" not in hdr:
            raise SystemExit("Input TSV missing 'status' column")
        keep = []
        sp = args.status_prefix
        for row in r:
            st = row.get("status","")
            if st.startswith(sp) or (sp=="ERR|WARN" and (st.startswith("ERR-") or st.startswith("WARN-"))):
                keep.append(row)

    # write filtered
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=hdr, delimiter="\t")
        w.writeheader()
        w.writerows(keep)

    # summary markdown
    by_status = Counter([r["status"] for r in keep])
    by_source = Counter([r["source"] for r in keep])
    by_target = Counter([r["resolved"] for r in keep])

    lines = []
    lines += ["# Link Report — Filtered Summary", ""]
    lines += [f"- Input: `{src.as_posix()}`"]
    lines += [f"- Output (filtered): `{dst.as_posix()}`"]
    lines += [f"- Kept statuses: `{args.status_prefix}`", ""]
    lines += ["## Counts by status", ""]
    for st, n in by_status.most_common():
        lines.append(f"- **{st}** — {n}")
    lines += ["", "## Top offending sources", ""]
    for s, n in by_source.most_common(20):
        lines.append(f"- {n} × `{s}`")
    lines += ["", "## Most-referenced broken targets", ""]
    for t, n in by_target.most_common(20):
        lines.append(f"- {n} × `{t}`")

    mdp.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[ok] wrote {dst} ({len(keep)} rows)")
    print(f"[ok] wrote {mdp}")

if __name__ == "__main__":
    main()
