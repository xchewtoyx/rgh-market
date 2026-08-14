---
type: concept
title: Initial Versus Sustained Velocity
description: >
  Deferring security and reliability buys early speed and costs far more
  later — emergent properties retrofitted under pressure introduce new
  risks, while early modest investment sustains velocity.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 4"
---

# Initial Versus Sustained Velocity

Teams — especially small ones — defer security and reliability "for
velocity" ("we'll add security after we have customers"). Distinguish
*initial* from *sustained* velocity: skipping these concerns speeds the
first releases and reliably slows you later, because they are
[emergent properties](security-reliability-intersection.md) whose
late-stage retrofit is very expensive — and invasive late changes, often
made under incident pressure, themselves introduce new security and
reliability flaws. Once live, neither property is optional: downtime loses
business; compromise is all-hands.

The internet is the canonical cautionary tale: ARPANET made survivability
and reliability explicit early design goals, while security wasn't a
consideration in a closed network of trusted institutions. IP/UDP/TCP got
no origin authentication or tamper detection; HTTP and DNS remain
inherently attackable; and retrofitting HTTPS/IPsec has taken decades —
50 years in, a substantial fraction of web traffic still isn't HTTPS.
Assumptions about who participates in your system will not survive
contact with a [changing landscape](design-for-changing-landscape.md).

The alignment argument — security/reliability goals largely *coincide*
with code health and long-term velocity:

- [Understandable systems](design-for-understandability.md) are easier to
  debug and modify without new bugs.
- [Designing for recovery](design-for-recovery.md) quantifies and controls
  rollout risk, *enabling* higher deployment rates.
- Designing for change makes accommodating new business requirements
  faster, not just new attacks.
- Mature CI/CD (robust test coverage, reliable pipeline, staggered
  rollouts/rollbacks, decoupled code and config flags) is a modest early
  investment; retrofitting test automation to a mature system is a huge
  lump of work whose tests often enshrine current buggy behavior. Agile
  velocity itself rests on this same up-front testing/CI investment.
- [Secure-by-construction frameworks](secure-by-construction-frameworks.md)
  convert security from a tax into eliminated fire drills and smooth
  reviews; larger organizations amortize the cost across projects.

With planning, security, reliability, and features can usually all be
satisfied at modest additional up-front cost — and *reduced* total
engineering effort over the system's lifetime.
