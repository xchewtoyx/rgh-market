---
type: concept
title: System Resilience vs Individual Resilience — Competing or Converging?
description: >
  Flexibility negotiated at the system level to keep an organisation viable
  can be delivered by transferring burden onto the individuals operating
  inside it, raising an open question resilience engineering has not
  settled: whether system-level and individual-level resilience reinforce
  each other or trade off.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 6"
---

An organisation and the individuals inside it are both, separately,
candidates for "resilience" — but improving one is not guaranteed to
improve the other, and can actively come at the other's expense.

The concrete case: airlines negotiate operational flexibility (in flight
and duty-time scheduling, for instance) specifically to preserve
**system-level resilience** — the organisation's capacity to survive
economic and competitive pressure. That flexibility is real and the
organisation genuinely benefits from it. But the flexibility is often
delivered by shifting scheduling variability onto individual crew members
— less predictable rostering, more variable rest opportunity — which can
erode **individual-level resilience**: the crew member's own capacity to
absorb workload variation without cumulative harm. The system gained
adaptive capacity; the individual lost some of theirs, in the same
transaction.

**This sharpens, rather than restates, [upward and downward
resilience](upward-and-downward-resilience.md).** That concept describes
the two directions information and intent flow between organisational
levels, and treats both directions as necessary and complementary. This
concept asks a harder, still-open question sitting underneath that
framework: when the levels' *resilience itself* — not just their
information flow — is in tension, does strengthening the system level
inherently cost the individual level, or is the apparent trade-off an
artefact of *how* a given organisation chose to deliver its flexibility,
rather than an unavoidable property of flexibility itself? Resilience
engineering does not currently have a settled answer; the honest position
is to treat any claimed gain in system-level resilience as incomplete until
its effect on individual-level resilience has been checked separately,
rather than assumed to move in the same direction by default.
