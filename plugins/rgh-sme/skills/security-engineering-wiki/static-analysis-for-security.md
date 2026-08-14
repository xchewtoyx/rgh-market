---
type: concept
title: Static Analysis for Security
description: >
  A spectrum from fast AST-pattern linters through abstract interpretation
  to formal methods, each trading depth against cost — most effective
  integrated early, with fast feedback and low false-positive rates.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 13"
---

# Static Analysis for Security

Static analysis inspects source without executing it, ideally before
check-in — fixing bugs gets drastically more expensive after merge or
deploy. Verifying arbitrary properties of arbitrary programs is
undecidable, so every tool trades depth of analysis against cost, and
false positives against false negatives. The spectrum:

- **Automated code inspection (linters, AST pattern matching)** — Error
  Prone (Java), Clang-Tidy (C/C++), GoVet, Pylint. Shallow, scales to any
  codebase at roughly compile speed, easily extended with custom checks,
  and can emit *suggested fixes* applied with a click (or `--fix` for
  mass modernization). Catches real bug patterns: `sizeof(pointer)` in
  `memcpy`, incompatible collection types. This is also the enforcement
  layer for [safe types](safe-types.md) and restricted APIs.
- **Abstract interpretation ("deep" static analysis)** — semantic
  analysis over control/data flow, often interprocedural, summarizing
  possible values in abstract domains (e.g. intervals). Sound coverage of
  all behaviors at the price of approximation-induced false warnings, and
  much slower — run nightly or differentially at code review, not in the
  editor. Tools: Frama-C (C runtime errors, buffer overflows), Infer
  (dangling pointers), AbsInt (worst-case execution time); Android's App
  Security Improvement program has driven over a million Play Store app
  fixes this way.
- **Formal methods** — specify safety ("bad thing never observable") and
  liveness properties, verify or build correct-by-construction. High
  up-front cost (mathematically rigorous requirements); practical in
  hardware EDA, safety-critical software, and cryptographic protocol
  analysis (continuous verification of TLS implementations). See the
  verification spectrum in [security invariants](security-invariants.md).

**Integration determines value.** Feedback while the developer is still
in context beats findings after the code "works" — the same lesson as
[compile-time safe-type enforcement](safe-types.md). Google's Tricorder
platform runs ~50k code-review analyses/day across 146 analyzers and 30+
languages, surfacing warnings *during code review* with a hard usability
bar: easy to understand, easy to fix, ≤10% user-perceived false
positives — reviewers' "Not useful" clicks disable underperforming
checks. Most high-value checks in practice are the simple, fast kind.

(Related analysis techniques: disassemblers/decompilers like Ghidra for
reverse-engineering malicious binaries in
[forensics](digital-forensics.md); concolic testing — concrete plus
symbolic execution — for generating inputs that cover unexplored
branches, complementing [fuzzing](fuzz-testing.md).)
