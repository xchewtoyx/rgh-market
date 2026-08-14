---
type: concept
title: Workflow Topology
description: >
  A workflow's task-connectivity shape — pipeline, DAG, or cyclic graph —
  trades simplicity against flexibility independently of what each task does.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

A [workflow](workflow-build-process.md) is an interconnected set of tasks,
equivalently conceptualizable as a state machine (each task a state,
transforming input into outputs propagated downstream), a publish-subscribe
network of task nodes sending and receiving work items per subscription, or a
set of tasks fully managed by a workflow orchestrator. These framings describe
the same thing; what matters most is how the tasks are interconnected — the
topology.

- **Pipeline** — simplest: tasks connected sequentially, each task's output
  feeding at most one downstream task. Benefit: simplicity. Cost:
  inflexibility — for example, if storefront-extraction details feed a
  plug-in generator but a later email-composer task also needs them, a
  pipeline forces routing them through the plug-in generator anyway, which
  over-couples the two tasks (the email task ends up sourcing store details
  from the plug-in generator, which isn't intuitive).
- **DAG (directed acyclic graph)** — a task may send output to multiple
  downstream tasks or need input from multiple upstream tasks, but
  information flow stays one-directional (no cycles). This fixes the
  pipeline's coupling problem by letting storefront details reach both a
  concept-generation task and an email-composition task directly. DAGs are the
  workhorse of workflow automation (Airflow, Luigi model workflows this way)
  and the default for basic [AI pipeline orchestration](ai-pipeline-orchestration.md)
  because they model a wide range of practical workflows while staying easy to
  reason about: a task can run once all its upstream dependencies have
  completed.
- **Cyclic graph** — the most general arrangement, where output from a task
  can circle back to upstream tasks, forming loops — useful for repairing an
  LLM mistake via quality-control retries. See
  [cyclic workflow repair loops](cyclic-workflow-repair-loops.md) for what
  this buys and what it costs. Prefer hiding recursion *inside* a task (local
  [Reflexion](reflexion.md) / retry) rather than hoisting cycles to the
  workflow level.

Topology is a separate design axis from
[batch vs. streaming workflow processing](batch-vs-streaming-workflow-processing.md)
— a given topology can run either way. Topology and batch/stream choices sit
under [workflow build process](workflow-build-process.md) step 4 —
assembling the graph after task I/O is defined.
