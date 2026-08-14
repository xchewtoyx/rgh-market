---
type: concept
title: Safe Search Argument Passing
description: >
  Wrap agent search queries so strings that look like CLI flags (e.g. --notes)
  are never parsed as options by underlying grep/find tools.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 56–60"
---

ACI search helpers (`search_dir`, `search_file`) often shell out to `grep` /
`find`. Issue text and option names frequently start with `--` (e.g. searching
for how `--notes` is handled). Without a hard separator, the underlying tool
treats the query as **its own option** (`grep: unrecognized option '--notes'`),
returns “no matches,” and the agent may retry the identical failing form before
pivoting to a weaker query (`"notes"`).

Harness requirements under [tool definition design](tool-definition-design.md):

- Always pass the pattern after `--` (or equivalent) so user/agent strings
  cannot be option-parsed.
- On failure, return a **definition-relative** error that names the quoting /
  flag issue, not only “0 matches”
  ([agent tool failure modes](agent-tool-failure-modes.md)).
- [Failure-derived prompt tips](failure-derived-prompt-tips.md): if search fails
  on a `--…` literal, strip dashes or re-quote rather than repeating the same
  call.

This is distinct from
[bounded search observations](bounded-search-observations.md) (cap hit count):
here the tool never searched. Pair with
[issue-grounded localization](issue-grounded-localization.md) so agents can
still quote option names from the issue safely.
