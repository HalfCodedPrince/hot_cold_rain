# Editing Workflow (LLM-facing) — v1.2

**Overarching directives**
- Read `index_pack.md` before edits for IDs, paths, status, aliases, and link-key sanity.
- Respect project limits: small file sets per task; do not introduce helper files unless justified.

**Scope lock**
- Each task states: `file`, `ops`, `forbid`, `mode`.
- If a referenced file is unseen, request a snippet or propose `[NEW STUB]` and stop.

**Style preflight**
- Check filename, front-matter keys, `links:` shape, tag casing, ranges.
- Inter-file references only via `links:`. No folder indexes.

**Provenance & retirement**
- Diachronic leaves:
  - `derived_from` should list the **previous leaf**.
  - Include a `Primer` (≤120 words); add `primer_rev:` if you change it across leaves.
- When retiring a leaf: set `status: Retired`, add `links.moved_to: <successor>`, and optionally move to `/retired/` after one release.

**Tooling discipline**
- For link/back-link work, query `index_pack.md` before proposing changes.
- Include a `LookupLog:` listing each file checked and FOUND/MISSING/INCONCLUSIVE.
- If INCONCLUSIVE, make no proposal in STRICT; ask ≤3 pointed questions.
- Enforce BacklinkGuard and adjacency rules.
- Validate anchors if referencing tables inside the same leaf or constants.

**Repo ground truth**
- Trust only the pasted file, `00_master_index.md`, `01_glossary.md`. Everything else is `[SPECULATIVE → CONFIRM?]`.

**Edit output format**
- For each file touched: the path on its own line, then one fenced block with the full replacement.

**Assumption register**
- List assumptions at the end. Empty is allowed.

**Validation checklist**
- `TermCheck:` new terms introduced.
- `LinkCheck:` added/changed paths.
- `ScopeCheck:` only requested areas changed.
- Header: ≤12 links and ≤300 tokens.
- File size: warn ≥12 KB; split or trim at 18 KB.

**Modes**
- `STRICT`: zero speculation; no new entities/laws/numbers; link only to existing pages. If new doctrine is required, mark `[NEW STUB]` and stop.
- `BUILDER`: allow `[NEW STUB]` proposals under **Proposals**.

**unknowns: [...]**
- Short checklist of gaps to resolve or avoid guessing.

**Missing-info rule**
- If anything blocks a clean pass, ask ≤3 pointed questions.

---

## Priority & Precedence
1) **Pasted snippet in chat** — authoritative.
2) **03_LLM_editing_workflow.md** (this file).
3) **03_LLM_linking_policy.md** (link rules and adjacency).
4) **02_style_guide.md** (naming, tone, placement).
5) **00_master_index.md** and **index_pack.md** (IDs, paths, membership).
6) **01_glossary.md** (terms allowed).
```