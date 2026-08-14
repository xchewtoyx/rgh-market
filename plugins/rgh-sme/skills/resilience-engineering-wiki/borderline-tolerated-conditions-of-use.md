---
type: concept
title: Borderline Tolerated Conditions of Use
description: >
  A deliberate, acknowledged operating regime that keeps a system running
  outside its formally updated rules because full compliance is economically
  or physically infeasible — distinct from normalisation of deviance because
  the gap is named and managed rather than eroding unnoticed.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 16"
---

**Borderline Tolerated Conditions of Use (BTCUs)** (Polet et al., 2003) name
an operating regime where a system continues running under conditions that
fall outside its current, formally updated rulebook — not through drift or
concealment, but through an acknowledged, managed decision that full
compliance is infeasible and the gap will be tolerated deliberately.

Concorde is the canonical case. Designed and certified in the late 1960s,
the aircraft could not undergo the costly retrofits that later civil-
aviation rule changes (speed limits below FL100, revised baggage-weight
limits) would have required across its small fleet. Adopting every updated
rule as written would have grounded the aircraft entirely, or made
transatlantic service fuel-infeasible. Operators instead ran Concorde under
BTCUs for decades — including two years after the fatal 2000 Paris crash —
prioritising the aircraft's continued operational and symbolic viability
over adopting the theoretical safety maximum the updated rules specified.

**Why this is a distinct concept from [normalisation of
deviance](normalization-of-deviance.md), despite both describing a gap
between formal rule and actual practice**: normalisation of deviance is an
*emergent, unacknowledged* ratchet — each step is locally rationalised and
the group does not experience itself as deviating at all. A BTCU is instead
*named and owned*: the organisation (and often the regulator) knows exactly
which rule is not being met, why, and under what bounded conditions the
tolerance holds. This makes a BTCU closer to a formal risk-acceptance
decision than a drift artefact — but the underlying mechanism it rests on is
the same one [Amalberti's continuum](amalberti-safety-continuum.md)
describes: a system finds a stable, deliberately negotiated equilibrium
between formal safety maximum and continued operational and economic
viability, and defends that equilibrium rather than either fully complying
or silently eroding.

The risk a BTCU carries is not that it exists, but that its bounded,
acknowledged character can quietly convert into ordinary normalisation of
deviance if nobody keeps re-examining whether the original conditions that
justified it still hold — an acknowledged exception that is never revisited
functions exactly like an unacknowledged one once enough time has passed.
