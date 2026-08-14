---
type: concept
title: Worked Example — Redesigning a Buffer Class Around Its Critical Path
description: >
  A real refactor of a buffer-management class shows designing around the
  critical path in practice — eliminating shallow, duplicated special-case
  checks made the class both faster and smaller.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 20"
---

A `Buffer` class managed what looked like a linear byte array over multiple
discontiguous underlying memory chunks — external chunks (caller-owned,
referenced not copied, for large data) or internal chunks (buffer-owned, data
copied in). This chunked design was already a sound structural fix against
expensive memory copies. As `Buffer` usage grew pervasive (several created
per RPC), the class's own implementation efficiency started to matter at a
system level, even though its high-level design was already sound.

**Target critical path**: allocating a small amount of new internal-chunk
space — the common case behind message-header construction. The ideal
behavior: one check confirming the last chunk is both internal and has
enough spare room, then just extend it.

**Diagnosed problems in the original code** (spread across three call layers
with identical method signatures — a direct instance of the
[different layer, different abstraction](different-layer-different-abstraction.md)
red flag, with the middle layer "nearly a
[pass-through method](pass-through-methods.md)"): numerous special-case
checks scattered and duplicated across the call chain — whether any
allocation existed at all; whether the current allocation had room, checked
twice (once inside the callee, again by the caller re-validating the return
value); a further re-check of that return value by the top-level caller. New
space was allocated first, generically, without regard to the existing last
chunk, and only afterward checked for adjacency to merge with it, adding yet
more conditionals. Six distinct conditions were checked on the critical path,
and every extra layer added both call overhead and another return value that
had to be checked.

**Fix**: refactor the whole class around its actual critical paths
(allocation, plus other common operations like retrieving total stored byte
count), eliminating the shallow layers and creating genuinely deep internal
abstractions. The refactored class shrank by 20% (1476 vs. 1886 lines)
*because* it was faster, not despite it. The new design collapses the whole
critical path into a single method with one test ruling out all special
cases at once, introducing a new instance variable tracking how much unused
space immediately follows the last chunk (zero if there's no space, the last
chunk isn't internal, or the buffer is empty) — this one field is what makes
a single-test critical path possible.

One deliberate small non-minimality: maintaining a running total-length field
on every allocation call costs a tiny bit of extra work on the critical path,
but was chosen over the "purer" ideal of recomputing total length on demand
from all chunks, because that recomputation would be expensive for buffers
with many chunks, and fetching total length is itself a common operation — a
small guaranteed-cheap update beats an occasionally-expensive recomputation.
This illustrates that
["the ideal"](design-around-the-critical-path.md) is a target to approach,
not a rule to follow absolutely, when a small deviation clearly serves the
overall critical-path goal better.

**Measured results**: appending a 1-byte string via internal storage dropped
from 8.8 ns to 4.75 ns (roughly 2x); constructing a buffer, appending a small
internal chunk, and destroying it dropped from 24 ns to 12 ns.
