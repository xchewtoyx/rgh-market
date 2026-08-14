---
type: concept
title: Orchestrator Selection Trade-offs
description: >
  What to weigh when picking an orchestration engine, illustrated through
  Airflow's specific strengths and structural weaknesses.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 4"
---

Apache Airflow is the dominant [orchestration](orchestration-vs-scheduling.md)
engine by mindshare — started at Airbnb in 2014, an Apache project since 2019 —
and its trade-offs are a useful template for evaluating any orchestrator:

**Strengths**: highly active development, a large community (mindshare makes
hiring and troubleshooting easier), and broad
[managed-offering availability](oss-vs-managed-platform-choice.md) across
major clouds, which lowers the operational burden of running it.

**Structural weaknesses**:
- Its core components — the scheduler and backend database — are
  non-scalable bottlenecks; scaling them is not simply a matter of adding
  worker nodes.
- Its scalable executor layer still exhibits a **distributed monolith**
  pattern: every executor runs the same codebase and dependency set, so any
  task's client library has to be installed cluster-wide, which produces
  constant dependency conflicts between unrelated pipelines that happen to
  share the same Airflow deployment. Mitigations are ephemeral,
  dependency-isolated infrastructure per job (e.g., spinning up a dedicated
  Spark cluster via managed services) or containerizing individual tasks so
  each carries its own dependency set.
- It lacks native support for schema management, lineage, and cataloging —
  those need bolting on separately (see
  [pipeline metadata categories](pipeline-metadata-categories.md) and
  [data lineage](data-lineage.md)).
- DAG development and testing is difficult, which works against
  [pipelines as code](pipelines-as-code.md)'s goal of treating pipeline
  definitions like reviewable, testable software.

Newer entrants (Prefect, Dagster) exist specifically to address these
weaknesses — better DAG testability and portability from local development to
production being a common selling point. The general lesson for choosing an
orchestrator: weigh mindshare and operational maturity against the specific
structural weaknesses a pipeline's own requirements are most sensitive to
(dependency isolation, native lineage, DAG testability), rather than
defaulting to whichever tool has the most search results.
