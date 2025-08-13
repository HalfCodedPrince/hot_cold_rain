#!/usr/bin/env bash
set -euo pipefail

TIMELINE="canon/timeline/point_timeline.csv"

echo "— VALIDATION REPORT —"

# --- Build ID → path index from YAML front matter (no grep options) ----------
declare -A ID2PATH

# Use find without NUL to avoid MSYS oddities; guard against spaces with while IFS= read -r
while IFS= read -r f; do
  # read first 120 lines; capture the first YAML block delimited by ---
  head -n 120 "$f" > /tmp/_head120.$$ || true
  # does it start with --- ?
  first=$(head -n 1 /tmp/_head120.$$ || true)
  if [ "$first" != "---" ]; then continue; fi
  # get lines 2..until next --- (or up to 80 lines)
  tail -n +2 /tmp/_head120.$$ | awk 'BEGIN{open=1} /^---$/{exit} {if(NR<=80)print}' > /tmp/_yaml.$$ || true
  # extract id:
  id=$(awk -F: '/^[[:space:]]*id[[:space:]]*:/ {sub(/^[[:space:]]*id[[:space:]]*:/,""); gsub(/^[[:space:]]+|[[:space:]]+$/,""); print; exit}' /tmp/_yaml.$$)
  if [ -n "${id:-}" ]; then ID2PATH["$id"]="$f"; fi
done < <(find canon -type f -name '*.md')

rm -f /tmp/_head120.$$ /tmp/_yaml.$$ 2>/dev/null || true

echo "Indexed IDs: ${#ID2PATH[@]}"

# --- Refs check --------------------------------------------------------------
awk -F, 'NR>1 {print NR ":" $8}' "$TIMELINE" \
| while IFS=: read -r ln refs; do
  # split on | ; strip quotes, anchors, CR/LF and surrounding spaces
  echo "$refs" | tr '|' '\n' \
  | sed -e 's/\r$//' -e 's/^"//' -e 's/"$//' -e 's/#.*$//' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' \
  | awk 'NF' \
  | while IFS= read -r p; do
      [ -f "$p" ] || echo "MISSING REF line $ln: $p"
    done
done

# --- ID check (REG/LOC/FAC/PERS in where/who) --------------------------------
# --- ID check (REG/LOC/FAC/PERS in where/who) --------------------------------
awk -F, 'NR>1 {print NR ":" $4 ":" $5}' "$TIMELINE" \
| while IFS=: read -r ln where who; do
  printf "%s\n" "$where" "$who" \
  | tr ';' '\n' \
  | sed -E \
      -e 's/^[[:space:]]+|[[:space:]]+$//g' \
      -e 's/^["“”'\''(]+//'  \
      -e 's/["“”'\'')]+$//' \
      -e 's/:$//' \
  | awk 'NF && $0 !~ /^\(/' \
  | while IFS= read -r id; do
      case "$id" in
        REG:*|LOC:*|FAC:*|PERS:* )
          [[ -n "${ID2PATH[$id]+x}" ]] || echo "MISSING ID line $ln: $id"
          ;;
        * ) : ;;
      esac
    done
done
