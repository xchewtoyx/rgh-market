---
type: concept
title: Stateful File Viewer
description: >
  Give the agent a windowed, line-numbered view of the open file with goto and
  scroll commands instead of flooding context with full-file dumps.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 1–15 (§5); pp. 16–30"
---

A stateful file viewer keeps an open path and shows a fixed window (for example
100 lines) with prepended line numbers and indicators of content above/below.
Commands such as `open`, `goto`, `scroll_down`, and `scroll_up` mutate that
state; subsequent [guardrailed edits](guardrailed-edit-tool.md) reference the
same line numbers. Window size is a measured knob: ~100 lines beat both ~30
lines (~−3.7 pts) and dumping the entire file (~−5.3 pts) on SWE-bench Lite
under [ACI component ablation](aci-component-ablation.md).

Shell-only inspection fails this job: `cat` floods context; `head`/`tail` are
poor navigators; bash is stateless so “scrolling” regenerates long commands;
interactive pagers map poorly to one-shot LM actions. Grounding edit and search
in viewer output is a core [agent-computer interface](agent-computer-interface.md)
pattern — complementary action/observation pairs under
[context engineering](context-engineering.md). Prefer `search_file` / `goto`
over linear hunting; [blind scroll loops](blind-scroll-loop.md) are a common
regression once the agent abandons search inside multi-thousand-line files.
