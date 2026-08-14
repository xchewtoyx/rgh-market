---
type: concept
title: Risk Relabelling as a Leading Indicator
description: >
  When the language used to describe a recurring anomaly quietly shifts
  toward a less alarming category, that shift is itself worth monitoring as
  a signal, regardless of whether any specific bad outcome can be predicted
  from it.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 6"
---

Before the Columbia disaster, foam debris struck the Space Shuttle's heat
shielding on essentially every flight across over a hundred missions, even
though the original design requirement was that the external tank shed no
debris at all. Over those missions the *language* used for the anomaly
drifted: "debris events" became the more innocuous "foam loss," and the
category shifted from a flight-safety issue to a routine
maintenance/turnaround issue. That recategorisation had a concrete
procedural effect — formal review was only mandated for events classified
as an "in-flight anomaly," and a foam strike immediately preceding the fatal
one had been logged merely as an "action," generating no paper trail of
concern at all.

The methodological point is not that this specific renaming could have been
shown, in advance, to lead to this specific accident — in a genuinely
complex system it usually cannot be, and a warning based on it might not
even have been believed. The point is narrower and more actionable: language
shifts that quietly lower an anomaly's perceived risk category are worth
treating as a leading indicator *in their own right*, independent of
whether the specific downstream consequence can be forecast. Renaming is how
[normalisation of deviance](normalization-of-deviance.md) becomes durable —
once "debris event" is spoken and written as "foam loss" often enough, the
new label is what future decisions get measured against, not the original
design assumption.

The practical habit this supports: when auditing a recurring anomaly, check
whether its name has changed over its history, and treat any softening as a
prompt to compare current practice against the *original* design assumption
rather than the current label — the same discipline [studying normal
work](studying-normal-work.md) and [chronic unease](chronic-unease.md)
already prescribe for other reasons.
