---
type: concept
title: Roadmap Confidence Gradient
description: >
  A roadmap should state decreasing confidence the further out a release
  is, rather than presenting every future release with the same apparent
  certainty as the next one.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 13"
---

A roadmap listing several future releases with features assigned to each
implicitly claims equal confidence in all of them, which is rarely true
and rarely intended. The honest documentation practice is an explicit
confidence gradient: the next release should be presented as a
high-confidence plan of intent; the release after that is usually still
reasonably well defined, if partly by default (whatever didn't make the
next release tends to land there); anything beyond that is a
deliberately loose, low-confidence forecast rather than a commitment.

The same gradient shows up one level down, within a single upcoming
release, in the form of **release objectives**: brief, business-terms
summaries of the specific features a release intends to deliver. Not
every objective traces directly to a single feature — some aggregate
several related features into one summary, some are milestones with no
direct user value of their own (a trade-show demo date, an
infrastructure or [architectural runway](architectural-runway.md) item),
and some exist specifically to record what the release will *not*
accomplish — an explicit exclusion is as much a documented commitment as
an inclusion, and omitting it silently invites the assumption that
anything not ruled out is still in scope.

Within that release-objectives list, rather than presenting one
undifferentiated scope list, committed work is documented separately from
**stretch goals** — items
included in the plan but explicitly flagged as scope that may be cut if
capacity runs short, each still carrying its own [prioritization
value score](requirements-prioritization.md) so a stretch item's relative
importance stays visible even though it isn't guaranteed. This keeps the
document honest about which commitments stakeholders can rely on versus
which represent upside if things go well, at the release-scope grain
rather than only at the multi-release roadmap grain above.

The corresponding authoring discipline is to keep far-future roadmap
entries abstract enough that their *intent* can still be honored even as
circumstances change, rather than fixing them in the same level of detail
as the near-term releases. Committing far-out scope in that level of
detail quietly reintroduces a fixed scope/time/resources planning model
for exactly the part of the roadmap where the least is actually known, and
it removes the ability to respond to new information or new market
opportunity in the meantime — a tension with [good-enough
requirements](good-enough-requirements.md)'s general caution against
manufacturing false precision, applied here to the specific case of
commitments to future work rather than to a single requirement's current
detail.
