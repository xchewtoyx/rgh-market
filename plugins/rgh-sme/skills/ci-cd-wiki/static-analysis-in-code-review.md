---
type: concept
title: Static Analysis Surfaced in Code Review
description: >
  Running fast static-analysis checks against a change and displaying the
  results directly inside the code review UI, with one-click fixes and a
  false-positive feedback loop, rather than as a separate pipeline gate the
  developer checks after the fact.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 13"
---

# Static Analysis Surfaced in Code Review

A [nonfunctional test gate](nonfunctional-test-gate.md) or [shift-left
security](shift-left-security.md) scan runs static analysis as a pass/fail
pipeline stage. A complementary integration point runs the same class of
fast, shallow checks (linters and AST pattern-matchers — style, common bug
patterns, API misuse) and surfaces the findings directly where the reviewer
and author are already looking: inline in the code review UI, at the moment
the change is under review, rather than as a separate report to go check.

This placement matters because it's the cheapest possible moment to fix an
issue — before the change has even merged — and because linter-class checks
can often propose the fix directly (an AST-level rewrite the author applies
with one click), turning a review comment into a zero-effort correction
instead of a to-do.

## The false-positive feedback loop

Because these tools run on every reviewed change, false-positive rate is a
first-class quality metric, not an afterthought: give reviewers a
lightweight way to mark a specific finding "not useful," and route that
signal back to whoever owns the individual check so noisy checks get tuned
or disabled. Without this loop, a check with a high false-positive rate
trains developers to ignore the whole tool rather than just the one bad
check, defeating every other check bundled alongside it.
