---
type: concept
title: Burnout Risk Factors
description: Christina Maslach's six organizational conditions that drive burnout, and why fixing the work environment beats trying to fix the person.
sources:
  - title: "Accelerate"
    resource: "Accelerate: The Science of Lean Software and DevOps (Nicole Forsgren, Jez Humble, Gene Kim), ch. 9"
---

Christina Maslach's research identifies six organizational risk factors that drive burnout:

1. **Work overload**: demands systematically exceed human capacity.
2. **Lack of control**: inability to influence decisions, schedule, or tools governing one's own work.
3. **Insufficient reward**: inadequate financial, institutional, or social recognition.
4. **Breakdown of community**: an unsupportive, adversarial, or siloed work environment.
5. **Absence of fairness**: arbitrary decision-making or uneven workload distribution.
6. **Value conflicts**: a mismatch between an individual's professional ethics and the organization's actual lived behavior.

The common management anti-pattern is trying to "fix the person" — wellness apps, resilience seminars — while leaving the organizational conditions that produce the risk factors untouched. Maslach's research finds that changing the work environment has a far higher probability of resolving burnout than changing the individual.

For incident work specifically, several of these risk factors map directly onto on-call design choices: work overload maps to raw [pager load](pager-load-management.md), lack of control maps to unpredictable or unilaterally-changed schedules, and breakdown of community maps to the rotation dynamics discussed in [sustainable on-call design](sustainable-on-call-design.md). Deployment and release friction that spills into off-hours emergency work — "deployment pain" — is itself a work-overload driver worth eliminating at the source rather than absorbing through the rotation.
