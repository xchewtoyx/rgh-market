---
type: concept
title: Evaluative State Banding
description: >
  When flagging a measure's good/bad status, use a small number of discrete
  states (roughly 4-5 at most) rather than a continuous or finely graded
  scale, or the evaluation itself becomes hard to perceive quickly.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 2 §2.2.1.3"
---

Because dashboard data must be evaluated in a glance, it helps to explicitly
flag a measure's status as good or bad, via a dedicated visual object (e.g.,
an icon) or a visual attribute (e.g., color). This evaluation need not be
binary, but should not exceed roughly 4-5 distinct states (e.g., very bad /
bad / acceptable / good / very good) — beyond that, the bands themselves
become too complex to perceive at a glance, defeating the point of having
them.

This is the same ceiling that shows up generally for how many distinct levels
of one visual attribute people can reliably tell apart — see
[perceptual distinctness limits](perceptual-distinctness-limits.md). It's also
the rationale behind the [bullet graph](bullet-graph.md)'s background bands
(bad/satisfactory/good, capped at 5) and behind
[status icon design](status-icon-design.md)'s recommendation to limit alert
icons to at most two severity levels. When encoding these bands with color,
follow [colorblind-safe color encoding](colorblind-safe-color-encoding.md) —
vary the intensity of one hue across the bands rather than switching hues.
