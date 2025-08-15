# Style Guide (v0.12)

## Dates & Codes
- Common dating: **AO** (After Ord). Pre-Ord allowed as negative AO, optional **BO** in prose (e.g., “975 BO”).
- Event codes: `EVT-####[-TAG]`. BO events: `EVT-####BO-TAG`.  
- Beats language allowed in prose: “Long Beat” (6 years), “Short Beat” (rite cadence)

## Casing / Spelling
- **Caps:** Oboe (star); Hex (moon); Old Song; Good Old Rhythm.
- **Spelling:** Ordian, Wurranian, Klr’ian; Cuzhar Krum.
- Ranges use en-dash (700–800 AO). Numbers one–nine spelled; 10+ numerals.

## IDs & Filenames
- IDs in front matter: `PERS:*`, `FAC:*`, `LOC:*`, `REG:*`, `BIO:*`, `CTP:*`, `ERA-*`, `EVT-*`.
- Filenames: lowercase `snake_case.md`.  
- Prefer one subfolder level (two for subtypes like Beats houses).  
- File format: markdown (keep schema consistent)
- Use `_cYYYY` or `_cYYYY_YYYY` for period-specific tech/doctrine/visual/lexicon pages.
- Snapshots already imply period; keep their `cXXXX` in filename.
- Entity pages, indices, and systems “root” pages stay **timeless** (no suffix).

## Tone by Document Type
- **History/Systems:** cool, concrete; let harm/brutality show via ledgers, rates, statutes.
- **Diegetic leafs:** in-world voice; 1 page; add plausible seal/signature line.
- **Entity pages:** thesis line + links; avoid purple prose.

## Timeline CSV (strict)
**Header:**
---
ao,code,title,where,who,summary,impact,refs,status
---
**Rules:**
- `where` / `who`: IDs separated by `;` (may be quoted), cleaned of stray trailing `:"` by validators.
- Avoid quotes in any field unless you must (and if you do, make sure the line still has exactly 9 comma-separated fields).`
- `refs`: `|`-separated repo paths (anchors allowed).
- Always start refs with `canon/….`
- Any field with commas must be **quoted**. Prefer commas in prose over `+`; only use `+` as a true operator or symbol.
- Status must be `Stable | Draft | Contested`.

**Validators:** `tools/validate_timeline.sh` (Bash)

## Names & Onomastics
- Keep reader load low: evocative trade names (“Seven Fingers”) + one-line native/gloss.
- Ledger-name on first mention (house-i, demonym, toponymic, or patronymic).
- House gentilics take **-i** (Zambrani); demonyms **-an/-ian** (Kllrian).
- Epithets in quotes on first use: Marr “the Skin-Grass”.
- Include optional `naming:` block in YAML for future tooling.

## Cross-File Linking
- Use a `links:` block with stable relative paths.  
- Don’t deep-link to Drafts from Stable pages (link the parent folder).

## Folder Layout (shallow, stable)
- `canon/entities/{people,places,regions,factions,biota,co_types}/`
- `canon/systems/{governance,law,tech,economy,planetology,climate,transport,security,culture,religions,health,infrastructure,language}/`
- `canon/eras/` (long-form overviews)
- `canon/timeline/point_timeline.csv` (or `.txt` mirror with the same columns)
- `canon/notes/{diegetic,rolls,snapshots,scratchpad}/`
- `canon/art_refs/`

## Front Matter Schemas (YAML)
### Entity (people/place/region/faction/biota/co-type)
```yaml
---
id: PERS:ZAM-001         # or LOC:/REG:/FAC:/BIO:/CO:
name: Thedos Zambrani
status: Stable           # Stable | Draft | Contested | Stub
aliases: [Thedos of Ord] # optional
links:
  # stable relative paths (avoid deep-linking into Drafts)
  home: canon/entities/places/ord_city.md
  related: canon/entities/factions/synod_of_beats.md
tags: [ord, leadership, reform]
---
```
## How to record linguistic drift in docs
When a term already shows variants, add an alias map in front-matter on the *base* page/Include optional block when names drift:
```yaml
aliases_by_era:
  05xx-0599: ["Ex"]        # early coastal school orthography
  0860-1050: ["Hex"]       # koiné standard at apex
  1700-1803: ["Hex","Hexe"]# modern spellings seen in pamphlets
  
  0860-1050: ["Treaty Port"]
  1150-1250: ["Contract Port","Charter Port"]
```

## Content Structure (recommended headings)
- Base System/Entity: `Thesis` · `Overview` · `Institutions/Actors` · `Practices/Law` · `Economics/Logistics` · `Risks/Failure Modes` · `Cross-refs`.
- Overlay: “What changes from base” · `Effects` · `Hooks` · `Cross-refs`. Keep overlays focused; no repetition of base aside from a short thesis.