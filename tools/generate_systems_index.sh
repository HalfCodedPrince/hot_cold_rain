#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"
OUT="$ROOT/tools/_systems_index.md"
: > "$OUT"

# collect: folder, id, name, path
tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT

while IFS= read -r -d '' f; do
  rel="${f#"$ROOT/"}"
  sub="${rel#canon/systems/}"
  group="${sub%%/*}"               # top-level under systems/
  [ "$group" = "$sub" ] && group="(root)"
  id="$(awk '
    BEGIN{fm=0}
    /^---[ \t]*$/ { if(fm==0){fm=1; next} else if(fm==1){exit} }
    fm==1 && /^id:[ \t]*/  { s=$0; sub(/^id:[ \t]*/,"",s); gsub(/^[ \t]+|[ \t]+$/,"",s); print s; exit }
  ' "$f")"
  name="$(awk '
    BEGIN{fm=0}
    /^---[ \t]*$/ { if(fm==0){fm=1; next} else if(fm==1){exit} }
    fm==1 && /^name:[ \t]*/{ s=$0; sub(/^name:[ \t]*/,"",s); gsub(/^[ \t]+|[ \t]+$/,"",s); print s; exit }
  ' "$f")"
  printf "%s\t%s\t%s\t%s\n" "$group" "${id:-?}" "${name:-?}" "$rel" >> "$tmp"
done < <(git ls-files -z -- 'canon/systems/**/*.md')

# print grouped, sorted nicely
awk -F'\t' '
  BEGIN{print "# Systems — auto-index\n"}
  { arr[$1]=arr[$1] sprintf("- **%s** (`%s`): `%s`\n",$3,$2,$4) }
  END{
    n=asorti(arr,keys)
    for(i=1;i<=n;i++){
      key=keys[i]
      g=key; g=toupper(substr(g,1,1)) substr(g,2)
      printf("\n## %s\n\n", g)
      printf("%s\n", arr[key])
    }
  }
' "$tmp" >> "$OUT"

echo "Wrote $OUT"
