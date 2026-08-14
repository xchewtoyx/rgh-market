---
type: concept
title: LM-Oriented Web Observations
description: >
  Convert pages and search hits into tokenizer-stable text with numbered links,
  readability extracts, and media placeholders shaped for LM agents—not browsers.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), Appendix A"
---

Browser ACIs for LMs should emit **text observations**, not raw HTML. WebGPT’s
environment: search via an API to a simplified results page; fetches cleaned
with Readability; remaining HTML → text (html2text); PDFs via a text extractor;
unsupported types return an error. Links become a stable special form such as
`【<id>†<text>†<domain>】` so the model can cite and re-click by ID without
burning fragile URL tokens. Images collapse to `[Image: <alt>]`; titles carry
page title and domain.

This is the web sibling of [bounded search observations](bounded-search-observations.md)
and [collapsed observations](collapsed-observations.md): informative, capped,
consistent columns under [ACI design principles](aci-design-principles.md).
Pair with [token-efficient quote observations](token-efficient-quote-observations.md)
when the agent must extract evidence. Filter source domains that invite answer-
copying when the task is open-book QA, and apply
[eval observation anti-leakage](eval-observation-anti-leakage.md) in benchmark
environments.
