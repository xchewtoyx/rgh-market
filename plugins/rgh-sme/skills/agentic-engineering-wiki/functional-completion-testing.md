---
type: concept
title: Functional Completion Testing
description: >
  When gold answers are absent, score whether the completion works —
  parseable, valid tool calls, or passing existing unit tests.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 10"
---

Functional completion testing asks whether the output is *usable*, not whether
it matches a gold string: parse success, calls only tools that actually exist
in the [tool inventory](tool-inventory.md) with typed arguments, or — for code
— whether the project's own unit tests still pass against the suggested body
(Copilot-style). Usually too weak alone, but powerful when the domain ships
executable oracles.

The strongest version exploits a domain that ships its own executable
verification: code is the canonical case, since a repository often carries its
own unit test suite. A code-completion evaluation framework can simulate
reimplementing a function pulled from an open-source repository, then check
whether that repository's *own* unit tests still pass against the suggested
code — a much stronger signal than the weaker fallback of just checking linter
agreement. Not every domain permits this kind of programmatic functional
test; where one is available, it is one of the cheapest, most objective
offline eval signals to build, and it's the same functional-check family
described more generally in
[offline evaluation proxies](offline-evaluation-proxies.md). Code is also
where this generalizes most fully to full agent evaluation, not just single
completions — see [coding agent eval design](coding-agent-eval-design.md).

Use it to grow beyond [offline example suites](offline-example-suites.md)
eyeballing when labels are scarce. Combine with
[gold-standard matching](gold-standard-matching.md) on partial critical fields
when some labels exist, and with [SOMA LLM assessment](soma-llm-assessment.md)
for free-form quality that neither match nor tests can capture.
