---
type: concept
title: Change Amplification
description: >
  Change amplification is the complexity symptom where a seemingly simple
  change requires modifications in many different places.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 2"
---

The classic illustration: a banner background color hardcoded on every page of
a website means changing the color requires editing every page, versus a
single shared variable that every page references, where changing the color
means changing one line. The first design amplifies a one-idea change into
many edits; the second doesn't.

Change amplification is one of the three observable symptoms of
[complexity](complexity.md) (alongside [cognitive load](cognitive-load.md) and
[unknown unknowns](unknown-unknowns.md)), and it's caused by
[dependencies](dependencies-as-a-cause-of-complexity.md) — the more places
that assume or duplicate a piece of information or behavior, the more places
a change to that information or behavior has to touch. A central goal of good
design is to minimize the code affected by each design decision, so that
changes stay proportional to the idea being changed.
