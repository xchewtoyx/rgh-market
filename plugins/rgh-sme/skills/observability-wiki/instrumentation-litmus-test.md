---
type: concept
title: Instrumentation Litmus Test for Every Change
description: A simple check to apply to every code change before shipping it — "how will I know if this is working as intended?" — turns instrumentation from an afterthought into a routine part of writing the change itself.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 9"
---

Good instrumentation is only useful if it's captured consistently, not just occasionally when someone remembers. A practical litmus test to apply to every pull request: **"How will I know if this change is working as intended?"** For example, adding a cache layer should also add `cache.put`/`cache.get`/`cache.hit` attributes — the instrumentation for verifying the change's own behavior ships alongside the change itself, rather than being bolted on later once something goes wrong.

This is the same friction-reduction goal as [making instrumentation a one-line change](low-cost-instrumentation-with-statsd.md), applied as a review-time habit rather than a tooling investment: asking the question consistently is what keeps instrumentation coverage from silently decaying as a codebase grows. Applying this test liberally is only safe if [the runtime cost of an unsampled annotation is negligible](unsampled-instrumentation-overhead-must-be-near-zero.md) — otherwise adding instrumentation on every change would trade correctness confidence for production risk.

A stricter, always-on variant of the same idea is [embedding runtime invariant assertions](runtime-invariant-assertions-as-embedded-oracle.md) directly at the point a change touches state, rather than only checking "is there a signal" — an assertion actively declares what correct looks like and flags the moment reality diverges from it. Once you've decided to add the instrumentation, [write it inline rather than behind a single-call-site wrapper method](inline-instrumentation-over-wrapper-methods.md) so it stays next to the context that explains it.
