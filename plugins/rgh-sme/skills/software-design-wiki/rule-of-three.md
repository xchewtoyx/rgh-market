---
type: concept
title: Rule of Three
description: >
  A ballpark heuristic for when duplication has earned its removal — first
  time, just write it; second time, duplicate but wince; third time,
  refactor.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 2 (credited to Don Roberts)"
---

Credited to Don Roberts: the first time you write something, just do it. The
second time you write something similar, wince at the duplication but
duplicate anyway. The third time you write something similar, refactor —
extract the shared shape into a single place. This is a ballpark heuristic
for when [duplicated code](code-duplication-red-flag.md) has earned the cost
of extraction, not a rigid rule — the underlying judgment is still whether
the resulting shared abstraction has a clean signature and a name that makes
sense, not raw repetition count. See [deciding where to start when several
groupings are possible](deciding-where-to-start-deduplication.md) for the
mechanics once you've decided to deduplicate.
