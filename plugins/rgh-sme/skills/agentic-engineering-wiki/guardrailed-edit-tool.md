---
type: concept
title: Guardrailed Edit Tool
description: >
  Apply multi-line edits only when lint or syntax checks pass; on failure
  revert and show error type, proposed snippet, and original content.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 16–30"
---

A guardrailed edit tool replaces a line range in the open file in one action,
grounded in [stateful file viewer](stateful-file-viewer.md) numbers, then runs
a focused linter or syntax check before committing. Clean check → keep the edit
and redisplay the viewer centered on the change. Failure → **revert**, and
return a three-part observation: error types, how the edit would have looked,
and the original content. Ablations show each part matters: missing error type
causes misdiagnosis; missing proposed snippet encourages identical retries;
missing original content leaves the model attending to stale transcript text.

Instruct the agent not to re-issue the identical failed edit
([failure-derived prompt tips](failure-derived-prompt-tips.md)). Guardrails cut
common [argument hallucination](argument-hallucination.md) and indentation
errors but can force edit orderings when the viewer window cannot show a whole
function — weigh that under [agent-computer interface](agent-computer-interface.md)
design and [agent system-level defenses](agent-system-level-defenses.md). On
SWE-bench Lite, removing lint-before-commit costs ~3 absolute resolve points;
removing the dedicated edit action entirely costs ~7.7 — see
[ACI component ablation](aci-component-ablation.md). Edit recovery still
degrades as consecutive failures accumulate
([compound mistake amplification](compound-mistake-amplification.md)). Cap
identical retries in tips and break edit thrash after a few lint failures so
the agent re-localizes instead. A clean lint pass does not imply a minimal
fix — steer toward
[idiomatic minimal patch preference](idiomatic-minimal-patch-preference.md)
after the edit applies. Prefer **existing library helpers**
(`to_native_string`) over inventing a local `bytes.decode` branch that still
calls the wrong converter — reproduction scripts can go green while the gold
idiom remains unused.
