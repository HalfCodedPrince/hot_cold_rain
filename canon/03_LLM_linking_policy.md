## Goals
Minimize headers, prevent stale links, keep backlinks deterministic, enforce era coherence.

## Header Budget
- Hard cap: **≤12 links** per page.
- Soft cap: **≤350 tokens** for the entire header.
- Drop optional links first (see Matrix).
- Token rule-of-thumb: tokens ≈ 2 + ceil(path_chars/4) per link.

## When to Link (LRR test)
Link only if at least one applies:
1) **L**exical: target is named in body.
2) **R**egulatory: target governs a mechanic used in body.
3) **R**eference-hub: target is a stable constants page or snapshot needed for context.
If none apply, do not link.

## Adjacency rules
- **Diachronic leaves**: link to **adjacent leaves** in the same family (prev/next), to **same-era snapshots**, and to **constants**. Cross-family links follow the LRR test and the general era window.
- **General era window** for cross-family links: ±100 AO unless `comparative: true` in header.
- **Snapshots**: link to same-era diachronic leaves and constants only.
- **Constants**: any page may link up to `/constants/*`; constants can only link to other constants/

## BacklinkGuard
- Before proposing **TGT → SRC**:
  - Check `index_pack.md`: if `TGT.links` already contains `SRC`, do not propose.
  - Reject non-adjacent era backlinks between diachronic leaves of the same family.
  - Ignore `status: Retired` and any path under `/retired/` as backlink targets.
- Propose only when **LRR** passes and **Adjacency** holds.
- If **TGT** is missing in `index_pack.md`, mark **low-confidence**.

## Lint
- Paths must resolve in `index_pack.md`.
- No duplicate link keys.
- Warn if header >12 links or >300 tokens.
- Flag out-of-window or non-adjacent links.
- **Retired guard**: no inbound links to `/retired/` except in `derived_from`.
- **Size**: warn at 12 KB; advise split at 18 KB.
- Primer allowed duplication; suggest `primer_rev` in front matter.

## Maintenance
- Prefer one diachronic leaf per period; avoid helper files.
- On rename/move, update headers only where LRR still passes; otherwise drop.
- Use `links.moved_to:` when retiring; remove after one release when inbound links clear.

## PR Template — Link Changes
- Added: `<path>` — **Why:** `<one line>` — **LRR:** `L|R|R` — **Adjacency ok:** `yes/no`
- Removed: `<path>` — **Why:** `unused / out-of-window / over cap`