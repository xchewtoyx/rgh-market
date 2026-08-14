---
type: concept
title: Define Errors Out of Existence
description: >
  The strongest technique for reducing exception-handling complexity is to
  redesign an operation's semantics so the "error" condition becomes a
  well-defined normal outcome, eliminating the exception entirely.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

Applied to [Tcl's `unset` mistake](too-many-exceptions.md): redefine its
contract from "delete this variable" (which fails if the variable is absent)
to "ensure this variable no longer exists" (which is trivially already
satisfied — and simply returns — if the variable was never there). Same
operation, no more error case left to report.

**Windows vs. Unix file deletion** is the sharper example. Windows refuses to
delete a file that's open in any process — a persistent source of frustration
where the only practical fix is finding and killing the offending process, or
rebooting. Unix instead unlinks the name from the directory immediately (the
delete call returns success right away; no new process can open it, and a new
file can reuse the name), while the underlying data persists until the last
process with it open closes it. This defines away two error conditions at
once: delete no longer fails just because the file is in use, and processes
already using the file experience zero new exceptions — they keep reading and
writing normally, unaware anything happened. An alternative of immediately
invalidating existing opens would just relocate the same error onto those
processes instead of eliminating it.

**Java's `String.substring(beginIndex, endIndex)`** throws
`IndexOutOfBoundsException` for out-of-range indices, forcing callers who just
want whatever portion of the requested range actually overlaps the string to
manually clamp both indices first — a one-line call turning into 5-10 lines.
A better contract: "returns the characters of the string (if any) with index
≥ beginIndex and < endIndex," well-defined for any indices, including
negative ones or `beginIndex > endIndex` (yielding an empty result). This
simultaneously simplifies the interface and *increases* functionality — it
handles more input combinations gracefully, making the method
[deeper](deep-modules.md). Python's list slicing takes exactly this
error-free approach.

This directly rebuts the objection "won't defining errors away hide real
bugs?" The error-throwing approach doesn't net-reduce bugs, because it forces
defensive boilerplate at every call site (itself bug-prone) or gets skipped
(causing surprise runtime exceptions). The best way to reduce bugs is to make
software simpler — not to add more places that can fail loudly. This
technique has limits, though: see
[limits of masking and defining away errors](limits-of-masking-errors.md).
