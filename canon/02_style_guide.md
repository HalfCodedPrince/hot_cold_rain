# Style Guide (v0.12)

## Dates & Codes
- Dates use **AO** (After the founding of Ord City). Pre-Ord may show **BO** in prose, but timeline uses negative AO.
- Event codes: `EVT-####[-TAG]` (e.g., `EVT-0746-TAM-D`); era codes: `ERA-##` (06–14 reserved for post-Cadence).
- “Beat” time: Long Beat = six years; Short Beat = rite cadence.

## IDs & Filenames
- IDs: `PERS:*`, `LOC:*`, `REG:*`, `FAC:*`, `BIO:*` (biota), `CO:*` (co-type), `SYS:*` (system doc), `ERA-*`, `EVT-*`.
- Filenames: **lowercase snake_case.md**. Overlays use suffix: `<basename>.<era_code>_<handle>.md` (e.g., `law_admin.09_green_skies.md`).
- Keep one canonical “base” doc per topic (timeless); period changes live in overlays colocated with the base.

## Folder Layout (shallow, stable)
- `canon/entities/{people,places,regions,factions,biota,co_types}/`
- `canon/systems/{governance,law,tech,economy,planetology,climate,transport,security,culture,religions,health,infrastructure,language}/`
- `canon/eras/` (long-form overviews)
- `canon/timeline/point_timeline.csv` (or `.txt` mirror with the same columns)
- `canon/notes/{diegetic,rolls,snapshots,scratchpad}/`
- `canon/art_refs/`

## CSV formatting
- No commas in summary or impact (use semicolons).`
- Avoid quotes in any field unless you must (and if you do, make sure the line still has exactly 9 comma-separated fields).`
- refs is a `|`-separated list of real files (anchors allowed, but the file must exist without the anchor).`
- Always start refs with `canon/….`

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
## Content Structure (recommended headings)
- Base System/Entity: `Thesis` · `Overview` · `Institutions/Actors` · `Practices/Law` · `Economics/Logistics` · `Risks/Failure Modes` · `Cross-refs`.
- Overlay: “What changes from base” · `Effects` · `Hooks` · `Cross-refs`. Keep overlays focused; no repetition of base aside from a short thesis.