# Link Policy

## Goals
Reduce header bloat, prevent stale links, keep backlinks deterministic, and enforce era coherence.

## Header Budget
- Hard cap: **≤12 links** per page.  
- Soft cap: **≤300 tokens** for the entire header.  
- Drop optional links first (see Matrix).  
- Token rule-of-thumb: tokens ≈ 2 + ceil(path_chars/4) per link.

## When to Link (LRR test)
Link only if at least one applies:
1) **L**exical: the target is **named in body** (proper noun, form name, or role).  
2) **R**egulatory: the target **governs a mechanic** used in body (law, metrology, calendars).  
3) **R**eference-hub: the target is a **stable index** readers must consult.  
If none apply, do **not** link.

## Era Adjacency
- Default window: **same era** or **±100 AO years**.  
- Outside window allowed only for **index pages** or **explicit cross-era comparisons**.  
- Disallow linking to **goalpost c1800** pages from medieval pages unless a “Comparative” subsection exists.

## Matrix (what should link where)
- **fee-farms, stairs, rents** → `systems/economy/taxation_finance_c0_1200.md`, `systems/governance/procurement_fee_farms_c700_1200.md`.  
- **Access Days, harbor law, watches** → `entities/factions/harbor_watches.md`, `systems/transport/navigation_currents.md` (if lanes/tides appear).  
- **Printed lists, forms, boards** → `systems/tech/writing_and_printing_c700_1200.md`.  
- **Seals, weights, assay slips, bags** → `systems/metrology/index.md`, `systems/infrastructure/courier_circuit_assay_ring_c700_1300.md`.  
- **Works Lists, dredge, quays** → `entities/factions/dredge_and_bar_works.md`; if financing appears, also `entities/factions/public_debt_office.md`.  
- **Material specs (pozzolan, iron-sand)** → link their system pages only if **used in body**.  
- **Risk/pricing** → `entities/factions/convoy_insurance_office.md` only if **rate/Step** mechanics are active.  
- **Calendars/measures** → link the smallest stable page under `systems/metrology/*`.

## BacklinkGuard
Before proposing a backlink **TGT → SRC**:
- Check `index_pack.md`: if **TGT.links** already contains **SRC**, **do not propose**.  
- Propose only when **LRR** passes and **Era Adjacency** holds.  
- If **TGT** is absent from `index_pack.md`, mark the proposal **low-confidence**.

## Lint (automated checks)
- Paths must resolve in `index_pack.md`.  
- No duplicate link keys.  
- Warn if header >12 links or >300 tokens.  
- Flag out-of-window era links.  
- Require a one-line **Why** for each new link in PR description.

## Maintenance
- Prefer **indices** over volatile leaf pages when structure is in flux.  
- On rename/move, update headers only where **LRR** still passes; otherwise drop.

## PR Template — Link Changes
- Added: `<path>` — **Why:** `<one line>` — **LRR:** `L|R|R` — **Era ok:** `yes/no`  
- Removed: `<path>` — **Why:** `unused / out-of-window / over cap`