---
type: concept
title: Managed Safety vs Regulated Safety
description: >
  Static rule-based limits and performance-based, actively managed risk
  assessment are two different ways of achieving safety, and the shift from
  one to the other requires regulators to change what they evaluate, not
  just relax the rules.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 6"
---

**Regulated safety** enforces a fixed rule as a blanket proxy for the
underlying risk — a maximum duty-hour cap applied identically regardless of
circadian phase, workload, or individual variation. It is auditable and
predictable, but it cannot represent a hazard whose actual severity varies
by more than the rule's single threshold can capture: two duty periods of
identical length can carry very different fatigue risk depending on when
they fall and what work they contain, and a fixed cap treats them
identically anyway.

**Managed safety** replaces the fixed threshold with continuous,
operator-and-organisation-driven risk assessment evaluating each specific
operation on its own terms — a Fatigue Risk Management System (FRMS)
assessing a given roster's actual fatigue risk rather than checking it
against a duty-hour ceiling. This is not deregulation: it is a different,
more demanding regulatory object. Regulators shift from checking rule
compliance (did the roster stay under the cap) to evaluating risk-
management *competency* (does the operator's process for assessing and
responding to fatigue actually work) — several regulators (New Zealand's
CAA in 1995, Singapore Airlines' Ultra Long Range operations in 2003,
UK CAA's easyJet flight-time alleviation in 2005) approved operational
flexibility beyond what fixed rules allowed specifically once operators
could demonstrate scientific fatigue-risk management in its place.

**Managed safety is a shared responsibility in a way regulated safety is
not.** A duty-hour cap is entirely the organisation's to enforce; managed
safety for a condition like fatigue depends on inputs the organisation
cannot fully observe or control — an individual's off-duty sleep hygiene
and personal choices shape fatigue as much as scheduled work hours do,
which means the managed-safety regime only functions if both employer and
employee actively participate in it, not just the employer.

**This is a specific instance of [procedures as resources for
action](procedures-as-resources-for-action.md) at the level of an entire
regulatory paradigm**, not just individual operator judgement: where that
concept describes how a single written procedure requires skilled judgement
to apply safely, managed safety describes an entire *class* of prescriptive
rule (duty-hour limits) being replaced by a framework that requires
organisational judgement to operate at all, with the regulator's own role
changing to match.

The flexibility managed safety buys organisations is not automatically a
gain for the individuals inside it — see [the system-versus-individual
resilience trade-off](system-vs-individual-resilience-tradeoff.md) for the
open question of whether operational flexibility negotiated at the system
level costs individual-level resilience in the process of being delivered.
