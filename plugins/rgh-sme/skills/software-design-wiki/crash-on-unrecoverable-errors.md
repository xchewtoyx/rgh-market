---
type: concept
title: Just Crash on Unrecoverable Errors
description: >
  For errors that are rare, hard to meaningfully handle, and not worth the
  complexity of trying, the best design is often to print diagnostics and
  abort the process — but only when the application's role makes that
  acceptable.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

Worked example: C's `malloc` returning `NULL` on allocation failure forces
*every* call site to check and react — pervasive boilerplate that's also easy
to forget, and a missed check leads to a null-pointer-dereference crash that
obscures the real cause. There's usually nothing productive an application
can do about out-of-memory anyway: any memory it could proactively free, it
should already have freed, and modern systems rarely actually exhaust memory
in practice — hitting this condition typically signals a bug rather than a
recoverable resource shortage. The recommended pattern is to wrap `malloc` in
a helper that checks the result internally and aborts with a clear message on
failure, so application code never calls raw `malloc` and never has to
individually handle the failure case. Newer languages that throw on
allocation failure instead of returning a sentinel don't really change the
calculus — a handler that itself tries to allocate memory to report the
error is likely to fail too, so crashing immediately on exhaustion is usually
more sensible than attempting recovery.

Other candidate crash-worthy conditions: I/O errors on an already-open file
(e.g. a disk hard error), failure to open a network socket, or detection of
an internal inconsistency likely indicating a bug. For most ordinary
applications these are rare enough that a hard abort with a clear message
doesn't meaningfully hurt usability.

Whether crashing is acceptable depends entirely on the application's role. A
replicated storage system must *not* abort on an I/O error — recovering lost
data via replication, even though it adds real implementation complexity, is
core to the value such a system exists to provide. This is the same
[investment mindset](strategic-vs-tactical-programming.md) trade-off in a
different guise: pay the complexity cost where the functionality actually
matters, and skip it everywhere else.
