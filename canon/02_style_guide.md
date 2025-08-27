# Style Guide (v0.17)
---

## IDs & Filenames
- IDs in front matter: `PERS:*`, `FAC:*`, `LOC:*`, `REG:*`, `BIO:*`, `CO:*`, `CO:DIA-*`, `SYS:*`, `IND:*`, `INFRA:*`, `TECH:*`, `LAW:*`, `REL:*`, `SNAP:*`, `ERA-*`, `EVT-`
- Filenames: lowercase `snake_case.md`.
- Prefer one subfolder level (two for subtypes like Beats houses).
- File format: markdown.
- Use `_cYYYY` or `_cYYYY_YYYY` for periodized pages.
- Snapshots already imply period; keep their `cXXXX`.
- Status: `Stable | Draft | Contested | Retired`.

## Overall tone by Document Type
- **Systems/Snapshots/Eras/Current:** cool, concrete; let harm/brutality show via ledgers, rates, statutes.
- **Diegetic leafs:** in-world voice; 1 page; add plausible seal/signature line; include header.
- **Entity pages:** thesis line + links; avoid purple prose.

---

## What goes where
### Constants
- `canon/constants/` — natural or civilizational invariants are not meant to be revised (e.g., fixed calendar base). Any page may link **up** to constants.

### Diachronic systems (default)
- Root: `canon/systems/diachronic/<pillar>/<family>/`
- Everything human-conventional lives here as **era leaves** only.
- File name: `<family>_cYYYY[–YYYY].md`
- Each leaf starts with a **Primer** (≤120 words). Duplicate the same Primer across the family.
- Optional `primer_rev: <int>` in front matter to track Primer changes.
- Provenance:
  ```yaml
  derived_from:
    - canon/systems/diachronic/<pillar>/<family>/<family>_cPrev.md
  era: YYYY–YYYY

### Retiring a leaf when superseded:

  ```yaml
  status: Retired
  links:
    moved_to: canon/systems/diachronic/<pillar>/<family>/<family>_cNext.md
  ```
Leaves are moved to `/retired/` after one release.

### Snapshots (point-in-time)

* `canon/snapshots/<domain>/<domain>_cYYYY[–YYYY].md`
* Scope: broad state for an era. Link to same-era diachronic leaves and constants.

---

## Timeline CSV (strict)

## **Header:**

## ao,code,title,where,who,summary,impact,refs,status

**Rules:**

* `where` / `who`: IDs separated by `;` (may be quoted).
* Avoid quotes unless necessary; keep exactly 9 comma-separated fields.
* `refs`: `|`-separated repo paths (anchors allowed), starting with `canon/…`.
* Status: `Stable | Draft | Contested`.

## Dates & Codes

* Dating: **AO**; BO allowed as negative AO or prose “BO”.
* Event codes: `EVT-####[-TAG]`; BO: `EVT-####BO-TAG`.
* Beats allowed: "Long Beat" (6y), "Short Beat", "hexad" (6-day week).

## Casing / Spelling

* Caps: Oboe; Hex; Old Song; Good Old Rhythm.
* Spelling: Ordian, Wurranian, Klr’ian; Cuzhar Krum.
* Ranges use en-dash (700–800 AO). Numbers one–nine spelled; 10+ numerals.

---

## Names & Onomastics

* Keep reader load low: evocative trade names + one-line native/gloss.
* Ledger-name on first mention.
* House gentilics **-i**; demonyms **-an/-ian**.
* Epithets in quotes on first use.
* Optional `naming:` block in YAML.

## Cross-File Linking

* Use a `links:` block with stable relative paths.
* Do not deep-link to Drafts from Stable pages; link the parent collection.
* Diachronic link rules live in `03_LLM_linking_policy.md`.

## Folder Layout

* `canon/constants/`
* `canon/systems_diachronic/{broad_family}/{pillar}/`
* `canon/snapshots/`
* `canon/eras/era/{people,factiobs}/`
* `canon/eras/` (bundles, if used)
* `retired/` (optional; exclude from indices)
* `canon/endpoint/{goalpost,final}`

## Technical limits (reminders)

* Editing session file visibility is limited; keep file counts per task low.
* Header cap: **≤12 links**; header token cap: **≤300**.
* File size: warn at **12 KB**, split or trim at **18 KB**.
* Discovery source of truth: `index_pack.md`. Do not rely on folder indexes.

## Content Structure (recommended)

* Diachronic leaf: `Primer` · `Thesis` · `Changes since <prev>` · `Standards/Forms used` · `Interfaces` · `Failure Modes`
* Snapshot: `Thesis` · `What changed` · `Institutions/Actors` · `Standards (selected)` · `Risks/Failure Modes`





