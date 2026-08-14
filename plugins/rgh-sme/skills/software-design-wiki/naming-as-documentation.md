---
type: concept
title: Naming Is a Form of Documentation
description: >
  Good names reduce the need for other documentation and make bugs easier to
  spot; poor names actively add ambiguity and complexity, and the effect
  compounds because a system has thousands of names.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 14"
---

Naming is one of the most underrated aspects of software design. This is
another instance of [complexity accumulating incrementally](incremental-accumulation-of-complexity.md):
any single mediocre name barely matters on its own, but a system has
thousands of names, so the cumulative discipline — or lack of it — across all
of them has a real effect on overall system complexity.

A war story makes the stakes concrete: a distributed OS project had files
that occasionally and mysteriously lost data (a block silently zeroed with no
user modification), taking six months to track down, with multiple engineers
giving up on it before it was found. The root cause was a single variable
name, `block`, reused for two genuinely different concepts — a *physical*
block number on disk and a *logical* block number within a file. At one buggy
call site, a logical block number got used where a physical one was
expected, silently corrupting an unrelated disk block. Reviewers who read the
faulty code directly, including the eventual finder, never caught it, because
seeing the name `block` in a physical-block-number context triggered an
automatic, unexamined assumption that it *was* one. `block` wasn't even a bad
name in isolation — it's a reasonably close fit for both concepts — yet it
still caused a six-month bug hunt. The lesson: don't settle for merely
"reasonably close" names; the extra time spent finding precise, unambiguous
names pays for itself quickly, and the skill of finding them gets faster with
practice. See [precise names](precise-names.md) and
[consistent names](consistent-names.md) for the two properties that would
have prevented this bug.
