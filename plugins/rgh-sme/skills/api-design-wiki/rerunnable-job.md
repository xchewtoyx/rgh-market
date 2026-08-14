---
type: concept
title: Rerunnable Job
description: >
  A persisted Job resource that holds method configuration separately from a
  custom run invocation, enabling scheduled execution and split configure/execute permissions.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 11"
---

On-demand [custom methods](custom-method.md) that return
[long-running operations](long-running-operation.md) force callers to resubmit full
configuration on every invocation. As parameters grow, that configuration drifts
out of source control; it also conflates **permission to run** with **permission
to choose parameters** — hard to enforce "User A may only run with these exact
settings." External cron clients add another failure domain.

A **job** splits configure and execute: create a **Job** resource holding the
configuration, then invoke a parameterless custom **`run`** method on that job
when work should happen. Scheduling reduces to calling `run` on a schedule inside
the API server instead of an external scheduler.

## Job resource shape

Turn an on-demand method's request fields into Job resource fields. Rename the
target-id field to a reference name (for example `id` → `chatRoom` on
`BackupChatRoomJob`). Assign the job its own server-chosen
[resource identifier](resource-identifier.md).

Expose standard methods on the job: get, create, update, delete, list. These
should be **synchronous** — heavy work lives in `run`. Update may be omitted when
jobs are immutable (delete and recreate avoids concurrent update-while-running).

## Run method

`run` accepts only the job id — **no execution-time parameters**; all config must
live on the Job resource. It returns an LRO with response/metadata types renamed
from the on-demand method (for example `RunBackupChatRoomJobResponse`). Some jobs
modify other resources or produce ephemeral output rather than a single backup
destination.

## Execution resources

When `run` produces no durable resource elsewhere, the LRO is the only artifact —
but [operation expiration](operation-expiration.md) is not guaranteed permanent and
varies by operation type. Retaining all Operations forever forces clients to filter
a global list to find one job's history.

An **Execution** sub-resource under the Job captures immutable results with a
**job-specific retention policy**. Calling `run` still creates an Operation for
progress; on completion the Operation resolves to the new Execution — analogous to
async create's LRO resolving to the created resource. Executions support get,
list, and optionally delete; no standard create or update (produced only by `run`).
Place executions under their Job (`.../analyzeChatRoomJobs/*/executions/*`), not
in the top-level operations collection, because the natural query is "executions
for this job."

## Trade-offs

Fine-grained authorization that inspects request parameters at call time can
replace configure/run separation but costs more implementation complexity.
Forever-retained Operations avoid Execution resources at the price of unscoped
filtering.
