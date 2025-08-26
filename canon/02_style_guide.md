# Style Guide (v0.14)
---

## IDs & Filenames
- IDs in front matter: `PERS:*`, `FAC:*`, `LOC:*`, `REG:*`, `BIO:*`, `CO:*`, `CO:DIA-*` (for Co-Type dialects) `SYS:*`, `SNAP:*`, `ERA-*`, `EVT-`
- Filenames: lowercase `snake_case.md`.  
- Prefer one subfolder level (two for subtypes like Beats houses).  
- File format: markdown (keep schema consistent)
- Use `_cYYYY` or `_cYYYY_YYYY` for period-specific tech/doctrine/visual/lexicon pages.
- Snapshots already imply period; keep their `cXXXX` in filename.
- Entity pages, indices, and systems “root” pages stay **timeless** (no suffix).

## Tone by Document Type
- **History/Systems:** cool, concrete; let harm/brutality show via ledgers, rates, statutes.
- **Diegetic leafs:** in-world voice; 1 page; add plausible seal/signature line, don't forget header
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

**Stable mechanics** (for example, solar system): …/<topic>.md

**Periodized mechanics**: …/<topic>_cYYYY[–YYYY].md

**World snapshots**: canon/notes/snapshots/<domain>/<domain>_cYYYY[–YYYY].md
Do not invent new domains unless absolutley have to.

---

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

## Dates & Codes (mainly for timeline.csv)
- Common dating: **AO** (After Ord). Pre-Ord allowed as negative AO, optional **BO** in prose (e.g., “975 BO”).
- Event codes: `EVT-####[-TAG]`. BO events: `EVT-####BO-TAG`.  
- Beats language allowed in prose: "Long Beat" (6 years), "Short Beat" (rite cadence), "hexad" (6 day week)

## Casing / Spelling
- **Caps:** Oboe (star); Hex (moon); Old Song; Good Old Rhythm.
- **Spelling:** Ordian, Wurranian, Klr’ian; Cuzhar Krum.
- **Ranges** use en-dash (700–800 AO). **Numbers** one–nine spelled; **10+ numerals** - no senary (6-base) math madness, we've been there, it's a bad place.

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
- `canon/eras/` (the biggest picture, in dynamic, mainly to show historical vectors, not just at the moment in time)
- `canon/timeline/point_timeline.csv` (timeline with historical events)
- `canon/notes/snapshots` (broad, world-state overviews at a *fixed* point in time)
- `canon/entities/{people,biota,co_types}/` (important historical figures/flora/fauna)
- `canon/systems/{system_type}/` (building blocks for eras abnd snapshots, contains mechanics, institutions, standards, law, tech workings, etc. Could be stable (like solar system params) or versioned by period)
- `canon/current/goalpost` (the initial outline of “where we are headed”)
- `canon/current/final` (the final outline, based the whole project, the last step)


## Front Matter (YAML)
We **don’t** use boolean flags like `overlay: true`. Page intent is expressed via:
- `status:` (Stable | Draft | Contested)
- file placement (Snapshots vs Systems)
- filename period markers (`_cYYYY[_YYYY]`)
- redirects (if ABSOLUTELY have to) via `links.moved_to: <new/path.md>`

## Front Matter Schemas (YAML)

### Entity (people/place/region/faction/biota/co-type)
```yaml
---
id: PERS:ZAM-001         # or LOC:/REG:/FAC:/BIO:/CO:
name: Thedos Zambrani
status: Stable           # Stable | Draft | Contested 
aliases: [Thedos of Ord] # optional
links:
  # stable relative paths (avoid deep-linking into Drafts)
  home: canon/systems/geography/places/ord_city.md
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
- Base System/Entity: `Thesis` · `Overview` · `Institutions/Actors` · `Practices/Law` · `Economics/Logistics` · `Risks/Failure Modes`

## Links (example for standardization)
  **systems & snapshots (primary)**
  governance: canon/systems/governance/centralization_levers_principality_c1400_1550.md
  law_admin: canon/systems/governance/law_admin.md
  print: canon/systems/print/pamphlet_economy_c1400_1503.md
  metrology: canon/systems/metrology/calendar_base6.md
  insurance: canon/systems/insurance/green_years_standard.md
  industry: canon/systems/industry/proto_industry_c1290_1400.md
  clinics: canon/notes/snapshots/special/co_types_biology_and_law.md

  **religion/era (secondary)**
  rhythm: canon/systems/religions/good_old_rhythm.md
  era_09: canon/eras/09_pamphlet_wars_1400_1503.md

  **maps & references (tertiary)**
  map_mutation_day: canon/notes/maps/map_mutation_day.yaml


# Appendix: Project Guardrails (GPT collaborator)

- **Lore-first.** Check every change against current lore; do not “upgrade” plot or systems ad hoc.
- **Repo as ground truth.** Only reference files that exist in the currently uploaded project set or in the user’s pasted snippet.
  - If a reference seems necessary but no file exists, mark it explicitly as a *proposed new stub*.
- **No silent renames.** Do not add/remove small words (“of”, “the”, etc.) in filenames or titles unless you’re explicitly proposing a rename.
- **Snippets are authoritative.** When a file is pasted in chat, treat that snippet as the canonical version for this pass. If you recall older drafts, label them “earlier memory (discard if outdated).”
- **Cross-file linking.**
  - Use `links:` with stable relative paths only.
  - Don’t re-propose links already present in `links:`.
  - Prefer symmetric links (propose reciprocal updates when relevant).
  - **Stable → Draft:** avoid deep-linking a Stable page to a Draft leaf; point to the stable parent/collection instead. Draft↔Draft and Stable↔Stable leaf links are fine.
- **Output format.** Post `.md` text directly in chat with the path and proposed filename. Proposing additions to existing files is allowed; don’t attach external files.

---

## Editing Workflow (LLM-facing)

**Overarching directives**:
- Treat index_pack.md as required pre-read for: ID/path resolution, overview membership, status, aliases, and link-key sanity. It is in the core upload set, so reliance is safe.

**Scope lock**
- Each task starts by stating: `file`, `ops`, `forbid`, `mode`.
- If a referenced file is unseen, request a snippet or propose `[NEW STUB]` and stop there.

**Style preflight**
- Check filename, front-matter keys, `links:` shape, tag casing, and ranges per this guide.
- Use only a `links:` block for inter-file references; do not insert inline prose about other files.  
  (See “Cross-File Linking”.)

**Tooling discipline**
- For link/back-link work, the assistant MUST query `index_pack.md` and the domain overview’s `links:` using the search tool before proposing changes.
- Response must include a short `LookupLog:` listing each file checked and the result: FOUND / MISSING / INCONCLUSIVE.
- If INCONCLUSIVE, no proposal is made in STRICT mode; ask ≤3 questions.
- Require verify-backlink before proposing any back-link.
- Require anchors to validate table anchors.
- Require LookupLog: in the delivery with the exact commands + outputs you ran.

**Repo ground truth**
- Only rely on the pasted file, `00_master_index.md`, `01_glossary.md`. Anything else is `[SPECULATIVE → CONFIRM?]`.

**Edit output format**
- For each file touched, output: the path on its own line, then one fenced block with the full replacement.

**Assumption register**
- List any assumptions at the end. Empty is allowed.

**Link discipline**
- You may propose reciprocal `links:` entries in other files. No prose edits in unseen files.  
  Do not deep-link into Drafts from Stable pages; link the parent folder. 

**Validation checklist**
- `TermCheck:` new terms introduced.
- `LinkCheck:` added/changed paths.
- `ScopeCheck:` confirm only the requested areas changed.

**Modes**
- `STRICT`: zero speculation; no new terms; do not assert new entities, laws, or numbers; link only to existing pages. If a section would require new doctrine, mark it “stub proposed” and stop.
- `BUILDER`: allowed `[NEW STUB]` and clearly labeled proposals at the end under “Proposals”.

**unknowns: [...]**: is a short checklist of concrete gaps you want to resolve or avoid guessing about (e.g., “who issues licenses,” “commission ranges,” “northern cartel tie strength”). If left empty, missing facts will not be invented in STRICT mode.

**Missing-info rule**
- If anything blocks a clean pass, stop and ask ≤3 pointed questions.

## Priority & Precedence

1) **Pasted snippet in chat** → authoritative for this pass.  
2) **02_style_guide.md** (this file).  
3) **00_master_index.md** and **index_pack.md** (IDs, paths, overview membership).  
4) **01_glossary.md** (terms allowed).  
5) Everything else = **[SPECULATIVE → CONFIRM?]**.

When rules collide: **Workflow** instructions override Appendix phrasing. “Cross-file linking” rules govern links.

...

**Task template**
```yaml
# Use "!" to select the active mode
TASK
mode: !STRICT | BUILDER
file: canon/.../your_file.md
ops: [style_check, lore_check, expansions, link_backlinks]
forbid: [no_prose_in_other_files, repo_ground_truth_only]
unknowns: [...]  # concrete gaps to resolve or avoid guessing
```


---

# See also: Entry Points

For navigation and context, see:

- **README.md** — repo/tooling overview (scripts, outputs, shortcuts).
- **00_master_index.md** — canon-facing landing page (hand-curated map).
- **01_glossary.md** — canonical terms
- **canon/notes/maps/map_reference.yaml** — LLM-friendly geography anchor