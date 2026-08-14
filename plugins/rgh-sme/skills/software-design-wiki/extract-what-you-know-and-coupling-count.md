---
type: concept
title: Extract What You Know, Guided by Coupling Count
description: >
  Extract only very small, confidently-named chunks without tests first,
  choosing them by counting how many values cross the new method's
  boundary — zero-coupling extractions are the safest, and naming them
  often produces design insight on its own.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 22"
---

A strategy for genuinely small, confidently-named chunks — "two or three
lines, five at most" — extracted without tests first, given tests
afterward. The risk metric that decides which chunks are safe to extract
this way is **coupling count**: the number of values flowing into and out of
a candidate extraction (instance-variable accesses don't count, since they
move with the code rather than crossing the new method's interface).
Extracting a two-line max-of-two-values calculation into its own method has
coupling count 3 (two parameters in, one return value out).

**Lower coupling count means safer extraction**, because the main risk in
manual extraction is a type-conversion mistake in the parameter or return
wiring, and low counts leave less room to get that wiring wrong — always
double-check where each passed variable is declared to get the extracted
signature right. **Zero-coupling-count extractions are the safest of
all** — pure "command" chunks that just tell the object to do something to
its own state (or occasionally global state), taking nothing and returning
nothing. Beyond safety, the act of trying to *name* such a chunk often
produces real design insight about what it's actually doing and how it
affects the object, which can cascade into further insight. A useful
personal habit when working without a tool: start by extracting a batch of
zero-count methods just to get oriented, as "a good prelude to testing and
further work."

Two caveats: don't let "small" creep upward — if a candidate extraction's
coupling count is above zero, reach for
[Introduce Sensing Variable](introduce-sensing-variable.md) to backstop it
instead of extracting on faith. And for [bulleted methods](monster-methods.md)
specifically, apparent chunk boundaries can be misleading, since chunks
often share temporaries — sometimes the profitable extraction lives within
or across the apparent bullet boundaries rather than matching them exactly.
Small extractions individually feel like they accomplish nothing, but
"progress has a way of sneaking up on you" as the method's structure
clarifies over repeated passes.
