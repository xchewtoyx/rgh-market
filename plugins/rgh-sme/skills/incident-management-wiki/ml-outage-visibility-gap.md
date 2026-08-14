---
type: concept
title: ML Outage Visibility Gap
description: ML quality outages are often detected by end users before monitoring, and can stay invisible in aggregate metrics when only a narrow slice of users is affected.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

ML systems are less deterministic than conventional services, which makes it
harder to write monitoring rules that catch every quality regression before a
human notices — end users, or whoever sits at the very end of the pipeline
(serving, or within an application), are frequently the first detector. This
is worse than an ordinary detection lag: a quality regression that hits 100%
of a narrow user slice can be completely invisible in aggregate dashboards,
because that slice never surfaces unless someone deliberately segments the
metric and looks at it. The affected users get consistently terrible service
the whole time while every organization-wide number looks fine.

The practical consequence for incident response is that the earliest
reliable signal for a real ML outage is often a support ticket or a user
complaint rather than a firing alert. Incident processes built around
automated detection-first assumptions need an explicit path for
user-reported quality issues to reach the same [incident severity
classification](incident-severity-classification.md) machinery that an
alert-triggered incident gets, rather than being triaged as routine support
tickets until someone happens to notice the pattern.

See also [ML outage boundary ambiguity](ml-outage-boundary-ambiguity.md) and
[ML incident organizational breadth](ml-incident-organizational-breadth.md)
for the other two ways ML outages differ from conventional ones.
