---
type: concept
title: Measuring Documentation Quality
description: >
  Measure documentation against the user and business outcome it was
  written to serve, using a stated baseline and hypothesis, and treat
  raw pageview-style numbers with suspicion since they can mean success
  or widespread failure equally well.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 9"
---

Measure documentation against the outcome established during audience research (see [the curse of knowledge and audience research](curse-of-knowledge-and-audience-research.md)), not against traffic alone: a successful page is one that helps its target reader complete the task accurately and efficiently, with enough confidence to continue afterward. Before changing content, establish a baseline and a specific hypothesis, and choose a measure that could actually disprove that hypothesis — a measure that can only ever confirm the change was good isn't telling you anything.

Useful measurement combines several sources, none of which is sufficient alone: analytics (visits, traffic source, search terms used, search refinements, page path, time on page, exit behavior, conversion, failed or zero-result searches); support data (ticket volume, recurring themes, resolution time, escalation rate, whether self-service actually improved); product data (activation, successful integrations, feature adoption, task completion time, retention, error rates); and interviews or task-based tests, which are what actually explain the *why* behind whatever the other signals show.

**Watch for vanity metrics.** High pageviews can mean healthy discovery of useful content, or they can mean a large number of users failing repeatedly and reloading the same unhelpful page — the number alone doesn't distinguish the two. Short time-on-page can mean the reader got a fast, correct answer, or that they abandoned the page in frustration. The fix for both cases is the same: segment by audience, product version, channel, and task; compare against the established baseline; and triangulate with qualitative evidence rather than trusting any single number in isolation. A "was this helpful?" button click or a single survey response is not proof of quality on its own.

Treat this as a standing system, not a one-time audit: set a regular review cadence, share findings with product, support, and engineering (not just within the documentation team), prioritize the highest-impact gaps the data surfaces, and measure again after a change ships. The loop is: a metric raises a question, research explains it, a targeted change tests a remedy, and ongoing maintenance preserves whatever improvement the change achieved.
