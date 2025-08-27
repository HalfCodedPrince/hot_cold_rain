# Style Guide (v0.15)

## IDs & Filenames
- IDs in front matter: `PERS:*`, `FAC:*`, `LOC:*`, `REG:*`, `BIO:*`, `CO:*`, `CO:DIA-*` (for Co-Type dialects), `SYS:*`, `IND:*`, `INFRA:*`, `TECH:*`, `LAW:*`, `REL:*`, `SNAP:*`, `ERA-*`, `EVT-`
- Filenames: lowercase `snake_case.md`.
- Prefer one subfolder level (two for subtypes like Beats houses).
- File format: markdown (keep schema consistent).
- Use `_cYYYY` or `_cYYYY_YYYY` for period-specific tech/doctrine/visual/lexicon pages.
- Snapshots already imply period; keep their `cXXXX` in filename.
- Entity pages, indices, and systems “root” pages stay **timeless** (no suffix).

## Overall tone by Document Type
- **Systems/Snapshots/Eras/Current:** cool, concrete; let harm/brutality show via ledgers, rates, statutes.
- **Diegetic leafs:** in-world voice; 1 page; add plausible seal/signature line; don’t forget header.
- **Entity pages:** thesis line + links; avoid purple prose.

---

## What goes where (snapshots vs systems)
### Snapshots (canon/notes/snapshots/…)
-- **Scope**: broad, world-state overviews at a point in time (e.g., tech_level_c1503.md, economy_c1503.md, societal_ramifications_green_skies_c1503_1530.md).
-- **Voice**: synoptic, comparative; cite systems with brief hooks.
-- **Names**: /<domain>_cYYYY[–YYYY].md (use ranges when needed).
**!!Don’t!!**: carry procedural detail (tenders, kit lists, penal code text).
**!!Do!!**: link to those under Systems.

### Systems (canon/systems/<pillar>/…)
-- **Scope**: mechanics, institutions, standards, law, and tech workings—stable through time or versioned by period.
-- **Voice**: operational; give models, levers, and examples.
-- **Names**: <topic>_cYYYY[–YYYY].md when period-bound; otherwise stable noun (e.g., law_admin.md, centralization_levers_principality_c1400_1550.md).

**Examples:**
✅ canon/systems/industry/foundry_discipline_1400_1550.md (standards & shop law)  
✅ canon/systems/industry/saltpeter_supply_c1500.md (supply chain model)  
✅ canon/systems/governance/green_edicts_c1503.md (statute pack; see header schema below)  
❌ not snapshots: those aren’t world overviews.

---

## File naming patterns at a glance
**Stable mechanics**: …/<topic>.md  
**Periodized mechanics**: …/<topic>_cYYYY[–YYYY].md  
**World snapshots**: canon/notes/snapshots/<domain>/<domain>_cYYYY[–YYYY].md  
Do not invent new domains unless absolutely necessary.

---

## Timeline CSV (strict)
**Header:**
---
ao,code,title,where,who,summary,impact,refs,status
---
**Rules:**
- `where` / `who`: IDs separated by `;` (may be quoted), cleaned of stray trailing `:"` by validators.
- Avoid quotes in any field unless you must (and if you do, make sure the line still has exactly 9 comma-separated fields).
- `refs`: `|`-separated repo paths (anchors allowed).
- Always start refs with `canon/….`
- Any field with commas must be **quoted**. Prefer commas in prose over `+`; only use `+` as a true operator or symbol.
- Status must be `Stable | Draft | Contested`.

## Dates & Codes (mainly for timeline.csv)
- Common dating: **AO** (After Ord). Pre-Ord allowed as negative AO, optional **BO** in prose (e.g., “975 BO”).
- Event codes: `EVT-####[-TAG]`. BO events: `EVT-####BO-TAG`.
- Beats language allowed in prose: "Long Beat" (6 years), "Short Beat" (rite cadence), "hexad" (6-day week).

## Casing / Spelling
- **Caps:** Oboe (star); Hex (moon); Old Song; Good Old Rhythm.
- **Spelling:** Ordian, Wurranian, Klr’ian; Cuzhar Krum.
- **Ranges** use en-dash (700–800 AO). **Numbers** one–nine spelled; **10+ numerals** — no senary (6-base) math.

---

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
- `canon/eras/` (big picture; vectors, not just snapshots)
- `canon/timeline/point_timeline.csv` (timeline with historical events)
- `canon/notes/snapshots` (broad overviews at a *fixed* point in time)
- `canon/entities/{people,biota,co_types}/` (figures/flora/fauna)
- `canon/systems/{system_type}/` (mechanics, institutions, standards, law, tech)
- `canon/current/goalpost` (where we are headed)
- `canon/current/final` (final outline)

## Front Matter (YAML)
We **don’t** use boolean flags like `overlay: true`. Page intent is expressed via:
- `status:` (Stable | Draft | Contested)
- file placement (Snapshots vs Systems)
- filename period markers (`_cYYYY[_YYYY]`)
- redirects (only if needed) via `links.moved_to: <new/path.md>`

## Front Matter Schemas (YAML)

### Entity (people/place/region/faction/biota/co-type)
```yaml
---
id: PERS:ZAM-001
name: Thedos Zambrani
status: Stable
aliases: [Thedos of Ord]
links:
  home: canon/systems/geography/places/ord_city.md
  related: canon/entities/factions/synod_of_beats.md
tags: [ord, leadership, reform]
---
````

## How to record linguistic drift in docs: 
## when a term shows variants, add an alias map in front-matter on the *base* page:

```yaml
aliases_by_era:
  05xx-0599: ["Ex"]
  0860-1050: ["Hex"]
  1700-1803: ["Hex","Hexe"]

  0860-1050: ["Treaty Port"]
  1150-1250: ["Contract Port","Charter Port"]
```

## Content Structure (recommended headings)

* Base System/Entity: `Thesis` · `Overview` · `Institutions/Actors` · `Practices/Law` · `Economics/Logistics` · `Risks/Failure Modes`

## Links (example for standardization)
```yaml
# systems & snapshots (primary)
governance: canon/systems/governance/centralization_levers_principality_c1400_1550.md
law_admin: canon/systems/governance/law_admin.md
print: canon/systems/print/pamphlet_economy_c1400_1503.md
metrology: canon/systems/metrology/calendar_base6.md
insurance: canon/systems/insurance/green_years_standard.md
industry: canon/systems/industry/proto_industry_c1290_1400.md
clinics: canon/notes/snapshots/special/co_types_biology_and_law.md

# religion/era (secondary)
rhythm: canon/systems/religions/good_old_rhythm.md
era_09: canon/eras/09_pamphlet_wars_1400_1503.md

# maps & references (tertiary)
map_mutation_day: canon/notes/maps/map_mutation_day.yaml
```