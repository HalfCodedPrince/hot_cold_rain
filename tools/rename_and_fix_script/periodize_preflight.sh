#!/usr/bin/env bash
set -euo pipefail

mapfile="${1:-mapping.csv}"
[ -f "$mapfile" ] || { echo "Provide mapping.csv"; exit 1; }

echo "=== Preflight: $mapfile ==="
errors=0

# Warn on backslashes in mapping (Windows paths)
if grep -n '\\' "$mapfile"; then
  echo "WARNING: Backslashes found above. Convert to forward slashes in mapping.csv."
fi

while IFS=, read -r old rawnew; do
  [ -n "${old:-}" ] || continue
  [ -n "${rawnew:-}" ] || continue
  # normalize slashes, trim quotes/spaces
  old="${old//\\//}"; rawnew="${rawnew//\\//}"
  new="${rawnew%\"}"; new="${new#\"}"; new="${new%% }"; new="${new## }"
  old="${old%\"}"; old="${old#\"}"; old="${old%% }"; old="${old## }"

  if [ ! -f "$old" ]; then
    echo "MISSING SOURCE: $old"
    errors=1
  fi
  if [ -e "$new" ]; then
    echo "TARGET EXISTS (ok if intended): $new"
  fi
done < "$mapfile"

[ $errors -eq 0 ] && echo "Preflight OK." || { echo "Preflight had errors."; exit 1; }
