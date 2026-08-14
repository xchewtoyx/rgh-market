---
type: concept
title: Blind Scroll Loop
description: >
  After finding a large file, repeatedly scrolling without search/goto wastes
  the episode — re-invoke search for the next symbol instead of linear hunting.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 76–90"
---

A [stateful file viewer](stateful-file-viewer.md) enables efficient location
when the agent uses **find → open → search_file → goto**. The complementary
failure mode is a **blind scroll loop**: after landing on a class (or other
anchor), the agent hunts a nested symbol (`kind`, a method, …) by issuing
`scroll_down` for dozens of turns while observations collapse to omitted
windows and the narrative forgets it already found the class.

Harness mitigations under [ACI design principles](aci-design-principles.md):

- Prompt tips / demos that prefer `search_file` / `goto` over scroll for
  symbol lookup in multi-thousand-line files.
- Detect repetitive scroll-without-search streaks and inject a system warning
  or force a search tool ([failure-derived prompt tips](failure-derived-prompt-tips.md)).
- Collapse scroll observations aggressively
  ([collapsed observations](collapsed-observations.md)) so the loop is both
  expensive *and* information-poor — make search the cheaper path.

This is an instance of
[compound mistake amplification](compound-mistake-amplification.md) inside
[agent trajectory phases](agent-trajectory-phases.md) localization: early
search success does not prevent mid-episode navigation regression. Pair with
[issue-grounded localization](issue-grounded-localization.md) so the agent
reaches the right file *before* scroll discipline matters.
