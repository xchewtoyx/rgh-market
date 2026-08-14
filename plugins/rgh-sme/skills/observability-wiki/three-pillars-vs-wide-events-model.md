---
type: concept
title: Three Pillars vs. Wide-Event Telemetry Model
description: Metrics/logs/traces stored in three separate silos is a cheap, well-understood model best suited to infrastructure and third-party code with a small number of known failure states; a single arbitrarily-wide structured event per unit of work, stored once and aggregated at query time, better suits code you own and want to debug novel failures in.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 1"
---

Two competing models for organizing telemetry:

- **Three pillars** — metrics, logs, and traces, each collected and stored in its own silo/system. Cheap and well-suited to infrastructure and third-party code you don't control, where the space of failure modes is small and largely known in advance. This is the traditional monitoring/APM model.
- **Unified / wide-event model** — one arbitrarily wide structured event (or trace) per unit of work, stored once in a columnar store, and aggregated at query time rather than at write time. Right for code you own, because the relationships between fields survive into the store and can be queried in combinations nobody predicted in advance.

Key principles behind the wide-event model: a dataset's value compounds combinatorially with the [dimensions](dimensionality.md) and [cardinality](cardinality.md) it preserves; pre-aggregation is a one-way, irreversible trip (see [pre-aggregation is irreversible](pre-aggregation-is-irreversible.md)); you don't know in advance what you'll need to ask later, so raw data should be preserved rather than summarized away; static dashboards have limited investigative value compared to an explorable interface; and fast (seconds, not minutes) feedback loops from query to answer are essential for the model to be usable in practice.

The choice isn't purely ideological — three-pillar tooling remains a reasonable default for infrastructure you don't own or can't change, while the wide-event model earns its cost specifically where you need to answer [unknown-unknown](known-unknowns-vs-unknown-unknowns.md) questions about your own systems. See [structured events as the observability substrate](structured-events-as-observability-substrate.md) for how metrics, logs, and traces can all be derived from the same underlying wide-event stream rather than collected as genuinely separate signal types.
