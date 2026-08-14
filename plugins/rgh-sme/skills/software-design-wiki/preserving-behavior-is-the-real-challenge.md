---
type: concept
title: Preserving Behavior Is the Real Challenge of Changing Code
description: >
  Every kind of code change is dominated by the amount of behavior that must
  be preserved, not the usually small amount that's intended to change —
  and preservation isn't passive, because it requires actually knowing what
  behavior is at risk.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 1"
---

Of the three things that can change when you touch a system — structure,
functionality, resource usage — [refactoring](refactoring-preserves-behavior.md)
and optimization both hold functionality invariant on purpose. Feature
addition holds *existing* functionality invariant while adding new
functionality. Even bug fixing changes only a small slice of functionality
relative to what's preserved. Every one of the
[four reasons to change software](four-reasons-to-change-software.md) is
therefore dominated by the same problem: "Preserving existing behavior is one
of the largest challenges in software development."

The practical difficulty isn't leaving code alone — preservation isn't
passive. It's *knowing* that behavior isn't changing when you don't actually
know how much behavior is at risk from a given edit. Understanding is the key
thing needed to make changes safely, which is exactly what
[characterization tests](characterization-tests.md) and the rest of this
domain's dependency-breaking toolkit exist to provide when that understanding
isn't already there.
