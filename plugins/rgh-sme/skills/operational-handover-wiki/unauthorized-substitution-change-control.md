---
type: concept
title: Unauthorized Substitution Change Control
description: Why a locally-reasonable substitution or deviation from an approved design must be routed back through the original design authority before being applied.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 3"
---

A substitution that looks equivalent to the person making it can silently violate an assumption that only the original designer knew about — and the person making the substitution has no way to know that, because the assumption was never written down anywhere they'd see it.

## The Canonical Failure

In the construction of a Manhattan skyscraper, the contractor substituted bolted joints for the structural engineer's originally specified welded joints on a critical bracing system, to cut costs. The substitution was made without a [cross-specialist communication schedule](cross-specialist-communication-schedule.md) consultation with the lead structural engineer. On paper the substitution looked sound — bolted joints are a standard, normally-adequate construction technique. What the substituting contractor could not have known is that the original design's wind-load calculations assumed straight-on wind loading; the engineer's original analysis had not been re-run for the case of *quartering* winds (wind hitting the building at an angle) hitting the substituted joints, a case in which the bolted joints were dramatically weaker than welded ones. The building was, unknown to almost everyone for a year, dangerously undersized for a fairly ordinary storm — a defect only discovered by chance and fixed through a covert, high-risk emergency retrofit.

## The Rule

Any deviation from an approved design or specification — even one that looks like a like-for-like substitution, and even when driven by a reasonable local motivation like cost or availability — must be routed back through the original design authority (the person or team who made the original decision and holds the assumptions behind it) for re-validation before it is applied. This applies whether the deviation is proposed by a different team, a different specialist, or a later maintainer working from the same documentation years afterward.

## Why This Matters for Handover and Maintenance

This is the sharpest version of "what's safe to touch, what's brittle": a component can look interchangeable with its original while silently depending on an assumption that never appears in the artifact itself, only in the reasoning that produced it. When handing over a system, flag the specific places where a component's design encodes an assumption that isn't obvious from inspecting the component alone (e.g. "this connector type was chosen because of X, not just because it was convenient") — otherwise a future maintainer has no way to know a swap they consider routine actually isn't.

Where the boundary can be expressed as a machine-checkable rule, back the process requirement with an [automated guardrail](automated-guardrails-for-safe-changes.md) so the check fires even for a maintainer who never read this rule.

## The Mirror Case: Documented Limits That No Longer Apply

The same hidden-assumption structure also runs in the opposite direction: a documented "do not do X" constraint (a load limit, a "this path is impassable," a hard-coded threshold) is itself the output of a past analysis made under specific conditions, and a maintainer who only sees the constraint — not the reasoning behind it — cannot tell whether those conditions still hold. An operator who understands *why* a limit was set is sometimes correctly able to recognize that the situation in front of them doesn't match the assumption the limit was protecting against, and safely deviate where a maintainer working from the bare rule alone could not (Klein, *Sources of Power*, ch. 8, describes exactly this: field experts who could recognize when a documented constraint's originating test conditions didn't match their actual situation). This is not license to casually override documented limits — it is the argument for recording the assumption behind a limit alongside the limit itself, so a future maintainer has the information needed to tell "this constraint no longer applies" from "I don't understand why this constraint exists," which look identical from the outside but call for opposite responses.

This is a single-decision failure: one deviation, evaluated once, against a hidden assumption. For the related but distinct risk of many individually-authorized small changes compounding into large, unreviewed drift over time, see [Decremental Drift in Maintenance Intervals](decremental-drift-in-maintenance-intervals.md).
