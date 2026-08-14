---
type: concept
title: Genotype vs Phenotype in Incident Categorization
description: >
  Incident classification schemes routinely conflate surface manifestations
  of an event with the underlying causal patterns that produced it, which
  corrupts both signal detection and trend analysis.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 12"
---

Hollnagel's genotype/phenotype distinction (1993a), applied to safety-event
taxonomies: a **phenotype** is how an event outwardly presented — the
surface manifestation an observer would name it by (an airprox, a runway
excursion, a dropped part). A **genotype** is the underlying causal pattern
that produced it — the class of systemic condition (a communication
breakdown, a [normalised](normalization-of-deviance.md) procedural
shortcut, a [goal conflict](goal-conflicts-and-production-pressure.md)
resolved the same way repeatedly) that could, in principle, generate many
different phenotypes.

The practical failure this distinction exposes: airline risk-categorisation
matrices routinely mix the two levels in the same list, filing "human
factors" (a genotype — a causal pattern) alongside "airprox" (a
phenotype — a surface event type) as if they were peers in one taxonomy.
This corrupts analysis in both directions:

- **It hides recurring genotypes.** The same underlying causal pattern
  produces different phenotypes on different occasions, so counting by
  phenotype alone (as most incident databases do) scatters a single
  systemic problem across many superficially unrelated categories,
  understating how often it actually recurs.
- **It produces false signal on phenotype counts.** A stable or falling
  count of one phenotype looks reassuring even while its causal genotype is
  actively worsening and about to manifest through a different, uncounted
  phenotype instead — a variant of why [aggregate counts mislead as safety
  indicators](why-error-counting-misleads.md).

The fix is not a bigger taxonomy but a structurally separated one:
categorise by genotype and phenotype as two independent axes, so that a
search for "how many events did this genotype produce" and a search for
"which genotypes produced this phenotype" are both directly answerable,
rather than requiring the analyst to already know the answer before
querying the data. This is a more granular, categorisation-level version of
the same discipline behind [separating explanatory factors from change
factors](explanatory-vs-change-factors.md): both insist that a single flat
list of "causes" hides distinctions the analysis actually depends on.
