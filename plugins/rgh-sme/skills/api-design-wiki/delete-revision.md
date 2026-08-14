---
type: concept
title: Delete Revision
description: >
  A dedicated custom method that hard-deletes one revision by compound id,
  kept separate from standard delete to avoid catastrophic confusion.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 28"
---

Revisions make mistakes permanent: sensitive data removed from the current
view may still exist in old snapshots. A custom `deleteRevision` method,
keyed by resource id plus revision id, removes one historical snapshot.

Do **not** overload the standard [delete method](standard-method-contract.md)
with [compound revision identifiers](compound-revision-identifier.md). A
variable mix-up can turn "delete one revision" into "delete the entire
resource and all history." A clearly named custom method keeps the operations
distinct and safer.

**Deleting the current revision is disallowed.** Removing the newest revision
would implicitly promote the next-newest — combining delete and
[restore](restore-revision.md) in one call. Reject such requests with
`412 Precondition Failed` (or equivalent). This also avoids the edge case of
deleting the sole remaining revision.

[Soft deletion](soft-deletion.md) does not apply to revisions: always
hard-delete revision records. Even when the parent resource supports soft
delete, restoring an old snapshot may need to revive a soft-deleted parent;
revision rows must disappear outright rather than linger in a recoverable
state.
