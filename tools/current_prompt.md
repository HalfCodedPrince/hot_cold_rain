Use repo files as ground truth.

Follow:
• 03_LLM_editing_workflow.md (process, limits)
• 03_LLM_linking_policy.md (adjacency, BacklinkGuard)
• 02_style_guide.md (naming, placement, diachronic model)

Pasted snippet is authoritative. Default STRICT unless TASK sets !BUILDER.
Consult index_pack.md and 00_master_index.md for IDs/paths.
Only propose links: entries across files; no prose in unseen files.
Headers: ≤12 links, ≤350 tokens. Enforce diachronic adjacency; constants can link to other constants; 
Diachronic leaves must, if possible, include a Primer (≤120 words), based on the previous diachronic state;
Use `derived_from` to chain leaves. Retire superseded leaves and set `links.moved_to`.
Avoid helper files (base/specs). No folder indexes. Keep task file count minimal.
Output = path + full .md block, then TermCheck / LinkCheck / ScopeCheck.
If blocked, ask ≤5 pointed questions.