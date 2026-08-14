---
type: concept
title: Dashboard Definition
description: >
  A dashboard is a visual display of the most important information needed to
  achieve one or more objectives, consolidated on a single screen so it can be
  monitored at a glance.
sources:
  - title: Information Dashboard Design
    resource: "Information Dashboard Design (Stephen Few), ch. 1"
---

Stephen Few's definition, which anchors what counts as a dashboard rather than
just any report or screen full of numbers: "a visual display of the most
important information needed to achieve one or more objectives; consolidated
and arranged on a single screen so the information can be monitored at a
glance."

Four points follow directly from this definition, each with design
consequences:

1. **Visual display.** Presented mostly graphically, with supporting text,
   because well-designed graphics communicate more efficiently and richly than
   text alone — but this requires actually understanding visual perception,
   not just "adding charts" (see [preattentive processing](preattentive-processing.md)
   and the [Gestalt grouping principles](gestalt-proximity.md)).
2. **Serves specific objectives.** A dashboard shows whatever mix of
   information — often cross-functional, often otherwise unrelated — is needed
   to achieve its holder's goal. It is not defined by information type,
   source, or audience seniority; any objective-holder can have one. This is
   why the correct content and grouping follow from *how the information will
   be used*, not from organizational structure — see
   [organize dashboard groups by business function, entity, or use](spatial-arrangement-by-importance-and-use.md).
3. **Fits on a single screen.** See
   [single-screen constraint](single-screen-constraint.md) for the detail and
   rationale.
4. **Monitored at a glance.** Because a glance cannot absorb full supporting
   detail, dashboard content is almost always abbreviated as summaries or
   exceptions (see [summarization and exception reporting](summarization-and-exception-reporting.md)).
   The dashboard's job is to signal what deserves attention, not to carry
   every fact needed to act on it — deeper detail should be one interaction
   away (see [dashboard as launch pad](dashboard-as-launch-pad.md)).

Two secondary attributes reinforce the definition without being part of it:
display mechanisms should be small, concise, and intuitive — whatever
communicates best in minimal space, not necessarily a literal gauge/meter/
traffic-light just because that's the "dashboard" cliché — and dashboards must
be customized to the specific person, group, or function they serve, or they
will not serve their purpose. Different roles need different design treatment;
see [dashboard role taxonomy](dashboard-role-taxonomy.md).

Few's closing framing is the one worth carrying into any design decision: "A
dashboard is a type of display, a form of presentation, not a specific type of
information or technology." Vendor gauges/meters/dials are a decorative
convention, not a requirement — real-time refresh is also not a requirement;
refresh rate should be dictated by the objective the dashboard serves (an
air-traffic display needs real time, a strategic sales dashboard can run off
last night's data).
