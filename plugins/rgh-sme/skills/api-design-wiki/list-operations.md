---
type: concept
title: List Operations
description: >
  A standard list method with mandatory filtering so clients can rediscover
  operation ids lost after process crashes.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 10"
---

[Long-running operations](long-running-operation.md) are created implicitly as
side effects — clients can lose the returned id if the initiating process
crashes before persisting it. A standard `ListOperations` method follows normal
[list method](standard-method-contract.md) conventions but requires
**filtering**, including on metadata fields (for example not done, paused).

Operations live in the centralized `/operations/*` collection, not nested under
the resource they modify.
