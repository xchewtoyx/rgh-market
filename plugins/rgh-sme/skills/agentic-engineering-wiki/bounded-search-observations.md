---
type: concept
title: Bounded Search Observations
description: >
  Cap and normalize search-tool output so localization stays informative
  without drowning the context window in unbounded grep dumps.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 1–15 (§4–5); pp. 16–30"
---

Bounded search observations wrap directory and file search in a consistent,
capped format (SWE-agent caps at ≤50 hits). Specialized commands —
`search_dir`, `search_file`, `find_file` — beat raw `grep`/`find` for LM
agents because shell tools often emit too many results or configurable formats
that vary across machines.

Prefer **summarized** multi-hit output over **iterative** one-match-at-a-time
paging (Vim/IDE style). Ablations: summarized ~18% resolved on SWE-bench Lite
vs iterative ~12% — worse even than removing search (~15.7%) — because agents
exhaustively walk every hit and burn cost/context. If results overflow the
cap, tell the agent to refine the query rather than page.

The tradeoff: a hard cap may force another query when the hit is just outside
the limit — spend an extra LM call rather than an unreadable dump. Prefer
simpler usage patterns and stable columns so the model can use any signal in
the issue text (line numbers, stack traces, class names) without relearning
flags. Pass patterns safely when they look like CLI flags
([safe search argument passing](safe-search-argument-passing.md)). This is
[tool definition design](tool-definition-design.md) for localization inside an
[agent-computer interface](agent-computer-interface.md), and a sibling of
[collapsed observations](collapsed-observations.md) for keeping later turns
affordable. Validate with
[ACI component ablation](aci-component-ablation.md).
