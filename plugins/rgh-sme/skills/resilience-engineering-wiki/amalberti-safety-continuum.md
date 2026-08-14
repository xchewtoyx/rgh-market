---
type: concept
title: Amalberti's Safety Continuum and the Ultra-Safe Plateau
description: >
  What makes systems safe changes with how safe they already are — and
  beyond about one failure in a million, more rules add nothing, while
  practical drift becomes the dominant residual risk.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 7"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 16"
---

Amalberti's continuum orders systems by achieved safety level and shows that
the effective safety mechanism — and the dominant vulnerability — changes as
a system gets safer:

| System level | Rate | Core safety mechanism | Primary vulnerability |
| :-- | :-- | :-- | :-- |
| Unsafe (10⁻¹–10⁻³) | e.g. organ transplant | individual practitioner competence | high inherent risk trade-offs |
| Safer (10⁻⁴) | e.g. road traffic | work standardisation, quality control | compliance breakdowns |
| Safe (10⁻⁵) | e.g. charter flying | top-management commitment, soft skills | unaddressed incident precursors |
| Ultra-safe (≤10⁻⁶) | e.g. airline flying | resilience; monitoring normal work | practical drift at the thin edge of the wedge |

The strategic lesson: interventions must match the level. Standardisation
genuinely moves a 10⁻³ system; it does nothing at 10⁻⁶. Ultra-safe systems
sit on a **plateau** where adding rules and compliance directives yields
zero progress — EU aviation issues 200+ new rules a year while safety stays
flat at 10⁻⁶ — accumulating [safety clutter](safety-clutter.md) instead. The
residual risk is [practical drift](procedural-drift.md) in normal work,
which rules cannot reach and incident reports do not surface ([Wald's
bomber paradox](walds-bomber-paradox.md)).

**Why safety levels differ so much across activities is not ignorance.**
The observed spread is vast — audacious medical grafts sit above 10⁻¹ fatal
adverse events, general surgery and aeronautical leisure activities around
10⁻³, business aviation near 10⁻⁴, chartered flights near 10⁻⁵, and
commercial scheduled flying, blood transfusion, and obstetric anaesthesia
at or below 10⁻⁶ — despite every domain having access to the same
off-the-shelf safety tools (audits, reporting systems, mandatory rules,
corporate safety cultures). Amalberti's resilience-balance thesis reframes
the spread: differences in safety level are not a shortage of tools or
knowledge, but an ecologically stable balance point where a system trades
off business viability and performance capacity against tolerated risk.
Rankings across domains stay remarkably stable for decades, with every
domain improving in parallel at roughly one order of magnitude per twenty
years — systems level off at their equilibrium point and only resume
improving under an external threat to that equilibrium (the US patient-
safety push, for instance, was driven by a medical-malpractice insurance
crisis, not a spontaneous safety initiative). Which archetype of system
resilience a given activity is settled into, and what tool that archetype
actually responds to, is set out in [the four archetypes of system
resilience](four-archetypes-of-system-resilience.md); how a system moves
between archetypes over its lifespan is [the master-coupling-paradigm life
cycle](master-coupling-paradigm-life-cycle.md).

Two attention traps at the plateau:

- **Decoy phenomena** (Turner, 1978): hyper-fixation on high-profile, narrow
  risk categories draws resources away from unmonitored systemic failure
  paths — an airline industry fixated on high-altitude stall incidents while
  an aircraft crashed over poor runway lighting and chart errors.
- Reading the plateau as "we've arrived" — the overconfidence that
  [chronic unease](chronic-unease.md) and the [armor
  strategies](armor-strategies-against-drift.md) exist to counter.
