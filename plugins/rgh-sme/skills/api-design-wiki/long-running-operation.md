---
type: concept
title: Long-Running Operation
description: >
  A persisted server resource that represents async work started by another
  method, returning immediately while the client polls or waits for completion.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 10"
---

When work is slow, resource-intensive, or depends on external systems, a
synchronous response breaks down: clients cannot distinguish slow from hung,
cannot see progress, and killing the local process does not stop server work.

A **long-running operation (LRO)** adapts language-level promises to HTTP APIs:
start work, return a placeholder immediately, resolve later to success or error.
Unlike in-process futures, LROs are a **return type** for existing methods (for
example create returns `Operation<ChatRoom, CreateChatRoomMetadata>` instead of
`ChatRoom`), are **persisted resources** with their own ids that outlive the
client, carry typed **metadata** for progress, and need discovery via
[List operations](list-operations.md).

Store operations in a **central top-level collection** (`/operations/1`), not
nested under the resource they touch — not every operation centers on one
resource, and nesting prevents querying all operations system-wide.

An API may offer both synchronous and LRO variants of the same capability where
users need blocking simplicity alongside distributed monitoring.

See [operation resource shape](operation-resource-shape.md),
[polling versus wait](operation-polling-vs-wait.md),
[cancel, pause, and resume](operation-cancel-pause-resume.md), and
[operation expiration](operation-expiration.md).
