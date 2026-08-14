---
type: concept
title: Safety-I vs. Safety-II
description: The paradigm shift from defining safety as the absence of negative events (Safety-I) to defining it as the presence of capacities to succeed (Safety-II).
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 5"
  - title: "Architecture for Flow"
    resource: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies (Susanne Kaiser), ch. 11"
---

Resilience engineer Erik Hollnagel formulated two contrasting paradigms of safety:

| Dimension | Safety-I (Traditional) | Safety-II (Resilience) |
| :--- | :--- | :--- |
| **Safety Definition** | Absence of negative events (Zero harm) | Presence of positive capacities to succeed |
| **Operational Focus** | Why things go wrong (Lagging incidents) | Why things normally go right (Normal work) |
| **Role of Human** | Bounded, unreliable component to constrain | Flexible source of system resilience |
| **Management Goal** | Reduce behavioral variability & enforce SOPs | Understand and support adaptive workarounds |

* **Safety-I**: Focuses on rare failures and attempts to eliminate human variability. It assumes that if people follow procedures perfectly, safety is guaranteed.
* **Safety-II**: Focuses on normal work. It recognizes that humans are a source of system resilience, adapting dynamically to succeed under goal conflicts.

Applying Safety-II requires studying normal work to bridge the gap between [work-as-imagined vs work-as-done](work-as-imagined-vs-work-as-done.md), and shifting [accident-models](accident-models.md) toward systemic interaction, viewing [human error as a symptom](human-error-as-symptom.md) of underlying design flaws.

Safety-II's emphasis on treating failure as an opportunity for inquiry rather than scapegoating aligns closely with the generative pole of the [Westrum organizational culture typology](westrum-organizational-culture-typology.md): both frame effective information flow about what's really happening as the precondition for adapting well, not just for avoiding blame.
