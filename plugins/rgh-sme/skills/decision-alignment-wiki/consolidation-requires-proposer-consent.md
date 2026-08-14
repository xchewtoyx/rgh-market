---
type: concept
title: Consolidation Requires Proposer Consent
description: >
  When merging near-duplicate stakeholder contributions to make a
  large set workable, get the original proposer's agreement that
  nothing was diluted before treating the merge as final.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 19"
---

A workshop that collects many stakeholders' individual concerns
(requirements, scenarios, risks, objections) almost always needs to
consolidate near-duplicates before the set is small enough to
prioritize or act on — see
[funneling-to-decision-themes](funneling-to-decision-themes.md) for
why the reduction itself is necessary. The failure mode specific to
*live, multi-stakeholder* consolidation is different from a solo
analyst funneling a report: a facilitator merging two people's
contributions into one item can silently erase the part of either
person's concern that didn't survive the merge, and neither
contributor may notice until much later, once the surviving item is
already being acted on.

The fix is procedural: whenever two contributions are proposed as
duplicates, confirm with *each* original proposer that the merged
item still fully captures what they meant, before treating the
consolidation as settled. A proposer who says "no, mine was actually
about X, not Y" either blocks the merge or forces a more precise
merged statement that covers both — either outcome is better than a
tidy-looking list that quietly dropped one person's actual concern.

This is a stakeholder-alignment safeguard that dot-voting and similar
narrowing techniques
([dot-voting-to-narrow-options](dot-voting-to-narrow-options.md),
[weighted-category-vote](weighted-category-vote.md)) implicitly
depend on but don't themselves guarantee: those techniques assume the
list being voted on already fairly represents everyone's input, and
that assumption only holds if the consolidation step that produced
the list was checked against the people who actually raised each
point.
