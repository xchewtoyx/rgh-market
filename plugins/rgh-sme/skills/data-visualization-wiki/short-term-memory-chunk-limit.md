---
type: concept
title: Short-Term Memory Chunk Limit
description: >
  Working memory holds only about 3-9 chunks of visual information at once,
  which is the underlying reason data that scrolls out of view is effectively
  lost to the viewer.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 4 §4.1"
  - title: Storytelling with Data
    resource: "Storytelling with Data (Cole Nussbaumer Knaflic), ch. 4"
---

Perception happens in the brain, not the eyes: only a fraction of what the
eyes register becomes a focus object, only a fraction of that becomes
conscious attention, and only a fraction of attention gets stored for later
use. Three memory stages are relevant:

- **Iconic memory** — a brief, preconscious visual buffer (a fraction of a
  second) that supports [preattentive processing](preattentive-processing.md):
  near-instant recognition of certain visual attributes. Evolutionary
  pressure favored detecting environmental differences quickly (e.g., motion
  of a distant predator), which is why iconic memory is tuned to those
  attributes.
- **Short-term (working) memory** — where conscious processing happens.
  Temporary, and limited to roughly **3 to 9 chunks** of visual information
  at a time (Knaflic cites about **four** chunks as a practical working
  figure). Once full, something must move to long-term memory or be forgotten
  to make room. A "chunk" depends on how the information is designed:
  individual numbers are each their own chunk, but a well-designed graphical
  pattern (e.g., the overall shape formed by a line graph) can represent far
  more information as a single chunk — this is a core structural advantage of
  well-designed graphics over raw text or numbers.
- **Long-term memory** — durable storage built over a lifetime, important for
  pattern recognition; reachable only by first being rehearsed through
  short-term memory. Combining visual and verbal cues helps trigger recall
  from long-term verbal memory (an image can unlock associated concepts and
  experiences).

The direct design consequence: this is the actual mechanism behind the
[single-screen constraint](single-screen-constraint.md). Once something
scrolls out of view, it's gone from working memory unless it happened to be
one of the few retained chunks — and navigating back to see it again displaces
whatever was just being looked at. Designing dashboard content as few,
information-dense chunks (a well-formed graph shape) rather than many raw
numbers is what lets more get held in mind simultaneously.

A graph with many series, colors, marker shapes, and a separate legend forces
repeated legend-to-data lookups that burn those few chunks and risk losing
attention. Prefer [direct labels](direct-labeling-over-legends.md) (leveraging
[Gestalt proximity](gestalt-proximity.md)) and form larger coherent chunks so
the finite working-memory budget is not spent on decoding the encoding.
