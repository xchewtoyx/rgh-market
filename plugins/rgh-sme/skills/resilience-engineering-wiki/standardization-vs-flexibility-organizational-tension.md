---
type: concept
title: The Standardization-versus-Flexibility Organizational Tension
description: >
  Organisational resilience requires continuously managing five concrete
  trade-offs between standardizing tendencies (procedure, audit, routine
  automation) and flexibility tendencies (local autonomy, informal practice,
  learning) — none of which resolves once and stays resolved.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 11"
---

Resilience engineering names two opposing organisational tendencies, each
individually legitimate, that pull against each other in every organisation
operating under risk:

- **Standardization**: routinising procedures, removing variance through
  standardised selection and training (making personnel substitutable),
  supervisory and audit control, output monitoring, routine automation.
- **Flexibility**: informal and unofficial work practices, distributed
  decision-making with local autonomy, agile operational systems, enabling
  technologies, feedback and learning mechanisms.

Neither tendency is dispensable on its own — standardisation is what makes a
large organisation coordinate and audit at all, flexibility is what lets it
handle what standardisation didn't anticipate — so the organisation cannot
resolve the tension by picking a side. Concretely, this plays out as five
ongoing trade-offs an organisation is always managing simultaneously, never
finished managing:

1. Formal procedures versus local autonomy.
2. Centralisation versus decentralisation.
3. System stability versus capacity to change.
4. Standard product/service quality versus adjusting to shifting demand.
5. Tested, proven technologies versus adopting technological innovation.

This is the organisational-design-level restatement of [the adapted-versus-
adaptive trade-off](adapted-vs-adaptive-trade-off.md): a system tuned
entirely toward the standardisation end of any one of these five axes gains
predictability and efficiency against the environment as currently known, at
the direct cost of the flexibility that same axis would otherwise supply
against an environment that changes. Safety margins are not a simple
by-product of how far toward either end an organisation sits — cutting cost
by stripping out apparent redundancy ("lean" operation) does not straightforwardly
increase risk; it can also sharpen attention onto the safety-critical
processes that remain, changing the *nature* of the system's vulnerability
rather than only its magnitude. This is why auditing organisational
resilience means checking where an organisation sits on each of the five
axes separately, the same diagnostic move [Woods's eight
criteria](eight-criteria-of-organizational-resilience.md) make for a
different checklist: a system can be well-balanced on one axis and badly
skewed on another, and one aggregate "how resilient are we" score hides
exactly that.
