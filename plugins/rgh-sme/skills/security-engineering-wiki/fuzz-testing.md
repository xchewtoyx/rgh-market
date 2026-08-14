---
type: concept
title: Fuzz Testing
description: >
  Generating vast numbers of unexpected inputs — coverage-guided, seeded,
  and sanitizer-instrumented — to find memory corruption, crashes, and
  DoS-triggering edge cases that human-written tests never consider.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 13"
---

# Fuzz Testing

A fuzz engine generates candidate inputs, a fuzz driver feeds them to the
fuzz target, and the engine watches how the system reacts. Prime targets
are anything parsing complex input: file parsers, decompressors, network
protocol implementations, codecs. Payoffs span security (memory
corruption; Heartbleed falls out of fuzzing OpenSSL with the right driver
and ASan in short order) and reliability (inputs triggering runtime
exceptions that cascade into DoS; timeout-bounded runs catch
deadlock/infinite-loop inputs). Differential fuzzing compares two
implementations of the same function and reports mismatches as crashes —
ideal when swapping libraries.

**How engines get smart**: beyond dumb random bytes, coverage-guided
engines (libFuzzer, AFL, Honggfuzz) use compiler instrumentation to see
which code paths an input reaches, preserving inputs that open new paths
as mutation material. Boost them with a **seed corpus** of representative
inputs (existing test sample files, published corpora) and
**dictionaries** of format keywords so generated input survives the
parser instead of dying on invalid tokens. Monitor coverage; a plateau
means investigating what the fuzzer can't reach. Run multiple engines
and cross-pollinate their interesting samples.

**Pair with sanitizers** ([memory safety](memory-safety.md)): without
instrumentation, only OS-visible crashes register — corrupted-but-unused
memory and undefined behavior pass silently. Sanitizer callbacks give the
engine well-defined error events plus rich crash metadata (stack trace,
memory layout) for triage and prioritization (read violations vs. write
violations). Caveats: handwritten assembly escapes instrumentation
(false positives and missed bugs); binary-only code needs CPU-emulator
integration (slower, less bug detail); and benign shallow crashes (e.g.
inconsequential signed-integer overflow) can block deeper exploration —
annotate "known safe" functions to disable a sanitizer only after
careful review.

**Driver hygiene**: avoid nondeterminism, slow I/O, and intentional
crashes; disable adversary-fixable integrity checks (CRCs the engine
can never satisfy) behind a `FUZZING_BUILD_MODE...` flag. To fuzz
configuration dimensions in one driver, derive options from a slice of
the input (or FuzzedDataProvider) rather than hashing it — the engine
then learns option/behavior relationships — but mind that inventing a
pseudoformat breaks compatibility with real-world seed files.

**Run it continuously.** Fuzzing is open-ended, so it can't gate commits;
it complements pre-commit testing by finding cases engineers never
imagined, and each crashing input becomes a regression test. Continuous
infrastructure (ClusterFuzz; OSS-Fuzz for open source) builds fuzzers
daily, manages corpora, deduplicates crashes by program state, files
bugs, retests known crashers, and auto-closes fixed ones — finding
issues hours after a change lands, before users are affected.

Fuzzing is also one of the discovery sources feeding
[continuous validation](continuous-validation.md) and
[static analysis](static-analysis-for-security.md) complements it from
the no-execution side.
