---
type: concept
title: Shift-Left Security
description: >
  Integrating security into design, coding, and the automated pipeline as
  continuous, embedded practice instead of a manual downstream gate, because a
  gatekeeping model cannot scale to high deployment tempo.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4, 6"
---

# Shift-Left Security

Corporate infosec staffing is typically wildly outnumbered by the developers
producing changes (a commonly cited ratio is roughly 1 infosec specialist to
10 infrastructure engineers to 100 developers). A traditional model that
positions infosec as a manual gate at the end of the pipeline — review
everything right before release — cannot scale against teams deploying
multiple times a day: it either becomes the pipeline's dominant bottleneck or
gets bypassed under delivery pressure. Either outcome defeats its purpose.

Shift-left security moves the same concerns earlier and automates what can be
automated:

- **Early involvement**: infosec participates in feature design, threat
  modeling, and demo reviews, not just final sign-off.
- **Pre-approved building blocks**: infosec provides ready-to-use libraries,
  containers, and build templates so secure-by-default is the path of least
  resistance for developers, rather than something bolted on afterward.
- **Automated security testing in the pipeline**: static analysis (SAST),
  dynamic analysis (DAST), dependency vulnerability scanning, and
  [continuous fuzzing](continuous-fuzzing.md) run as part of the normal CI
  test suite — this is the security instance of the
  [nonfunctional test gate](nonfunctional-test-gate.md)'s Q4 "security &
  penetration" quadrant becoming an actual automated pipeline stage rather
  than a checklist. The fastest of these checks can also run earlier still,
  surfaced directly in [code review](static-analysis-in-code-review.md)
  rather than waiting for a pipeline stage to report back.
- **Developer empowerment over manual review**: infosec's role shifts from
  personally reviewing every change to building the tools and guardrails that
  let developers build securely without waiting on a reviewer.

High performers following this model spend roughly half the time on security
remediation that low performers spend, because defects are caught while
they're cheap to fix (at commit or design time) rather than after release —
the same [bring the pain forward](bring-the-pain-forward.md) logic applied to
security specifically, and a direct reduction in
[failure demand](failure-demand.md).

The broader philosophy (sometimes called Rugged DevOps or DevSecOps) treats
security as an intrinsic property every team member owns, not an external
audit step performed on their behalf. See
[platform-inherited compliance](platform-inherited-compliance.md) for how
this scales to regulatory compliance specifically.
