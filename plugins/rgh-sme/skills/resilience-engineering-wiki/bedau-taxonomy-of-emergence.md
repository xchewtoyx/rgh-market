---
type: concept
title: Bedau's Taxonomy of Emergence
description: >
  A three-way split of how a macro-level property relates to its
  micro-level parts — nominal (directly derivable), weak (derivable only by
  running the full system), and strong (not derivable even in principle) —
  that sharpens the general resultant-vs-emergent distinction into a
  workable taxonomy.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 4"
---

Bedau (1997, 2002) refines the general [resultant-vs-emergent
distinction](emergence.md) into three distinct classes, ordered by how
completely a macro-level property can be recovered from micro-level facts:

1. **Nominal emergence**: the macro-property is meaningless stated at the
   micro-level, but can be derived directly by assembling micro-level
   component traits — an alarm clock's mechanics, or a metal's properties
   from its atomic structure. No individual atom "is loud," but the alarm
   clock's loudness follows straightforwardly once the components are
   assembled.
2. **Weak emergence**: a micro-level explanation exists *in principle*, but
   the macroscopic behaviour cannot actually be derived without running a
   full one-to-one simulation of the system — the system is, in Kolmogorov's
   sense, its own fastest simulator, and no analytic shortcut exists.
   Cellular automata, neural networks, and insect swarms are the paradigm
   cases: nothing hidden is happening, but nothing shorter than running the
   whole thing produces the answer.
3. **Strong emergence**: the macro-property cannot be explained or predicted
   from micro-level causality even in principle, not merely for want of
   computing power. This directly challenges strict upward causation:
   Davies (2004) grounds it in physical upper bounds on information content
   and processing rate that prevent complete micro-level determinism above
   some critical complexity threshold, meaning downward organisational
   constraints are doing real causal work, not just providing a convenient
   redescription of upward causation.

This taxonomy sharpens Laplace's (1814) determinism — the claim that an
infinite intellect ("Laplace's demon") knowing all microscopic forces and
initial conditions could compute every past and future macro-state — into a
graded claim rather than an all-or-nothing one: Laplace's demon handles
nominal emergence trivially, handles weak emergence only by actually running
the simulation (which the demon, being infinite, still technically can), and
cannot handle strong emergence even with infinite computational power,
because the relevant causal structure genuinely does not live at the
micro-level alone.

Reductionism — explaining macro-system properties purely through
lower-level component interaction laws — works cleanly only for nominal
emergence: it accounts for additive physical traits (the total mass of an
alarm clock) but struggles even with an alarm clock's *functional* property
(waking someone up is not a mass-like sum of its parts' properties), and
fails outright for weakly or strongly emergent systems — living organisms,
societies, ecosystems, consciousness — where the components (atoms in a
body) individually lack the property (life) the macro-system exhibits.

Mapped onto resilience specifically, this taxonomy produces [a three-tier
taxonomy of organizational resilience](nominally-and-weakly-emergent-resilience.md)
and [strongly emergent resilience and the self-defeating
prophecy](strongly-emergent-resilience-and-self-defeating-prophecy.md) —
the practical payoff of the abstract classification above.
