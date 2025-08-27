# Editing Workflow (LLM-facing)

**Overarching directives**
- Treat `index_pack.md` as required pre-read for: ID/path resolution, overview membership, status, aliases, and link-key sanity. It is in the core upload set, so reliance is safe.

**Scope lock**
- Each task starts by stating: `file`, `ops`, `forbid`, `mode`.
- If a referenced file is unseen, request a snippet or propose `[NEW STUB]` and stop there.

**Style preflight**
- Check filename, front-matter keys, `links:` shape, tag casing, and ranges per the style guide.
- Use only a `links:` block for inter-file references; do not insert inline prose about other files.  
  (See `03_linking_policy.md`.)

**Tooling discipline**
- For link/back-link work, query `index_pack.md` and any relevant domain index or page before proposing changes.
- Responses must include a short `LookupLog:` listing each file checked and the result: FOUND / MISSING / INCONCLUSIVE.
- If INCONCLUSIVE, make no proposal in STRICT mode; ask ≤3 pointed questions.
- Verify backlinks before proposing any back-link (BacklinkGuard).
- Validate anchors if you reference table anchors.
- Include the exact queries you ran in `LookupLog:`.

**Repo ground truth**
- Rely only on the pasted file, `00_master_index.md`, `01_glossary.md`. Everything else is `[SPECULATIVE → CONFIRM?]`.

**Edit output format**
- For each file touched, output the path on its own line, then one fenced block with the full replacement.

**Assumption register**
- List any assumptions at the end. Empty is allowed.

**Link discipline**
- You may propose reciprocal `links:` entries in other files. No prose edits in unseen files.  
- Do not deep-link to Drafts from Stable pages; link the parent folder. 
- Before proposing a backlink from **SRC → TGT**, check `index_pack.md`: if `TGT.links` already contains **SRC**, do not propose.
- If **TGT** is absent from `index_pack.md`, mark proposal as “low-confidence”.
- Prefer adding backlinks only when **SRC** is cited in **TGT**’s body or governs **TGT**’s mechanics.
- Output proposals as a path list only. No prose edits in **TGT**.

**Validation checklist**
- `TermCheck:` new terms introduced.  
- `LinkCheck:` added/changed paths.  
- `ScopeCheck:` only the requested areas changed.

**Modes**
- `STRICT`: zero speculation; no new terms; do not assert new entities, laws, or numbers; link only to existing pages. If a section would require new doctrine, mark it `[NEW STUB]` and stop.
- `BUILDER`: allow `[NEW STUB]` and clearly label proposals at the end under **Proposals**.

**unknowns: [...]**
- A short checklist of gaps you want to resolve or avoid guessing about (e.g., “who issues licenses,” “commission ranges,” “northern cartel tie strength”). If left empty, missing facts will not be invented in STRICT mode.

**Missing-info rule**
- If anything blocks a clean pass, stop and ask ≤3 pointed questions.

---

## Priority & Precedence

1) **Pasted snippet in chat** — authoritative for this pass.  
2) **03_LLM_editing_workflow.md** (this file).  
3) **03_linking_policy.md** (link rules and BacklinkGuard).  
4) **02_style_guide.md** (naming, tone, placement, schemas).  
5) **00_master_index.md** and **index_pack.md** (IDs, paths, membership).  
6) **01_glossary.md** (terms allowed).

When rules collide: **link rules** in `03_linking_policy.md` govern links; otherwise this workflow controls process.

---

## Task template
```yaml
# Use "!" to select the active mode
TASK
mode: !STRICT | BUILDER
file: canon/.../your_file.md
ops: [style_check, lore_check, expansions, link_backlinks]
forbid: [no_prose_in_other_files, repo_ground_truth_only]
unknowns: [...] 
