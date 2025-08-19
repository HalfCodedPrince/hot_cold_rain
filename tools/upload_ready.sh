#!/usr/bin/env bash
# tools/upload_ready.sh
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

echo "[run] repo root: $ROOT"

run_if_exists() {
  local path="$1"; shift || true
  if [[ -x "$path" ]]; then
    echo "[run] $path $*"
    "$path" "$@"
  elif [[ -f "$path" ]]; then
    echo "[run] sh $path $*"
    sh "$path" "$@"
  else
    echo "[skip] $path not found"
  fi
}

# 1) snapshots
run_if_exists "tools/make_snapshot.sh"

# 2) systems index (support either file name)
if [[ -f "tools/generate_systems_index.sh" || -x "tools/generate_systems_index.sh" ]]; then
  run_if_exists "tools/generate_systems_index.sh"
else
  run_if_exists "tools/make_systems_index.sh"
fi

# 3) router lite heatmap
if command -v python >/dev/null 2>&1; then
  echo "[run] python tools/router_lite.py"
  python -u "tools/router_lite.py"
else
  echo "[error] python not found in PATH"; exit 2
fi

# 4) validate links (emit report + link_targets.tsv)
VALIDATE_ARGS=(--root . --out tools/link_report.tsv --emit-link-targets tools/link_targets.tsv --warn-anchors)
if [[ -n "${VALIDATE_NO_CASE:-}" && "$VALIDATE_NO_CASE" == "1" ]]; then
  VALIDATE_ARGS+=(--no-case)
fi
echo "[run] python tools/validate_links.py ${VALIDATE_ARGS[*]}"
# IMPORTANT: don't stop the pipeline if validate exits non-zero (it does when problems are found)
if ! python -u "tools/validate_links.py" "${VALIDATE_ARGS[@]}"; then
  echo "[warn] validate_links reported problems (non-zero exit). Continuing to filter & finalize…"
fi

# 5) filter report (errors + warnings) -> ensure outputs exist
FILTER_SCRIPT="tools/filter_link_report.py"
if [[ ! -f "$FILTER_SCRIPT" ]]; then
  # fallback to a possible alternate name
  FILTER_SCRIPT="tools/filter_links_report.py"
fi
if [[ -f "$FILTER_SCRIPT" ]]; then
  echo "[run] python $FILTER_SCRIPT --in tools/link_report.tsv --out tools/link_errors.tsv --md tools/link_summary.md --status-prefix 'ERR|WARN'"
  python -u "$FILTER_SCRIPT" --in tools/link_report.tsv --out tools/link_errors.tsv --md tools/link_summary.md --status-prefix 'ERR|WARN'
else
  echo "[warn] $FILTER_SCRIPT not found; skipping filtered outputs"
fi

# 6) file everything into upload_ready/ and reports/ (timestamped)
echo "[run] bash tools/finalize_artifacts.sh"
bash "tools/finalize_artifacts.sh"

echo "[done] upload_ready pipeline complete."
