---
type: concept
title: Flawed Process Models in Control-Theoretic Accidents
description: >
  Under STAMP, every controller — human or automated — acts on an internal
  model of the system's current state, and accidents occur specifically when
  that model diverges from the system's actual state without the controller
  knowing it has diverged.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 8"
---

Every controller in [STAMP's hierarchical control
structure](stamp-hierarchical-control-structure.md) — human or automated —
must maintain an internal **process model**: a working representation of
(1) the controlled process's current state, (2) the required relationships
among the variables that make it up, and (3) which state transitions are
permissible from here. The controller does not act on the system directly;
it acts on its model of the system, and every control decision is only as
good as that model.

A STAMP accident, in this framing, is specifically a case where the
controller's process model has become **inconsistent with the actual state
of the controlled process**, and nothing in the controller's information
flow revealed the divergence before it mattered:

- The **Mars Polar Lander** software interpreted normal Hall-sensor noise
  during leg deployment as ground contact, updating its process model to
  "landed" while the spacecraft was still descending — and cut the descent
  engines accordingly.
- **Public-health officials** at Walkerton held a process model that said
  water testing and reporting were functioning normally, because [the
  measuring channel that would have corrected that model had been severed
  by privatisation](stamp-hierarchical-control-structure.md) — the model was
  wrong not because anyone reasoned badly from available information, but
  because the information itself had stopped arriving.
- **Shuttle mission managers'** process model classified foam shedding as a
  routine turnaround maintenance issue rather than a flight-safety hazard —
  the same drift [risk relabelling as a leading
  indicator](risk-relabeling-as-leading-indicator.md) documents from the
  language side; here it is the same event viewed as what the label did to
  the controller's model of the risk itself.

The common shape across all three: the process model was not obviously
irrational given what the controller could see — the Mars lander's inference
followed its programmed logic correctly given the sensor noise, the health
officials followed their existing report-driven procedure correctly given
no reports arrived, the mission managers followed established category
logic correctly given the maintenance framing. Each is a further instance of
[local rationality](local-rationality-principle.md) operating at the level
of an automated or institutional controller rather than an individual human
operator — which is also why fixing a single flawed model after the fact
does not fix the general vulnerability: any controller's process model can
diverge the same way again unless the information channels that keep it
synchronised with reality are themselves made visible and monitored.
