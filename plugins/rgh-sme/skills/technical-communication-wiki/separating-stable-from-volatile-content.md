---
type: concept
title: Separating Stable from Volatile Content
description: >
  Keep durable, slow-changing orientation material — goals, vision,
  stable concepts — physically separate from fast-changing
  implementation detail, and make the volatile material depend on the
  stable material rather than the reverse.
sources:
  - title: Living Documentation
    resource: "Living Documentation (Cyrille Martraire), ch. 9"
---

Not all content needs the same maintenance discipline, because not all content changes at the same rate. Goals, vision, stable domain concepts, and durable orientation material tend to stay accurate for a long time and can justify carefully written, hand-maintained prose — the cost of writing it well is repaid many times over precisely because it doesn't need frequent revisiting. Implementation detail, procedure, and anything tied to the current state of a fast-changing system are the opposite: they need to be cheap to update, or they will silently drift out of date (see [maintaining and deprecating documentation](maintaining-and-deprecating-documentation.md)).

The practical consequence is structural: keep stable and volatile material in physically separate places rather than interleaved in the same document, organize the stable material around names and concepts that are themselves unlikely to change, and — where one piece of content needs to reference another — have the volatile material link to or depend on the stable material, not the other way around. A stable orientation document that references specific, frequently-changing implementation details embeds a maintenance burden into exactly the content that was supposed to be low-maintenance; a volatile document that links out to a stable concept doesn't have that problem, because the thing it's linking to isn't the thing that keeps changing.

It's worth treating apparent stability as a claim to test rather than an assumption to build on — content that looks evergreen because it hasn't needed a recent update can still turn out to be more coupled to current implementation than it first appears. A README is a useful test case: the parts describing what a project is for and why it exists tend to be genuinely durable, while any part describing current configuration, dependency versions, or setup steps is really volatile content that happens to share a file with the durable part, and benefits from being clearly separated or moved elsewhere rather than left to quietly go stale next to material that doesn't.
