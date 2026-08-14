---
type: concept
title: Implementation Documentation Contaminates Interface
description: >
  Interface documentation that describes implementation details a caller
  doesn't need is a red flag, usually caught by asking, for each candidate
  fact, whether a user of the class genuinely needs to know it.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

**Red flag: implementation documentation contaminates interface** — "occurs
when interface documentation, such as that for a method, describes
implementation details that aren't needed in order to use the thing being
documented."

A worked case study, an `IndexLookup` class (a client-side interface for
indexed range queries spread across index and object servers), shows the
diagnostic test in action. Its original class comment buried implementation
minutiae — internal RPC names, private tuning parameters — that belong
nowhere near [interface documentation](interface-documentation.md), plus
filler that stated the obvious or said nothing at all. The revised comment
kept only what a caller needs: what an instance represents and the
method-by-method usage pattern, deliberately omitting server-crash handling
because crash recovery is fully transparent to this class's callers.

For each candidate fact about a class, ask: does a *user* of this class need
to know it to use it correctly? For `IndexLookup`: the wire message format
used to talk to servers — no, pure implementation detail; the comparison
function used for range matching — yes, callers need this; the server-side
index data structure — no, it should be hidden so thoroughly that not even
the class's own callers need to know it exists; whether requests to different
servers are issued concurrently — possibly, if it has a caller-visible
performance implication even though the mechanism stays hidden; the
crash-recovery mechanism — no, because recovery here is fully transparent
(if crashes *were* visible to callers in some other system, the interface
documentation would need to describe how they manifest, though still not the
internal recovery mechanics).

A second example on the same class's `isReady()` method: a bad version
leaked internal jargon and left a key internal term undefined; a good version
defined readiness purely in terms of caller-visible consequences (whether the
next call will block) and stated the important, non-obvious interface fact
that the method must be called for progress to occur at all.
