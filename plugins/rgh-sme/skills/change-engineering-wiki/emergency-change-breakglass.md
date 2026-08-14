---
type: concept
title: Emergency Change Breakglass
description: >
  A deliberately narrow, heavily audited mechanism to bypass normal change
  gates during an active incident, traded off against the risk that the
  bypass itself is misused.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 5, ch. 14"
---

# Emergency Change Breakglass

Normal release gates — [manual approval release gates](manual-approval-release-gates.md),
[provenance-based deployment policy](provenance-based-deployment-policy.md),
[peer review as change control](peer-review-as-change-control.md) — exist to
slow a change down long enough to catch problems. During an active incident
that tradeoff can invert: the safest action (e.g. reconfiguring a frontend
to divert traffic from a failing backend) may need to land faster than the
regular pipeline allows. A breakglass mechanism is the escape valve for
exactly this case: it bypasses the normal gate on demand, rather than
requiring the gate to be weakened for everyone at all times.

A breakglass mechanism only stays safe if every use is rare and expensive to
hide: access is restricted to a small set of people or roles, every
invocation raises an alert and is logged with full context, and each use is
reviewed after the fact (not just rubber-stamped) to confirm it was
warranted and to feed back into fixing whatever gap in the normal path made
the bypass necessary. If breakglass becomes routine, it has quietly become
the actual change-approval mechanism, minus the safety properties the
regular gate was providing — that is the signal to treat it as an incident
in its own right and either raise the audit bar or fix the underlying gate
so it doesn't need bypassing.
