---
type: concept
title: Look for Decisions That Can Change (Extraction Heuristic)
description: >
  A method's name often understates how much it actually does — extract
  hard-coded decisions (which API, which database, which format) into their
  own methods named after intent, before settling on final class
  boundaries, since a fully encapsulated decision is a clean extraction
  boundary in its own right.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

Method *names* alone often understate how much is really happening inside —
an innocuous-sounding `updateScreen()` might actually generate text, format
it, *and* push it to several different GUI objects. This heuristic:
exploratory [Extract Method](splitting-and-joining-methods.md) passes,
*before* settling on final class boundaries, specifically targeting
hard-coded assumptions or decisions buried in a method's body (a particular
API, a particular database, a particular format) — naming the extracted
method after the *intent* (what information is being fetched, say) rather
than the mechanism used to get it.

The side benefit runs beyond making later grouping easier: this can fully
encapsulate a low-level resource behind a small, coherent set of methods,
which then becomes a clean class-extraction boundary in its own right —
the extracted methods are already the right shape for a new class's public
interface once you decide to actually pull it out. See
[feature sketches](feature-sketches.md) for a complementary, more
structural way of finding the same kind of boundary by tracing instance
variable usage instead of reading method bodies.
