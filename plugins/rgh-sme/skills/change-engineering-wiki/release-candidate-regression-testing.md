---
type: concept
title: Release Candidate Regression Testing
description: >
  Re-run the comprehensive test suite against an assembled release candidate
  even after post-submit CI passed, for sanity, auditability, cherry-picks,
  and emergency cuts.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Release Candidate Regression Testing

After a change passes [continuous build](green-head-vs-true-head.md) — possibly
after failure cycles — it enters a pending release candidate. Continuous
delivery then promotes that candidate through sandboxed and shared test
environments (dev, staging), often including manual QA, running **larger
tests against the entire assembled unit**.

Run that comprehensive suite against the release candidate even when the
same suite already ran post-submit on individual commits, because:

- **Sanity check** — confirm nothing strange happened during cut,
  packaging, or assembly.
- **Auditability** — results tied to the RC are readily available without
  digging through continuous-build logs.
- **Cherry picks** — a cherry-picked fix diverges the RC's source from the
  latest continuous-build-tested cut, requiring fresh verification.
- **Emergency pushes** — continuous delivery can cut from true head and run
  a minimal test set for confidence without waiting for full continuous
  build.

This pairs with [build once, promote the
artifact](build-once-promote-artifact.md): the RC is the unit under test;
artifacts should not be silently rebuilt between environments during
promotion.
