---
type: concept
title: Token-Efficient Quote Observations
description: >
  Let find/quote tools match case-insensitively and return abbreviated
  start–end spans so evidence fits the context budget without full-page dumps.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), Appendix A"
---

When a browsing agent must ground answers in page text, expose **find** and
**quote** actions whose observations are shaped for
[context engineering](context-engineering.md): case-insensitive match (quotes
also ignore whitespace), and allow abbreviated spans such as
`<start>━<end>` instead of pasting the entire intervening passage. Answering-
phase prompts then list numbered quotes with titles, domains, and extracts —
compact working memory for citation rather than another full page load.

This instantiates [ACI design principles](aci-design-principles.md) (compact
actions, concise feedback) for evidence gathering alongside
[lm-oriented web observations](lm-oriented-web-observations.md). Prefer
abbreviation over dumping whole pages when the agent already localized the
span; keep quote IDs stable so later turns can cite without re-fetching.
