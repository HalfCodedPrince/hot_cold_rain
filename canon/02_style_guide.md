# Style Guide (v0.18)
See also (meta docs):
```
canon/system_index/editing_workflow.md
canon/system_index/linking_policy.md
canon/system_index/systems_diachronic_map_core.md
```
---

## IDs & Filenames
- IDs in front matter: `PERS:*`, `FAC:*`, `LOC:*`, `REG:*`, `BIO:*`, `CO:*`, `CO:DIA-*`, `SYS:*`, `IND:*`, `INFRA:*`, `TECH:*`, `LAW:*`, `REL:*`, `SNAP:*`, `ERA-*`, `EVT-*`, `SYSIDX:*`, `INDEX:*`
- Filenames: lowercase `snake_case.md`.
- Prefer one subfolder level (two for subtypes like Beats houses).
- File format: markdown.
- Use `_cYYYY` or `_cYYYY_YYYY` for periodized pages.
- Snapshots already imply period; keep their `cXXXX`.
- Status: `Stable | Draft | Contested | Retired`.

## Overall tone by Document Type
- **Systems / Snapshots / Eras / Current:** cool, concrete; show harm via ledgers, rates, statutes.
- **Diegetic leafs:** in-world voice; 1 page; add plausible seal/signature line; include header.
- **Entity pages:** thesis line + links; avoid purple prose.

---

## What goes where

### Constants
- `canon/constants/` — natural or civilizational invariants not meant to be revised (e.g., fixed calendar base, physical regions as locators). Any page may link **up** to constants.

### Diachronic systems (default)
- Root: `canon/systems_diachronic/<family>/<pillar>/`
- Families (≤10 total): `economy/`, `governance/`, `technology/`, `culture_and_religion/`, `social_fabric/`
- Pillars (examples):
  - `economy/` → `industrial_capacity/`, `agriculture/`, `insurance_steps/`, `taxation_commerce/`, `supply_system/`
  - `governance/` → `legal_policy/`, `state_policy/`, `warfare/`, `polity_order/`, `religion_and_state/`
  - `technology/` → `broad_infrastructure/`, `communication/`, `shipbuilding_and_navigation/`
  - `culture_and_religion/` → `religious_topography/`, `sect_tenets/`, `arts_letters/`
  - `social_fabric/` → `social_strata/`, `co_types/`
- Two levels max: `family/pillar/leaf.md`
- Leaf filename: `<pillar>_cYYYY[_YYYY].md`
- Each leaf starts with a **Primer** (≤120 words). Duplicate the same Primer across that pillar; track with `primer_rev: <int>` when it changes.
- Provenance:
  ```yaml
  derived_from:
    - canon/systems_diachronic/<family>/<pillar>/<pillar>_cPREV.md
  era: YYYY–YYYY
  ```

#### Retiring a leaf when superseded
```yaml
status: Retired
links:
  moved_to: canon/systems_diachronic/<family>/<pillar>/<pillar>_cNEXT.md
```
- Keep only the newest leaf “active.” Avoid new inbound links to retired leaves. Move retired leaves under `/retired/` after one release.

### Snapshots (point-in-time)
- `canon/snapshots/<domain>/<domain>_cYYYY[_YYYY].md`
- Scope: broad state for an era; maps, “tech level” summaries.
- Link to same-era diachronic leaves and constants.
- Political entities’ maps live here; systemic political evolution lives in `governance/polity_order/*`.

---

## Timeline CSV (strict)

**Header:**
```
AO,code,title,where,who,summary,impact,refs,status
```

**Rules:**
- `where` / `who`: IDs separated by `;` (may be quoted).
- Avoid quotes unless necessary; keep exactly 9 comma-separated fields.
- `refs`: `|`-separated repo paths (anchors allowed), starting with `canon/…`.
- Status: `Stable | Draft | Contested`.

## Dates & Codes
- Dating: **AO**; BO allowed as negative AO or prose “BO”.
- Event codes: `EVT-####[-TAG]`; BO: `EVT-####BO-TAG`.
- Beats allowed: “Long Beat” (6y), “Short Beat”, “hexad” (6-day week).
- Ranges use en-dash: `700–800 AO`. Numbers one–nine spelled; 10+ numerals.

---

## Casing / Spelling
- Caps: Oboe; Hex; Old Song; Good Old Rhythm.
- Spelling: Ordian, Wurranian, Klr’ian; Cuzhar Krum.

---

## Names & Onomastics
- Keep reader load low: evocative trade names + one-line native/gloss.
- Ledger-name on first mention.
- House gentilics **-i**; demonyms **-an/-ian**.
- Epithets in quotes on first use.
- Optional `naming:` block in YAML.

---

## Cross-File Linking
- Use a `links:` block with stable relative paths.
- Deep-linking is not allowed (`#` in URLs is banned).
- Use relative paths only; no absolute or external URLs.
- BacklinkGuard: require reciprocal links between peer documents. **Exemptions:** constants and index catalogs may omit backlinks; note any exemption with a YAML comment next to the link or in the PR.
- Header cap: **≤12 links**. Follow diachronic rules in `linking_policy.md`.

---

## Folder Layout
- `canon/constants/`
- `canon/systems_diachronic/{family}/{pillar}/`
- `canon/snapshots/`
- `canon/eras/{era_name}/entities/{people,factions}`
- `canon/eras/{era_name}`
- `retired/` (optional; exclude from indices)
- `canon/endpoint/{goalpost,final}`

---

## Technical limits (reminders)
- Editing session file visibility is limited; keep file counts per task low.
- Header token cap: **≤350**.
- File size: warn at **12 KB**, split or trim at **18 KB**.
- Discovery source of truth: `index_pack.md`. Do not rely on folder indexes.

---

## Content Structure (recommended)
- Diachronic leaf: `Primer` · `Thesis` · `Changes since <prev>` · `Standards / Forms` · `Interfaces` · `Failure Modes`
- Snapshot: `Thesis` · `What changed` · `Institutions / Actors` · `Standards (selected)` · `Risks / Failure Modes`

---

## Header standard (do not deviate)
```yaml
---
id: <DOMAIN:CODE>                # required
name: <Human-readable title>     # required
status: Stable | Draft | Contested | Retired   # required
updated: YYYY-MM-DD              # required

# era-scoped pages only (diachronic leaves or snapshots)
era: YYYY–YYYY                   # optional

# diachronic leaves only
derived_from:
  - canon/systems_diachronic/<family>/<pillar>/<pillar>_cPREV.md
primer_rev: 1                    # optional, bump if Primer text changes
comparative: true                # optional, allow non-adjacent links (see policy)

# optional helper for indices; ≤140 chars; mirror body Thesis
thesis: >-
  One-line gist for builders and index tools.

# links (cap: ≤12 entries; era-adjacent; maintain BacklinkGuard)
links:
  procurement: canon/systems_diachronic/governance/state_policy/state_policy_c700_1200.md
  moved_to: canon/systems_diachronic/<family>/<pillar>/<pillar>_cNEXT.md   # when status: Retired

# tags (short, canonical)
tags: [pillar, family, key-terms]

# aliases if needed (entities or terms)
aliases: [Alt name, Older name]
---
```

## Example with primer
```yaml
---
id: SYS:PROC-700-1200
name: State Policy (c.700–1200 AO)
status: Draft
updated: 2025-08-28
era: 700–1200
derived_from:
  - canon/systems_diachronic/governance/state_policy/state_policy_c620_700.md
primer_rev: 1
links:
  legal_policy: canon/systems_diachronic/governance/legal_policy/legal_policy_c0_1200.md
tags: [policy, procurement, public-health]
---
```
# State Policy (c.700–1200 AO)

## Primer
Executive rules, procurement, public health, social policy, and censorship are published as circulars and administered by Watches and Works. Courts interpret but do not issue these rules. This family excludes courtroom procedures and doctrine; it holds execution mechanics and posted schedules.

## Thesis
…

## Changes since c.620–700
…
