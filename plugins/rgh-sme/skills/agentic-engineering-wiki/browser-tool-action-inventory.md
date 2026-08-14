---
type: concept
title: Browser Tool Action Inventory
description: >
  Give browsing agents a small closed command set — search, click-by-ID, find,
  quote, scroll, back, end — instead of free-form browser scripting.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), §2 Table 1"
---

WebGPT’s ACI exposes a fixed command vocabulary: `Search`, `Clicked on link
<link ID>`, `Find in page`, `Quote`, scroll up/down by N, `Top`, `Back`, and
`End: Answer` / `End: Nonsense|Controversial`. Observations use
[lm-oriented web observations](lm-oriented-web-observations.md) with stable
link IDs so click targets are parseable. Prefer a modern search API so the LM
practices **using a search engine**, not reimplementing retrieval indices
([retrieval-augmented generation](retrieval-augmented-generation.md) remains
the alternative when you own the corpus).

Keep the inventory small under [ACI design principles](aci-design-principles.md)
and [tool inventory](tool-inventory.md). Treat non-matching generations as
[invalid actions that still spend budget](invalid-action-budget-accounting.md).
Episode shape often splits into
[browse-then-answer phases](browse-then-answer-episode.md).
