# Style Guide (v0.11)

## Dates & Codes (AO / BO)
- Use **AO** (After the founding of Ord City) for common dating.
- **Pre-Ord** dates are negative AO (e.g., -975 AO) and may be labeled **BO** in prose for clarity (“975 BO”).
- Event codes for BO dates: `EVT-####BO-TAG` (e.g., `EVT-0930BO-ZIG`), while the `ao` field in the timeline remains a negative integer for sortability.
- Use **Beat** language when relevant: “Long Beat” (six years), “Short Beat” (rite cadence).

- **Caps**: Oboe (star); Ex (moon); Old Song; Good Old Rhythm.
- **Spelling**: Ordian, Wurranian, Klr’ian, Cuzhar Krum.
- **Ranges**: en-dash (700–800 AO).
- **Numbers**: one–nine spelled; 10+ numerals.

## IDs & Filenames
- Use IDs in text and data: `PERS:*`, `LOC:*`, `FAC:*`, `EVT-*`, `ERA-*`.
- Filenames: lowercase `snake_case.md`. Prefer Markdown with YAML front matter.
- Legacy `.yaml` entity files are being migrated to `.md`. Keep schemas consistent during transition.

## Tone by Document Type
- **History/System pages:** academically cool, concrete; let harm/brutality show via ledgers, rates, statutes (esp. for labor/slavery).
- **Diegetic leafs:** in-world voice; keep to one page; include a plausible seal/signature line.
- **Entity pages:** short thesis line + links; avoid purple prose.

## Timeline CSV
Header must be:  
`ao,code,title,where,who,summary,impact,refs,status`

Rules:
- `where`/`who` prefer IDs (`LOC:*`, `PERS:*`, `FAC:*`).
- `refs` must be existing paths.
- `status` is `Stable`, `Draft`, or `Contested`.

## Capitalization & Names
- Keep reader load low: use evocative trade names (“Seven Fingers”) with one-line native/gloss in place files.
- Avoid Latinized plurals unless diegetic.

## Cross-File Linking
- In each entity/system page, keep a `links:` block with stable relative paths.
- Don’t deep-link to drafts from Stable pages (link the parent folder instead).