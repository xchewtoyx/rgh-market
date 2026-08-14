---
type: concept
title: Modeling Any Workflow as a Trace
description: Trace primitives generalize beyond user-facing HTTP requests to any DAG-shaped process — a build pipeline's workflow/job/step structure maps directly onto trace/span/child-span — and once modeled that way, finding the real bottleneck requires tracing the DAG's critical path, not just looking at individual job durations.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 18"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §7"
---

[Trace](trace-anatomy-and-spans.md) primitives aren't specific to user-facing HTTP requests — any process with a start, an end, and a set of nested or sequential sub-steps can be modeled the same way. A CI/CD pipeline, for example, maps naturally: a workflow run becomes the trace, each job becomes a span, and each step within a job becomes a child span. Once modeled this way, "team folklore about slow builds" turns into measurable, filterable, queryable data using the same [core analysis loop](core-analysis-loop.md) techniques used for any other trace.

The same reframing extends to offline, data-intensive workloads (e.g. MapReduce-style batch jobs) that have no single "request" to hang a trace id on at all — the fix is to pick a different, still-meaningful unit of work as the trace id, such as a key (or range of keys) in the input data, or a shard of the job. Tracing infrastructure originally built around online serving requests can cover batch systems too, as long as *some* stable, meaningful identifier exists to group the work under.

This reframing also surfaces a debugging trap: the jobs in a pipeline form a DAG, not a flat list, and an end-to-end duration is determined by the DAG's *critical path*, not by any individual job's duration. Optimizing a job that isn't on the critical path yields zero end-to-end improvement no matter how much faster it gets — you have to trace the DAG to find which path actually determines total duration before optimizing anything. This is a specific instance of the more general principle in [deciding whether to create a span](deciding-whether-to-create-a-span.md): a span (or job) is only worth optimizing if it's actually on the path that determines the outcome you care about. Computing the critical path also directly surfaces a specific, common optimization target once you have it: steps that run sequentially on the critical path purely because nobody parallelized them, often in shared infrastructure the investigating engineer didn't write themselves — once visible on the critical path, this class of fix tends to be easy even though finding it without a trace is not.
