---
type: concept
title: Codebase Retrieval for Agents
description: >
  When issue text is tiny and repos are huge, BM25 file retrieval underperforms
  interactive localization — and stuffing more retrieved tokens often hurts.
sources:
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 1–15 (§3–4)"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 31–45"
---

Repository-scale issue resolution cannot dump the whole codebase into context
(average hundreds of thousands of lines vs ~200-word issues). Two harness
patterns:

1. **One-shot retrieval → generate patch** — select files (sparse **BM25** is
   typical; dense retrieval struggles with long code keys / NL queries), pack
   instructions + issue + files + example patch, ask for a diff.
2. **Interactive localization** under an
   [agent-computer interface](agent-computer-interface.md) —
   [issue-grounded localization](issue-grounded-localization.md) with search /
   open / edit loops.

Empirically (SWE-bench): models often do **best on the shortest** BM25 context
budget among those tried (13k > 27k > 50k for several baselines) — more
retrieved tokens are not free under [lost in the middle](lost-in-the-middle.md).
At ~27k tokens BM25 still misses *all* oracle files on nearly half of
instances while only ~40% get a full oracle superset. “Oracle” retrieval
(gold-edited files) is an analysis upper bound, not a realistic prior.
Interactive agents improve file localization F1 versus BM25+frontier models
(~59% vs ~45% in SWE-agent comparisons) — prefer ACI search over stuffing
larger BM25 packs when building SE agents. Coverability also depends on max
tokens and tokenizer length inflation across models under
[LLM model selection criteria](llm-model-selection-criteria.md).

**Distraction survives correct file selection.** Even under oracle retrieval
(the right files, guaranteed), collapsing code inside those files that the
gold patch never touches (keeping only a small buffer around edited regions)
lifts resolve rate substantially over showing the oracle files whole
(SWE-bench: Claude 3 Opus 9.39% vs 4.8%; Claude 2 5.93% vs ~1.96%; roughly
doubling in both cases). Correct-file localization and
in-file-region localization are two separable bottlenecks — an ACI or
one-shot prompt that nails file selection can still bury the actual edit site
in irrelevant same-file code. Prefer a
[stateful file viewer](stateful-file-viewer.md)'s windowed view (or an
equivalent collapse-to-relevant-region step in a one-shot pipeline) over
pasting whole retrieved files even once you trust the retrieval.

**Prefer patch/diff output over whole-file regeneration.** For one-shot
generate-a-fix prompting, asking the model to emit a patch (unified diff)
consistently outperforms asking it to regenerate the entire modified file —
despite patch format being comparatively rare in training data (SWE-bench,
Claude 2 under oracle: 4.8% resolved generating patches vs 2.2% regenerating
whole files; the gap widens on shorter instances). Output-format choice is
part of [tool definition design](tool-definition-design.md) even outside an
interactive ACI: a localized-edit representation is easier for the model to
produce correctly than reproducing everything it read verbatim plus a small
change, which invites transcription drift across the untouched majority of
the file.
