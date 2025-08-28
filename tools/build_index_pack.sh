#!/usr/bin/env bash
set -euo pipefail

# ==== Flags (env) ====
# OUT: output Markdown path. A .txt twin is also written next to it.
OUT="${OUT:-tools/new_index/index_pack.md}"
# OUT_BASENAME: base path used for the .txt twin (default = OUT without .md)
OUT_BASENAME="${OUT_BASENAME:-${OUT%.md}}"
# WARN_CRLF: 0 to make it actually shut up
WARN_CRLF="${WARN_CRLF:-1}"
# INCLUDE_THESIS: 1 to include a THESIS map (ID<TAB>one-line thesis); default 0.
INCLUDE_THESIS="${INCLUDE_THESIS:-0}"
# INCLUDE_ALIASES: 1 to include an ALIASES map (ID<TAB>a|b|c from front-matter); default 0.
INCLUDE_ALIASES="${INCLUDE_ALIASES:-0}"
# INCLUDE_BACKLINKS: 1 to include BACKLINKS (target_path<TAB>src_id<TAB>src_path from links:); default 0.
INCLUDE_BACKLINKS="${INCLUDE_BACKLINKS:-0}"
# INCLUDE_RETIRED: 1 to scan files under retired/; default 0.
INCLUDE_RETIRED="${INCLUDE_RETIRED:-0}"
# SANITIZE_ASCII: 1 to normalize CRLF->LF, tabs->spaces, and ASCII-transliterate output; default 1.
SANITIZE_ASCII="${SANITIZE_ASCII:-1}"
# QUIET: 1 to suppress progress logs; default 0.
QUIET="${QUIET:-0}"
# ROOT: repo root override; default = `git rev-parse --show-toplevel` or $PWD.
ROOT="${ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"

mkdir -p "$(dirname "$OUT")"
log() { [ "$QUIET" = "1" ] || printf '%s\n' "$*" >&2; }

# ---- File listing (tracked + untracked .md, normalized paths) ----
list_files() {
  (
    cd "$ROOT" || exit 0
    {
      git ls-files '*.md' 2>/dev/null
      find . -type f -name '*.md' -print 2>/dev/null
    } \
    | sed 's|^\./||' \
    | tr '\\\\' '/' \
    | sort -u \
    | grep -Ev '^(tools/upload_ready/|\.git/|node_modules/|vendor/|\.venv/)' \
    | grep -E  '^canon/.*\.md$' \
    | grep -Ev '^(canon/(02_style_guide|03_LLM_.*)\.md)$' || true \
    | { if [ "$INCLUDE_RETIRED" = "1" ]; then cat; else grep -Ev '^retired/'; fi; } || true
  )
}

# ---- Front-matter parser → TSV: ID<TAB>PATH<TAB>THESIS<TAB>ALIASES<TAB>LINKPATHS ----
parse_file() {
  local rel="$1" abs="$ROOT/$rel" has_crlf=""
  if awk 'sub(/\r$/,""){f=1} END{exit f?0:1}' "$abs"; then has_crlf="CRLF"; fi
  awk -v rel="$rel" -v has_crlf="$has_crlf" -v warn_crlf="${WARN_CRLF:-1}" '
    BEGIN{ fm=0; id=""; thesis=""; aliases=""; in_alias=0; in_links=0; in_thesis=0; links=""; }
    NR==1 && $0 ~ /^---[[:space:]]*$/ { fm=1; next }
    fm==1 && $0 ~ /^---[[:space:]]*$/ { fm=2; next }
    fm!=1 { next }  # only first front-matter

    { gsub(/\r/,""); }

    $0 ~ /^id:[[:space:]]*/ { sub(/^id:[[:space:]]*/,""); id=$0; gsub(/^[[:space:]]+|[[:space:]]+$/,"",id); next }

    $0 ~ /^thesis:[[:space:]]*$/ { in_thesis=1; thesis=""; next }
    $0 ~ /^thesis:[[:space:]]+/ && in_thesis!=1 { sub(/^thesis:[[:space:]]*/,""); thesis=$0; next }
    in_thesis==1 {
      if ($0 ~ /^[a-zA-Z0-9#_-]+:[[:space:]]*/) { in_thesis=0 }
      else { line=$0; gsub(/^[[:space:]]+|[[:space:]]+$/,"",line);
             if (line!="") { if (thesis!="") thesis=thesis" "; thesis=thesis line; } next }
    }

    $0 ~ /^aliases:[[:space:]]*\[/ { s=$0; sub(/^aliases:[[:space:]]*\[/,"",s); sub(/\][[:space:]]*$/,"",s);
      gsub(/[[:space:]]*/,"",s); gsub(/"+|'\''/,"",s); gsub(/,/,"|",s); aliases=s; in_alias=0; next }
    $0 ~ /^aliases:[[:space:]]*$/ { in_alias=1; next }
    in_alias==1 && $0 ~ /^[[:space:]]*-[[:space:]]*/ {
      s=$0; sub(/^[[:space:]]*-[[:space:]]*/,"",s);
      gsub(/^[[:space:]]+|[[:space:]]+$/,"",s); gsub(/"+|'\''/,"",s);
      if (aliases!="") aliases=aliases"|"; aliases=aliases s; next
    }
    in_alias==1 && $0 !~ /^[[:space:]]*-/ { in_alias=0 }

    $0 ~ /^links:[[:space:]]*$/ { in_links=1; next }
    in_links==1 {
      if ($0 ~ /^[^[:space:]]/ || $0 ~ /^$/) { in_links=0; next }
      if ($0 ~ /^[[:space:]]+[a-zA-Z0-9_]+:[[:space:]]*/) {
        line=$0; sub(/^[[:space:]]*[a-zA-Z0-9_]+:[[:space:]]*/,"",line);
        gsub(/^[[:space:]]+|[[:space:]]+$/,"",line);
        if (line ~ /^canon\//) { if (links!="") links=links"|"; links=links line; }
        else if (line!="") { printf("BAD_LINK_PATH\t%s\t%s\n", id, $0) > "/dev/stderr"; }
      }
      next
    }

    END{
      gsub(/[[:space:]]+/," ",thesis); gsub(/\t/," ",thesis);
      # Flag only if it looks like a path: "canon/…", "*.md", or token/token with no spaces
      if (thesis ~ /(^|[[:space:]])canon\/|\.md($|[[:space:]])|[A-Za-z0-9._-]+\/[A-Za-z0-9._-]+/) {
      if (thesis!="") printf("THESIS_PATH\t%s\n", rel) > "/dev/stderr";
      thesis="";
    }

      if (length(thesis) > 240) thesis=substr(thesis,1,240);

      if (id=="") { printf("MISSING_ID\t%s\n", rel) > "/dev/stderr"; exit 0 }

      printf("%s\t%s\t%s\t%s\t%s\n", id, rel, thesis, aliases, links);
      if (has_crlf!="" && warn_crlf=="1") printf("CRLF\t%s\n", rel) > "/dev/stderr";
    }

  ' "$abs"
}

# ---- Temp stores ----
tmpdir="$(mktemp -d)"; trap 'rm -rf "$tmpdir"' EXIT
manifest="$tmpdir/manifest.tsv"; : >"$manifest"
thesis_map="$tmpdir/thesis.tsv"; : >"$thesis_map"
aliases_map="$tmpdir/aliases.tsv"; : >"$aliases_map"
backlinks="$tmpdir/backlinks.tsv"; : >"$backlinks"
warnings="$tmpdir/warn.tsv"; : >"$warnings"

# ---- Scan ----
filelist="$tmpdir/files.txt"
list_files > "$filelist"
files_count="$(wc -l < "$filelist" | tr -d '[:space:]')"
log "Scanning markdown files... ($files_count found)"

while IFS= read -r rel; do
  [ -n "$rel" ] || continue
  out="$(parse_file "$rel" 2>>"$warnings" || true)"
  [ -n "$out" ] || continue
  while IFS=$'\t' read -r id path thesis aliases links; do
    printf "%s\t%s\n" "$id" "$path" >>"$manifest"
    [ "$INCLUDE_THESIS" = "1" ] && [ -n "$thesis" ] && printf "%s\t%s\n" "$id" "$thesis" >>"$thesis_map"
    [ "$INCLUDE_ALIASES" = "1" ] && [ -n "$aliases" ] && printf "%s\t%s\n" "$id" "$aliases" >>"$aliases_map"
    if [ "$INCLUDE_BACKLINKS" = "1" ] && [ -n "$links" ]; then
      IFS='|' read -r -a arr <<<"$links"
      for tgt in "${arr[@]}"; do printf "%s\t%s\t%s\n" "$tgt" "$id" "$path" >>"$backlinks"; done
    fi
  done <<< "$out"
done < "$filelist"

# ---- Resolve duplicates ----
log "Resolving duplicates..."
resolved="$tmpdir/resolved.tsv"
sort -u "$manifest" > "$tmpdir/manifest.sorted.tsv"
awk -F'\t' '
  {
    id=$1; path=$2; retired = (path ~ /^retired\//) ? 1 : 0;
    if (!(id in best)) { best[id]=path; br[id]=retired; next }
    cur=best[id]; cr=br[id];
    if (cr==1 && retired==0) { best[id]=path; br[id]=retired; next }
    if (cr==retired && length(path) < length(cur)) { best[id]=path; br[id]=retired; next }
    dups[id]=(dups[id]==""?best[id]"|"path:dups[id]"|"path)
  }
  END{
    for (k in best) printf("%s\t%s\n", k, best[k]);
    for (k in dups) if (dups[k]!="") printf("DUPLICATE_ID\t%s\t%s\n", k, dups[k]) > "/dev/stderr";
  }
' "$tmpdir/manifest.sorted.tsv" > "$resolved" 2>>"$warnings"

ids_count="$(wc -l < "$resolved" | tr -d '[:space:]')"
warn_count="$( [ -s "$warnings" ] && wc -l < "$warnings" | tr -d '[:space:]' || echo 0 )"

# ---- Write pack ----
log "Writing $OUT ..."
{
  printf "# INDEX_PACK v1\n"
  printf "# BUILT: %s\n" "$(date -u +%FT%TZ)"
  printf "# ROOT: %s\n" "$ROOT"
  printf "# STATS: %s IDs, %s files, %s warnings\n\n" "$ids_count" "$files_count" "$warn_count"

  printf "# ID->PATH (MIN)\n"
  sort -k1,1 "$resolved"
  printf "\n"

  if [ "$INCLUDE_THESIS" = "1" ] && [ -s "$thesis_map" ]; then
    printf "# THESIS (OPTIONAL)\n"
    sort -k1,1 "$thesis_map"
    printf "\n"
  fi

  if [ "$INCLUDE_ALIASES" = "1" ] && [ -s "$aliases_map" ]; then
    printf "# ALIASES (OPTIONAL)\n"
    sort -k1,1 "$aliases_map"
    printf "\n"
  fi

  if [ "$INCLUDE_BACKLINKS" = "1" ] && [ -s "$backlinks" ]; then
    printf "# BACKLINKS (OPTIONAL)\n"
    sort -k1,1 -k2,2 "$backlinks"
    printf "\n"
  fi

  if [ -s "$warnings" ]; then
    printf "# WARNINGS (OPTIONAL)\n"
    sort -u "$warnings"
    printf "\n"
  fi
} > "$OUT"

# ---- Sanitize & .txt twin ----
if [ "$SANITIZE_ASCII" = "1" ]; then
  tmp="$OUT.tmp"
  sed 's/\r$//' "$OUT" | expand -t 2 > "$tmp"
  if command -v iconv >/dev/null 2>&1; then
    iconv -f UTF-8 -t ASCII//TRANSLIT "$tmp" > "${tmp}.a" && mv "${tmp}.a" "$tmp"
  fi
  mv "$tmp" "$OUT"
fi
cp "$OUT" "${OUT_BASENAME}.txt"

log "Done: $OUT (and ${OUT_BASENAME}.txt)"
