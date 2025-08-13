#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
OUTDIR="$ROOT/tools"
mkdir -p "$OUTDIR"

echo "» Generating id_to_path.csv"
printf "id,path\n" > "$OUTDIR/id_to_path.csv"

# Iterate tracked md files; skip missing paths defensively (Windows rename quirks).
while IFS= read -r -d '' f; do
  [ -f "$f" ] || { echo "  ! skip (missing): $f" >&2; continue; }
  id="$(awk '
    BEGIN{fm=0;found=0}
    /^---[ \t]*$/ { if(fm==0){fm=1; next} else if(fm==1){exit} }
    fm==1 && !found && $0 ~ /^id:[ \t]*/ {
      sub(/^id:[ \t]*/,""); gsub(/^[ \t]+|[ \t]+$/,"")
      print; found=1
    }
  ' "$f")"
  if [ -n "${id:-}" ]; then
    printf "%s,%s\n" "$id" "$f" >> "$OUTDIR/id_to_path.csv"
  fi
done < <(git ls-files -z -- 'canon/**/*.md')

echo "» Generating front_matter_anthology.md"
: > "$OUTDIR/front_matter_anthology.md"
while IFS= read -r -d '' f; do
  [ -f "$f" ] || { echo "  ! skip (missing): $f" >&2; continue; }
  awk -v FILE="$f" '
    BEGIN{fm=0}
    /^---[ \t]*$/ {
      if(fm==0){ fm=1; print "\n## " FILE; next }
      else if(fm==1){ fm=2; exit }
    }
    fm==1 { print }
  ' "$f" >> "$OUTDIR/front_matter_anthology.md"
done < <(git ls-files -z -- 'canon/**/*.md')

echo "» Generating link_targets.tsv"
: > "$OUTDIR/link_targets.tsv"
while IFS= read -r -d '' f; do
  [ -f "$f" ] || { echo "  ! skip (missing): $f" >&2; continue; }
  awk -v FILE="$f" '
    BEGIN{inlinks=0; code=0}
    /^```/ { code = !code; next }                    # ignore code fences
    code { next }

    /^links:[ \t]*$/ { inlinks=1; next }
    inlinks && NF==0 { inlinks=0 }                   # blank line ends block
    inlinks && $0 ~ /^[^ \t-].*:[ \t]*/ { inlinks=0 }# next top-level key
    inlinks {
      line=$0
      sub(/^[ \t-]*/,"",line)
      split(line, kv, ":[ \t]*")
      val=(length(kv)>1)?kv[2]:kv[1]
      gsub(/^[ \t"'\'']+|[ \t"'\'']+$/,"",val)
      # only real md paths; skip uppercase paths (example detritus)
      if (val ~ /\/[^ ]*\.md([#?].*)?$/ && val !~ /[A-Z]/) {
        print FILE "\t" val
      }
    }
  ' "$f" >> "$OUTDIR/link_targets.tsv"
done < <(git ls-files -z -- 'canon/**/*.md')

echo "» Snapshot complete."
echo "   id_to_path.csv: $(($(wc -l < "$OUTDIR/id_to_path.csv")-1)) ids"
echo "   front_matter_anthology.md: $(grep -c '^## ' "$OUTDIR/front_matter_anthology.md") files"
echo "   link_targets.tsv: $(wc -l < "$OUTDIR/link_targets.tsv") links"
