---
type: concept
title: How to Think About Performance During Design
description: >
  Neither micro-optimizing every statement nor ignoring performance entirely
  works well — the middle path is developing working knowledge of which
  operations are fundamentally expensive and defaulting to the cheap
  alternative whenever it's equally simple.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 20"
---

Micro-optimizing every statement slows development and adds needless
complexity while often not even helping, since many "optimizations" don't
pay off. Ignoring performance entirely tends to scatter many small
inefficiencies throughout the code — a "death by a thousand cuts" that can
leave a system 5-10x slower than necessary, and is hard to fix retroactively
because no single change moves the needle.

The middle path: build a working sense of which operations are
*fundamentally* expensive, and default toward the cheap alternative when a
clean, simple option exists on both sides. As rough intuition (not
benchmarks to cite verbatim): a network round-trip within a datacenter costs
tens of thousands of instruction-times; disk I/O costs millions;
flash costs tens of thousands; a DRAM cache miss costs a few hundred
instruction-times, often as significant to overall performance as raw
computation. A small, purpose-built micro-benchmark framework — isolating the
cost of one operation at a time — is worth building as infrastructure: a few
days of upfront investment can make each subsequent micro-benchmark a
5-10 minute addition, useful both for characterizing library performance and
validating new code.

Examples of choices that are naturally efficient at no added complexity cost:
preferring a hash table over an ordered map for key-based lookup when
ordering isn't needed (both equally simple via standard libraries, but a hash
table can be 5-10x faster); storing an array of structures inline, in one
contiguous allocation, rather than as an array of pointers to separately
allocated structures.

The decision rule when efficiency genuinely trades off against complexity: if
a more efficient design adds only a small amount of complexity, and that
complexity stays hidden rather than leaking into interfaces, it may be worth
adopting immediately — with the caution that
[complexity is incremental](incremental-accumulation-of-complexity.md) still
applies, so this isn't a free pass. If the faster design adds substantial
implementation complexity or complicates interfaces, prefer starting simple
and optimizing later only if performance actually becomes a demonstrated
problem — unless you already have solid evidence a given path will matter,
in which case building the faster version immediately is reasonable. A
distributed storage system that deliberately added complexity to bypass the
kernel for networking, based on prior measurement showing kernel-based
networking would be too slow, is an example of a justified upfront
complexity investment based on real evidence — one that then let most of the
rest of the system stay simple.
