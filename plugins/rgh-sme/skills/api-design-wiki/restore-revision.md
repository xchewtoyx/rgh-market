---
type: concept
title: Restore Revision
description: >
  A custom method that atomically creates a new revision whose data is copied
  from a specified older revision, making that copy the current representation.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 28"
---

Restoration could be done manually: get an old
[compound revision identifier](compound-revision-identifier.md), update the
resource with that data, optionally create a revision — three round-trips
each able to fail, delay, or race concurrent writers. A custom
`restoreRevision` method makes rollback atomic and convenient.

Restore **creates a new revision** copied from the chosen snapshot; it does
not move an old revision forward or rewrite its timestamp. The new record has
a fresh [revision identifier](revision-identifier.md) and the latest
`revisionCreateTime`, so it becomes current while history remains an honest
progression — like photocopying an old page and placing the copy on top of
the stack.

Restore does not alter history entries; browsing revisions still shows the
original sequence without apparent time jumps.
