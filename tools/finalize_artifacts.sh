#!/usr/bin/env bash
# tools/finalize_artifacts.sh
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

UPLOAD_DIR="tools/upload_ready"
REPORTS_DIR="tools/reports"
mkdir -p "$UPLOAD_DIR" "$REPORTS_DIR"

# timestamp like 2025-08-19-123045
TS="$(date +"%Y-%m-%d-%H%M%S")"

copy_or_move() {
  local src="$1" dest="$2"
  if [[ -n "${CLEANUP_MOVE:-}" && "$CLEANUP_MOVE" == "1" ]]; then
    mv -v -- "$src" "$dest"
  else
    # copy, preserve original file for future runs
    cp -v -- "$src" "$dest"
  fi
}

# --- 1) Upload-ready items ---
# router_index.md (always under tools/)
if [[ -f "tools/router_index.md" ]]; then
  copy_or_move "tools/router_index.md" "$UPLOAD_DIR/router_index.md"
else
  echo "[warn] tools/router_index.md not found (did router_lite.py run?)"
fi

# front_matter_anthology.md (often at repo root; also check tools/)
if [[ -f "front_matter_anthology.md" ]]; then
  copy_or_move "front_matter_anthology.md" "$UPLOAD_DIR/front_matter_anthology.md"
elif [[ -f "tools/front_matter_anthology.md" ]]; then
  copy_or_move "tools/front_matter_anthology.md" "$UPLOAD_DIR/front_matter_anthology.md"
else
  echo "[warn] front_matter_anthology.md not found"
fi

# (Optional) build a single combined file for upload
if [[ -f "$UPLOAD_DIR/router_index.md" && -f "$UPLOAD_DIR/front_matter_anthology.md" ]]; then
  cat "$UPLOAD_DIR/router_index.md" "$UPLOAD_DIR/front_matter_anthology.md" > "$UPLOAD_DIR/index_pack.md"
  echo "[ok] wrote $UPLOAD_DIR/index_pack.md"
fi

# --- 2) Reports with timestamp suffixes ---
# list: link_targets.tsv id_to_path.csv link_errors.tsv link_report.tsv link_summary.md
for f in tools/link_targets.tsv tools/id_to_path.csv tools/link_errors.tsv tools/link_report.tsv tools/link_summary.md; do
  if [[ -f "$f" ]]; then
    base="$(basename "$f")"
    name="${base%.*}"
    ext="${base##*.}"
    if [[ "$ext" == "$base" ]]; then
      # no extension
      dest="$REPORTS_DIR/${name}_${TS}"
    else
      dest="$REPORTS_DIR/${name}_${TS}.${ext}"
    fi
    copy_or_move "$f" "$dest"
  fi
done

echo "[done] finalize_artifacts completed."
