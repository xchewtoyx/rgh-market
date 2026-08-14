---
type: concept
title: ACI Component Ablation
description: >
  Measure resolve rate with each ACI piece swapped or removed so human-UI
  instincts do not silently regress the agent harness.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 1–15 (§4–5)"
---

Treat the [agent-computer interface](agent-computer-interface.md) as a
configurable surface and **ablate** it on a fixed model and task set (SWE-agent
on SWE-bench Lite with GPT-4 Turbo is the reference). Yang et al. show large
swings from interface choices alone — default ~18% resolved versus shell-only
~11%, and RAG non-interactive ~2–4% at far lower cost but much worse success.

High-signal ablations from that study:

- **Editor:** guardrailed multi-line edit+lint (18%) ≫ edit without linting
  (15%) ≫ no dedicated edit / sed-style overwrite (10.3%).
- **Search:** summarized multi-hit output (18%) ≫ no search (15.7%) ≫
  iterative one-result-at-a-time UI (12%) — human IDE paging *hurts* agents
  that exhaustively walk every match.
- **Viewer window:** ~100 lines beats both 30 lines and full-file dumps.
- **History:** last-N collapsed observations beat keeping full history; dropping
  the demonstration costs a smaller but real slice.

Run these as [offline prompt evaluation](offline-prompt-evaluation.md) /
[per-task offline harness tests](per-task-offline-harness-tests.md) before
shipping ACI changes. Track cost per resolved instance and early-vs-late
submit curves: successful runs finish earlier and cheaper; raising
max-budget alone rarely rescues the long failing tail. These are
[episode-scale metrics](episode-scale-evaluation-vs-request-apm.md), not
sub-second per-tool APM substitutes. Tie findings back to
[ACI design principles](aci-design-principles.md) and concrete tools
([guardrailed edit](guardrailed-edit-tool.md),
[bounded search](bounded-search-observations.md),
[stateful file viewer](stateful-file-viewer.md),
[collapsed observations](collapsed-observations.md)).
