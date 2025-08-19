#!/usr/bin/env bash
set -euo pipefail

mapfile="${1:-mapping.csv}"
mode="${2:-DRY}"   # DRY or APPLY

[ -f "$mapfile" ] || { echo "Provide mapping.csv"; exit 1; }
echo "=== Periodize ($mode): $mapfile ==="

# Helper: text files only (ignore binaries)
text_files() { grep -RIl -- .; }

while IFS=, read -r old rawnew; do
  [ -n "${old:-}" ] || continue
  [ -n "${rawnew:-}" ] || continue

  # normalize slashes & trim quotes/spaces
  old="${old//\\//}"; rawnew="${rawnew//\\//}"
  new="${rawnew%\"}"; new="${new#\"}"; new="${new%% }"; new="${new## }"
  old="${old%\"}"; old="${old#\"}"; old="${old%% }"; old="${old## }"

  if [ ! -f "$old" ]; then
    echo "SKIP (missing): $old"
    continue
  fi

  echo
  echo "-----"
  echo "RENAME:"
  echo "  $old"
  echo "  → $new"

  if [ "$mode" = "APPLY" ]; then
    # ensure parent
    mkdir -p "$(dirname "$new")"
    git mv "$old" "$new"
  fi

  echo "UPDATE REFS:"
  # Find and replace literal path occurrences across repo text files
  # Use # delimiter to avoid path slashes clashing
  hits=$(grep -RIl -- "$old" . | wc -l | tr -d ' ')
  echo "  $hits file(s) reference $old"
  if [ "$mode" = "APPLY" ] && [ "$hits" -gt 0 ]; then
    grep -RIl -- "$old" . | while read -r f; do
      sed -i "s#${old}#${new}#g" "$f"
    done
  fi

done < "$mapfile"

echo
echo "Done ($mode). To apply, run: tools/periodize_many.sh mapping.csv APPLY"
