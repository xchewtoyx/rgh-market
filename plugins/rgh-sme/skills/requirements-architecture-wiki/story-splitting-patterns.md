---
type: concept
title: Story Splitting Patterns
description: >
  A user story too large to fit an iteration is decomposed along one of a
  small set of recurring seams — workflow steps, business-rule variation,
  data-entry method, or deferred system qualities — rather than cut
  arbitrarily in half.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 6"
---

When a [user story](user-story.md) fails the **Small** or **Estimable**
prong of [INVEST](invest-criteria-for-user-stories.md), it needs to be
split — but an arbitrary cut risks losing independent value on one or both
halves. Recurring seams to split along instead:

- **Workflow steps** — a story that bundles a multi-step user workflow
  splits into one story per discrete step, each individually shippable
  (e.g. a story to "publish pricing to customers" splits into: publish to
  one channel, then a second channel, then a third, rather than shipping
  all channels simultaneously).
- **Business rule variations** — a story that looks simple in the general
  case may hide complexity in its edge-case rules; once that complexity
  surfaces, split off each rule variation as its own story rather than
  building all variations into the first pass.
- **Data entry / interaction method** — when the complexity lives in the
  interface rather than the underlying function, ship the simplest
  interaction first (e.g. a basic chart) and split richer interaction
  modes (a comparison view, a filtered view) into follow-on stories.
- **Defer system qualities** — when the first correct implementation is
  straightforward but most of the effort is in making it fast, precise, or
  reliable, split the [non-functional](non-functional-requirement.md)
  dimension out: ship a working but unoptimized version first (e.g. a
  display that interpolates from the last known reading) and follow with a
  story that hardens it (e.g. true real-time updates).

These patterns compose — a large story often needs more than one applied
in sequence. Splitting stops being the right move when what remains isn't
a size problem but an uncertainty problem (the team doesn't know enough to
even scope the split); that case calls for a [spike](spike-story.md)
instead.
