---
type: concept
title: Requirement Revisit Triggers
description: >
  A documented requirement needs a named set of triggers for reopening
  it — usage, dependency, and expectation changes among them — plus a
  scheduled check-in even when nothing seems to have changed.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 14"
---

A requirement or target that was correctly specified when written can
become wrong later without anyone deciding to change it — the world around
it moved. A useful taxonomy of what should trigger revisiting a documented
target: usage changes (the system is used differently than assumed),
functional changes (the system itself changed), dependency changes (a hard
dependency's own guarantees changed, which caps what you can honestly
promise on top of it), failure-induced changes (an incident revealed the
target was wrong — the resulting discussion is often the valuable output
even when the number itself doesn't move), user-expectation changes,
tooling changes, and simple intuition that something no longer fits.

A useful diagnostic pair for spotting a mis-specified target without
waiting for a formal trigger: "always missing the target but stakeholders
are happy anyway" and "always comfortably meeting the target but
stakeholders are unhappy" are both signals that the documented number and
the actual need have come apart, in opposite directions. Because a
requirement can go stale silently, some scheduled revisit should always
exist on the calendar — even a two-minute no-change check-in — rather than
relying solely on a trigger being noticed. This matters especially because
some drift never produces a single change big enough to trip a trigger at
all — see [decrementalism in constraint
drift](decrementalism-in-constraint-drift.md) for why a scheduled revisit
against the *original* documented value is the only defense against a
requirement eroded one small, individually-reasonable step at a time. This is the enforcement
mechanism behind [stable vs. volatile
documentation](stable-vs-volatile-documentation.md)'s claim that apparent
stability should be periodically tested, not just assumed, and it's the
"next revisit date" field that recurs across the worked templates in [SLO
as documented requirement](slo-as-documented-requirement.md).
