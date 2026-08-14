---
type: concept
title: Interface Documentation
description: >
  Interface comments are the only viable place to describe an abstraction,
  and must be kept strictly separate from implementation comments — a method
  comment forced to explain implementation to be understood is itself a
  sign the module is shallow.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

Code itself is inherently too detailed and implementation-laden to convey an
[abstraction](abstraction.md) directly — if you want code that presents good
abstractions, you must document those abstractions with comments. The core
discipline is keeping interface comments (what a caller needs to know to use
something) strictly separate from implementation comments (how it works
internally); mixing them exposes implementation detail to users who
shouldn't need it. If a class or method's interface comment is *forced* to
also explain its implementation to make sense, that's a signal the module is
[shallow](shallow-modules.md) — the act of writing the comment surfaces a
design problem that might otherwise go unnoticed.

A class-level interface comment should describe overall capability, what
each instance represents, and any limitation relevant to a prospective
user's decision to use it (e.g. "single-threaded, one request at a time") —
with zero implementation detail. A method-level interface comment should
generally cover, in order:

1. A caller-perspective behavioral summary (the abstraction).
2. Precise documentation of each argument and the return value, including
   constraints and inter-argument dependencies.
3. Any **side effects** — any consequence altering future system behavior
   that isn't part of the returned result, such as mutating retrievable
   internal state or writing to the filesystem.
4. Any exceptions the method can raise.
5. Any **preconditions** the caller must satisfy before calling (e.g. a
   binary search requiring a pre-sorted list) — while the general design
   advice is to minimize preconditions in the first place (see
   [define errors out of existence](define-errors-out-of-existence.md)),
   whatever remain must be documented.

For an interface where call order matters, or that has meaningful internal
state (an object that must be initialized before use, an operation only
valid in certain states), document the required sequencing or protocol
explicitly — this is a caller-facing fact exactly as much as an argument's
type is, not an implementation detail. Concurrency and timing behavior
belongs in the same category whenever a caller's correctness depends on
it (whether a call blocks, whether it's safe to invoke from multiple
threads).

**Examples illustrate a contract; they don't replace it.** A worked example
call is valuable for making an interface's behavior concrete, but it must
stay representative of the actual documented behavior rather than
silently becoming the only place that behavior is specified — a reader who
generalizes from an example beyond what the prose contract actually
promises can end up depending on incidental details the example happened
to exhibit but the interface never committed to.

See [implementation documentation contaminating interface](implementation-documentation-contaminates-interface.md)
for the specific failure mode of interface comments that leak internals, and
[implementation comments](implementation-comments.md) for the separate
discipline of documenting the "how."
