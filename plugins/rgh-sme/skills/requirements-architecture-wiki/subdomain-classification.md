---
type: concept
title: Subdomain Classification (Core, Supporting, Generic)
description: >
  Classifying a subdomain as core, supporting, or generic determines how
  much design and documentation investment it deserves, before any
  bounded context or build-vs-buy decision gets made for it.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies (Susanne Kaiser), ch. 2"
---

Not every part of a business domain deserves the same design and
documentation effort. Splitting the domain into subdomains and classifying
each one before deciding how to build it prevents both over-investing in
parts that don't matter competitively and under-investing in the parts
that do:

- **Core** — the business-critical part that provides the organization's
  competitive advantage: complex, changes often, and is the reason the
  organization exists in its current form. Warrants the deepest design
  investment, the most careful [bounded context](bounded-context.md)
  boundaries, and building in-house even where market-equivalent
  components have commoditized — a cloud provider does not outsource its
  own infrastructure just because "cloud" has become a commodity category
  elsewhere, because that infrastructure is its own core domain.
- **Supporting** — helps the core function but provides no competitive
  advantage on its own; simpler and more stable than core, and often
  present in competitors' products too. Justifies custom building only
  when genuine specialization is needed, and investment should stay low
  even then.
- **Generic** — ubiquitous across many businesses (authentication, payment
  processing), not differentiating, but necessary. The default is buy,
  use an open-source solution, or outsource to a utility supplier, freeing
  design and documentation effort for the core.

The classification is a heuristic, not a permanent label — a subdomain
that starts core can commoditize over time as the market catches up, and
the classification should be revisited rather than assumed to be fixed at
initial [architecture documentation](architecture-documentation-package.md)
time. It's also possible, and common, to split a decision along it rather
than force a binary build-or-buy choice: use an off-the-shelf product for
its intended use cases and custom-build only the specific gap that makes a
subdomain non-generic for this organization, rather than either fully
adopting or fully rejecting the off-the-shelf option.

This classification is what should drive where a
[trade-off write-up](documenting-trade-offs.md) or an [architecturally
significant decision](architecturally-significant-decision.md) record gets
written in the first place: a build-vs-buy choice about a generic
subdomain rarely rises to that level, while the same choice about a core
subdomain almost always does.
