---
id: SYSIDX:DIA-MAP-APPX
name: Systems Diachronic — Appendix & Examples
status: Draft
updated: 2025-08-28
audience: Internal
notes: Supplement to the core map. If conflict, core wins.
---

# Systems Diachronic — Appendix & Examples

## Expanded pillar scopes (In / Out)

### economy/industrial_capacity
**In:** fuels, power, tools, mills, kilns, glassworks, foundries, yard throughput; capacity metrics; cost curves.  
**Out:** build specs of docks/roads (→ technology/broad_infrastructure); ration decrees (→ governance/state_policy).

### economy/agriculture
**In:** crops, rotations, tithes, rents, granary rules, procurement prices.  
**Out:** city distribution (→ economy/supply_system); irrigation works (→ technology/broad_infrastructure).

### economy/insurance_steps
**In:** rate postings, claim practice, convoy membership proofs, receipts/tallies.  
**Out:** court appeals (→ governance/legal_policy).

### economy/taxation_commerce
**In:** tariffs, dues, rebates, exemptions, port fees.  
**Out:** enforcement edicts (→ governance/state_policy).

### economy/supply_system
**In:** quota classes, ration windows, convoy-as-supply tables, warehouse redemption, spoilage penalties.  
**Out:** depots/quays hardware (→ technology/broad_infrastructure); ration decrees (→ governance/state_policy).

### governance/legal_policy
**In:** codes, courts, Bench, procedures, oaths, evidence rules, remedies; religious-law interface.  
**Out:** executive circulars and inspections (→ governance/state_policy).

### governance/state_policy
**In:** circulars, procurement, inspection regimes, quarantine/public health, social policy, licensing/censorship.  
**Out:** adjudication (→ governance/legal_policy).

### governance/warfare
**In:** order-of-battle patterns, escort/convoy doctrine, blockades, prize rules, mobilization classes.  
**Out:** shipyard capacity (→ economy/industrial_capacity or technology/broad_infrastructure).

### governance/polity_order
**In:** Free Cities system, Temple-State bloc, Empire → Principality transitions; cohesion and decay mechanics.  
**Out:** region maps (→ snapshots); physical geography (→ constants).

### technology/broad_infrastructure
**In:** roads, bridges, ports, drydocks, sewers, levees, raised ways, drainage, city form/elevation logic.  
**Out:** rates/quotas (→ economy), decrees (→ governance/state_policy), combat doctrine (→ governance/warfare).

### technology/communication
**In:** beacons, flags, drums, couriers, schedules, presses, compositories.  
**Out:** censorship/licensing (→ governance/state_policy); sacred calendars (→ culture_and_religion/sect_tenets).

### technology/shipbuilding_and_navigation
**In:** civil hull types, rigs, yard cycles, repair/maintenance; charts, pilotage, currents, winds, timekeeping, day-marks, Fog-Gates, nav signals.  
**Out:** armament, tactics, prize practice (→ governance/warfare).

### culture_and_religion/sect_tenets
**In:** doctrines, rites, calendars, lineages, schisms.  
**Out:** licensing/taxation (→ governance/state_policy).

### culture_and_religion/religious_topography
**In:** shrines, routes, sites, endowments as places.  
**Out:** legal status (→ governance/religion_and_state or governance/state_policy).

### culture_and_religion/arts_letters
**In:** schools of thought, guild curricula, patronage, canons, festivals of learning.  
**Out:** presses/compository hardware (→ technology/communication).

### social_fabric/*
**In:** statuses, guilds, privileges, obligations, access days, muster classes.  
**Out:** price effects (→ economy); court enforcement (→ governance/legal_policy).

## Filenames and IDs — examples
- `canon/systems_diachronic/economy/industrial_capacity/industrial_capacity_c300_700.md`  
  `id: SYS:EC-INDCAP-300-700`
- `canon/systems_diachronic/governance/legal_policy/legal_policy_c700_1200.md`  
  `id: SYS:GOV-LAW-700-1200`
- `canon/systems_diachronic/governance/state_policy/state_policy_c1200_1500.md`  
  `id: SYS:GOV-POL-1200-1500`
- `canon/systems_diachronic/technology/shipbuilding_and_navigation/shipbuilding_and_navigation_c700_1200.md`  
  `id: SYS:TECH-SHIPNAV-700-1200`
- `canon/systems_diachronic/governance/warfare/warfare_c300_700.md`  
  `id: SYS:GOV-WAR-300-700`

## Retired leaf — header snippet
```markdown
---
id: <SYSTEM:BRANCH-ERA>
name: <Title> (c.YYYY–YYYY AO)
status: Retired
updated: YYYY-MM-DD
era: YYYY–YYYY
links:
  moved_to: canon/systems_diachronic/<family>/<pillar>/<pillar>_cRRRR_SSSS.md
---
```

## Allowed link set — examples
- Prev/Next within pillar:  
  `prev: .../industrial_capacity_c300_700.md` ↔ `next: .../industrial_capacity_c700_1200.md`
- Same-era snapshot:  
  `canon/eras/01_early_ord_300_700.md`
- Constants hub:  
  `canon/constants/region_geography/<region>.md`
- Optional parent overview (if exists):  
  `canon/systems_diachronic/economy/_overview.md`

**Disallowed:** deep-links (e.g., `file.md#header`), cross-era jumps without `comparative: true` flag in the leaf.

## Sanity checklist before merge
- Header links ≤12; header ≤350 tokens; no deep-links.
- AO dating and en dashes enforced.
- Primer ≤120 words; tags lower case.
- `derived_from` present on new leaves; `moved_to` present on retired leaves.
- Pillar boundaries respected.
- BacklinkGuard maintained on targets that accept backlinks.
- Filenames and paths in snake_case; era slice matches content.

## Boilerplate section stubs

### Thesis block
```
## Thesis
<What changed across this slice. Mechanism over narrative. One concise paragraph.>
```

### Standards / Forms block
```
## Standards / Forms
- <Instrument or record> — <1-line what/how>
- <Board or drill> — <1-line how it is executed>
```

### Interfaces block
```
## Interfaces
- <Office A> — <touchpoint>
- <Office B> — <touchpoint>
```

### Failure Modes block
```
## Failure Modes
- <Failure> — <cause/effect>
- <Dispute> — <what gets contested>
```

## Notes on snapshots and constants
- **Snapshots** carry maps and “tech level” summaries by era; link outward to diachronic leaves for mechanisms.
- **Constants** carry stable physical locators for regions/places; not political entities.
