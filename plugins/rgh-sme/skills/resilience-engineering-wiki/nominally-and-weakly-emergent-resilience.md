---
type: concept
title: Nominally and Weakly Emergent Resilience
description: >
  Pariès's mapping of Bedau's first two emergence classes onto organizational
  resilience — resilience computable from designed individual and collective
  traits (nominal) versus resilience arising from feedback and
  self-organisation that only the running system itself produces (weak).
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 4"
---

Pariès maps [Bedau's taxonomy of emergence](bedau-taxonomy-of-emergence.md)
directly onto organisational resilience, giving the field's usual
sharp-end/blunt-end split a rigorous emergence-theoretic grounding rather
than leaving it as a loose spatial metaphor.

**Nominally Emergent Resilience (NER)** is resilience produced by
computable combinations of individual agent traits and explicit local
couplings — resilience an organisation can design in the same way it designs
any other engineered property, because the whole is a legible function of
its designed parts:

- Sharp-end competencies: individual cognitive skill, error management,
  stress regulation, [surprise management](irony-of-resilience.md).
- Blunt-end supportive measures: deliberately designed error-tolerant
  physical and procedural environments.
- Explicit collective structures: rationally designed role definitions,
  shared procedures, cross-monitoring, communication protocols, delegated
  leadership, and traditional Safety Management Systems.

NER is the emergence class that conventional safety engineering already
knows how to build — it is exactly the kind of resilience a checklist,
procedure, or SMS can add.

**Weakly Emergent Resilience (WER)** is resilience arising from complex
feedback and feedforward loops and indirect component interactions, where
the macro-level behaviour requires running the actual system (or a full
one-to-one simulation of it) to predict — no amount of analysing the
individual components in isolation gets there. Insect swarms are the
canonical illustration: ants following nothing more than "walk randomly" and
"lay/follow a pheromone trace on finding food" generate self-organising,
auto-catalytic collective foraging with no central controller, no
agent-to-agent communication, and no individual ant holding any
representation of the group's task — a mechanism called **stigmergy**.
Human parallels include emergency crowd evacuations, [distributed
cognition](team-preconscious-knowledge.md), and mimetic social behaviour.

WER systems share several operational signatures:

- **Edge of chaos**: WER systems stabilise at [the boundary between order
  and disorder](edge-of-chaos-and-phase-transitions.md), and — distinctively
  — actually *require* residual randomness to survive: ants that
  occasionally lose the pheromone trail discover new food sources the
  colony would otherwise never find, while excessive order produces
  synchronisation crises (the epileptic-seizure analogy for over-coordinated
  neural firing).
- **Resonance-model accidents**: failures emerge from non-linear functional
  variability in separate components matching up and reinforcing each other
  (Hollnagel's Functional Resonance Analysis Method, mentioned as the
  genuinely functional alternative to [tree-based risk
  assessment](structural-limits-of-tree-based-risk-assessment.md)) —
  concurrence at the level of a formal accident model rather than a
  narrative one.
- **Sufficiency over optimisation**: WER systems deliberately maintain
  sub-optimal trade-offs (Amalberti's "sufficiency") rather than optimising
  fully, because full optimisation against the currently known environment
  consumes exactly the flexibility needed for an unexpected shift — the
  system-level instance of [the efficiency-thoroughness
  trade-off](efficiency-thoroughness-trade-off.md) and [the
  adapted-versus-adaptive trade-off](adapted-vs-adaptive-trade-off.md).
- **Highly Optimized Tolerance (HOT)**: systems that tune their internal
  variables to absorb frequent, small perturbations efficiently become,
  by the same tuning, acutely vulnerable to rare, large ones (Carlson &
  Doyle, 2002) — the WER-specific version of [the irony of
  resilience](irony-of-resilience.md).
- **Scale-free network topology**: modular hub-and-spoke structures (airline
  route networks, the web) are highly resilient against random component
  failure — most nodes are peripheral and expendable — but acutely
  vulnerable to a targeted attack on one of the few highly connected hubs, a
  vulnerability profile invisible to any metric that only counts random
  failure rates.

The practical distinction between the two classes matters for where an
intervention should be aimed: NER responds to conventional design effort
(better training, better procedures, better role definitions); WER does not,
because there is no component-level lever that produces it directly — WER
has to be cultivated by shaping the conditions the self-organising dynamic
runs under (preserving edge-of-chaos variability, avoiding over-optimisation)
rather than specified directly.
