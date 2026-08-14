---
type: concept
title: Memory Safety
description: >
  Around 70 percent of security vulnerabilities are memory-safety issues;
  memory-safe languages eliminate the class by default, and sanitizers
  catch what remains in unsafe languages.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 12, 13"
---

# Memory Safety

Memory-safety errors dominate vulnerability statistics: ~70% of all
security vulnerabilities per Microsoft (stable over 12+ years), 85% of
Android bugs per Google. Language choice is therefore one of the
highest-leverage security decisions in a project: a memory-safe language
(Java, Go, and similar) removes the entire class — buffer overflows,
use-after-free, uninitialized reads, leaks — by default, for both
security and reliability.

Where C/C++ is required, run sanitizers continuously (presubmit or CI,
not opt-in):

- **Valgrind** — interprets the binary (no recompile); catches
  unallocated/out-of-bounds/uninitialized reads and leaks; its Helgrind
  tool finds pthread misuse, lock-ordering deadlocks, and data races.
- **Google Sanitizers suite** — ASan (memory errors), LSan (leaks), MSan
  (uninitialized reads), TSan (races and deadlocks), UBSan (undefined
  behavior: misaligned pointers, signed overflow, float conversion
  overflow). Up to 10x faster than Valgrind, with IDE integration.
- **Go Race Detector** — Go prevents C++-style corruption but still has
  data races.

How sanitizers work: the compiler instruments the binary with callbacks
into a runtime that tracks execution metadata — ASan keeps shadow memory
marking each byte's validity and "poisons" red zones around allocations
and freed regions, yielding precise reports (exact line, allocation and
free sites) for overflows and use-after-free. Instrumented binaries can
be orders of magnitude slower, so teams commonly run sanitizer-enhanced
pipelines nightly in CI rather than on every commit. Sanitizers multiply
the power of [fuzzing](fuzz-testing.md), which otherwise only sees
OS-visible crashes.

Memory-unsafe runtime code can also be contained architecturally —
sandboxing and layered containment
([defense in depth](defense-in-depth.md)) — and typed APIs address the
non-memory vulnerability classes ([safe types](safe-types.md),
[strong domain types](strong-domain-types.md)).
