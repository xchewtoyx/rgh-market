---
type: concept
title: Comments Belong in the Code, Not the Commit Log
description: >
  Explaining why a change was made only in a commit message leaves the code
  itself undocumented, and a future developer needing that context is
  unlikely to think to search version-control history for it.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 16"
---

A specific anti-pattern: putting the real explanation of *why* a change was
made only in the commit message, and leaving the code itself undocumented.
This fails on retrieval — a future developer needing that context is
unlikely to think to go scan repository history for it, and even if they do,
finding the relevant message in the log is tedious.

Self-check before writing a commit message: will developers plausibly need
this information again in the future? If yes, it belongs in the code itself,
not only the commit log. A concrete failure mode this prevents: a commit
fixing a subtle bug, documented only in the commit message, risks being
silently reverted later by someone who doesn't realize they're recreating the
original bug, because nothing in the code itself flagged why that logic
existed. A commit message can still duplicate the explanation for
convenience, but the code copy is the one that matters — the underlying
principle is the same one behind
[keeping comments near the code](keeping-comments-current.md): put
documentation where developers will actually see it, and the commit log
rarely qualifies.
