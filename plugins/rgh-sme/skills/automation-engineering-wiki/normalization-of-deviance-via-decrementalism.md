---
type: concept
title: Normalization of Deviance via Decrementalism
description: >
  A safety-critical threshold erodes not through one bad decision but through
  many small, individually-defensible relaxations, each judged safe only
  because the previous relaxation happened to succeed — leaving the
  cumulative drift invisible to anyone reviewing changes one at a time.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 1-2, 5"
---

# Normalization of Deviance via Decrementalism

A documented aviation maintenance case shows the pattern clearly: a critical
part's required lubrication interval crept from 300 flight-hours to 2,550
over three decades, in roughly six separate, independently-approved steps —
never one large jump. Each individual extension was locally reasonable
(tied to a broader maintenance-schedule change, backed by the fact that
nothing had failed yet) and drew no special scrutiny, because the gap
between the old interval and the new one was always small relative to the
current baseline. The part involved was later implicated in a fatal
in-flight failure; investigators found it had likely gone unlubricated for
nearly twice even the final, already-stretched interval.

The mechanism generalizes beyond that one case: a safety margin does not
get removed by a single decision that visibly trades safety for something
else — it gets removed by a long sequence of small steps, each one judged
against the immediately preceding baseline rather than the original design
rationale, and each one seemingly vindicated because the system kept
working afterward. But **empirical success after a relaxation is not proof
the relaxation was safe** — it can just as easily reflect that the failure
condition wasn't triggered this time, for reasons unrelated to the margin
that was cut. Every step "So far so good" narrows the actual safety margin
a little further while the record of *apparent* safety keeps growing,
right up until a step that finally exhausts what redundancy was left.

For automation, the equivalent targets are exactly the numbers this
domain treats as [safeguards](safeguards-against-runaway-automation.md):
a rate limit, a retry budget, a canary soak time, a required approval
threshold, a governor's cap. These are exposed to the identical failure
mode — a series of separately-reasonable tickets each loosening a limit
slightly to unblock some immediate need, with no single change looking
like "we are removing the safety margin" because each one is compared only
to the value right before it, not to the reasoning that set the original
limit. Two structural properties make this specifically hard to catch in
review: the check that would flag drift (comparing today's value to the
original design rationale) is not the check anyone runs when reviewing an
individual change (comparing it to yesterday's value), and the incremental
gap is deliberately kept small enough on each occasion that it doesn't
read as remarkable — which is exactly what lets it go unquestioned.

The defense isn't refusing all relaxation of a safeguard — sometimes the
original threshold genuinely was too conservative. It's making sure a
change to a safety-critical limit is evaluated against the *original*
rationale for that limit, not just against its most recent value, and
treating a limit's origin story as something to actively preserve (the
same concern [safeguards against runaway
automation](safeguards-against-runaway-automation.md) raises about
transferring the operational knowledge behind a safety limit as engineers
rotate off — a limit nobody remembers the reason for cannot be defended
against the next small, reasonable-looking request to loosen it further).
Periodically re-justifying a safeguard's current value from first
principles, rather than only ever reviewing proposed deltas from it, is
what catches decrementalism that change-by-change review structurally
cannot.

There is also a specific trap waiting on the other side of a successful
fix: **risk homeostasis** is the tendency for a system to drift back
toward its habitual risk level even after a safety margin has been
deliberately widened, because the same underlying pressure that eroded the
margin the first time — cost, schedule, throughput — never went away. A
governor's rate limit raised after an incident, or a retry budget loosened
"just this once" to unblock a launch, is exposed to the same decrementalism
this note describes starting from a new, wider baseline; restoring a
margin without also addressing why it was worn down invites the same slow
erosion to resume from scratch.
