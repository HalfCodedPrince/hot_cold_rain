---
id: SYSIDX:DIA-MAP-CORE
name: Systems Diachronic — Core Map
status: Draft
updated: 2025-08-28
audience: Internal
precedence: Subordinate to workflow/linking/style
notes: Canonical structure and rules; keep ≤12 KB
---

# Systems Diachronic — Core Map

## Purpose
Define what goes where inside `canon/systems_diachronic/`. Keep the tree shallow, files consistent, and links sane.

## Core rules
- Two levels max: `family/pillar/leaf.md`.
- ≤10 families total. ≤3 leaves per pillar.
- File names: `snake_case_cYYYY[_YYYY].md`.
- One active leaf per pillar; older leaves get `status: Retired`.
- No region folders. No deep-links. Header ≤12 links and ≤350 tokens.
- AO dating only; use en dashes in ranges (`700–1050 AO`).

## Directory (v3)

```
canon/systems_diachronic/
  economy/                  # exchange and flows, plus production inputs
    industrial_capacity/    # fuels, workshops, mills, yard throughput; price effects
    agriculture/            # fields, rotations, tithes, rents, granaries
    insurance_steps/        # insurer-side process and posting practice over eras
    taxation_commerce/      # trade taxes, fees, rebates, exemptions, ports’ dues
    supply_system/          # staples provisioning, convoy-as-supply, ration regimes
  governance/               # rules and institutions
    legal_policy/           # codes, courts, procedures, evidence, remedies; religious-law interface
    state_policy/           # executive rules, procurement, public health, social policy, censorship
    warfare/                # coercive use; fold land/naval/doctrine inside the leaf text
    polity_order/           # systemic evolution of polities; no maps here
    religion_and_state/     # jurisdictional interface, toleration, endowments
  technology/               # important technologies in dynamic
    broad_infrastructure/   # roads, ports, sewers, levees, city form and drainage
    communication/          # signals, mail, flags, drums, semaphores, presses
    shipbuilding_and_navigation/  # civil hulls and yards; charts, pilotage, timekeeping, nav aids
  culture_and_religion/     # culture and religion
    sect_tenets/            # doctrines, rites, calendars; lineages and schisms
    religious_topography/   # sites, pilgrim routes, shrines; non-jurisdictional
    arts_letters/           # schools, curricula, patronage, canons
  social_fabric/            # people and orders
    social_strata/          # ranks, guilds, access rights, duties
    co_types/               # Co-Type taxonomy, status, accommodations
```

## Pillar boundaries (compact)
- **economy/industrial_capacity** Throughput and inputs (fuels, power, tools, mills, yard capacity). Not builds (→ technology/broad_infrastructure); not decrees (→ governance/state_policy).
- **economy/agriculture** Fields, rotations, rents, granaries. Not city distribution (→ economy/supply_system).
- **economy/insurance_steps** Insurer process, rate postings, claim practice.
- **economy/taxation_commerce** Dues, rebates, exemptions.
- **economy/supply_system** Flows, quotas, ration windows, convoy tables, warehousing and redemption rules. Hardware of depots/quays (→ technology/broad_infrastructure).

- **governance/legal_policy** Courts and procedures; codes; remedies; evidence; religious-law interface. Not circulars/enforcement (→ governance/state_policy).
- **governance/state_policy** Executive rules, procurement, public health, social policy, licensing/censorship. Courts’ interpretation (→ governance/legal_policy).
- **governance/warfare** Coercive use; include land/naval/doctrine inside the leaf. Not shipyard capacity (→ economy/industrial_capacity or technology/broad_infrastructure).
- **governance/polity_order** Systemic view of polities across eras. Maps live in snapshots; physical regions live in constants.
- **governance/religion_and_state** Legal status of sects, endowments, courts’ reach, sanctuary rules.

- **technology/broad_infrastructure** Roads, ports, sewers, levees, raised ways, drydocks, city form/elevation logic. Not rates/quotas (→ economy/*); not decrees (→ governance/state_policy).
- **technology/communication** Beacons, flags, drums, couriers, presses, schedules. Not censorship (→ governance/state_policy); not sacred calendars (→ culture_and_religion/sect_tenets).
- **technology/shipbuilding_and_navigation** Civil hull lifecycle and navigation (charts, pilotage, currents, time, day-marks, Fog-Gates). Not combat fitouts/tactics (→ governance/warfare).

- **culture_and_religion/** Doctrines, rites, sites, canons. Licensing/taxation (→ governance/state_policy or economy/taxation_commerce).
- **social_fabric/** Statuses, guilds, duties, access days. Enforcement (→ governance/legal_policy).

## Leaves lifecycle
- New era leaf sets `derived_from` to prior leaf in same pillar.
- Superseded leaf gets `status: Retired` and `links.moved_to` pointing to the successor.
- Keep only the newest leaf active; avoid new inbound links to retired leaves.
- Max three leaves per pillar, e.g.: `_c300_700.md`, `_c700_1200.md`, `_c1200_1500.md`.

## Filenames and headers
- Front matter keys: `id`, `name`, `status`, `updated`, `era`, `primer_rev`, `links`, `tags`.
- Keep `Primer` ≤120 words; tags lowercase and concise.

## Linking discipline (LRR)
- Allowed: prev/next within same pillar; same-era snapshots; constants hubs; immediate parent overview if present.
- Disallowed: deep-links to headers; cross-era jumps without `comparative: true`.
- Maintain BacklinkGuard on targets that accept backlinks.

## Orientation
- Law vs policy: adjudication lives in **legal_policy**; circulars/enforcement in **state_policy**.
- Warfare sits under **governance/warfare**; land/naval/doctrine are sections within leaves.
- `supply_system` stays economic; depot hardware lives in **broad_infrastructure**.
- Shipbuilding and navigation are together under **technology/shipbuilding_and_navigation**; combat stays in **governance/warfare**.
- Political maps and city plans live in **snapshots** by era.
- Physical regions live in **constants** as locators, not polities.
  
## Minimal template (active leaf)
```markdown
---
id: <SYSTEM:BRANCH-ERA>
name: <Title> (c.YYYY–YYYY AO)
status: Draft
updated: YYYY-MM-DD
era: YYYY–YYYY
primer_rev: 1
links:
  prev: canon/systems_diachronic/<family>/<pillar>/<pillar>_cPPPP_QQQQ.md
  next: canon/systems_diachronic/<family>/<pillar>/<pillar>_cRRRR_SSSS.md
tags: [<lowercase, concise>]
---
# <Title> (c.YYYY–YYYY AO)

## Primer
<≤120 words>

## Thesis
<One paragraph>

## Standards / Forms
- <bullets>

## Interfaces
- <bullets>

## Failure Modes
- <bullets>
```
