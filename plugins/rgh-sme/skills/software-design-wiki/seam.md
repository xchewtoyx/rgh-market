---
type: concept
title: Seam
description: >
  A seam is a place where you can alter a program's behavior without
  editing the code at that place, by changing a decision made at some
  separate enabling point instead — the central mechanism behind nearly
  every dependency-breaking technique.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 4"
---

Treating a program as one long document to read and edit carefully breaks
down as soon as you try to pull an individual class out for unit testing:
"even when pieces of software look independent, they often depend upon each
other in subtle ways," and extracting a class for testing forces work
regardless of how good the design otherwise is.

A **seam** is a place where behavior can be altered without editing the code
at that place. Every seam has an **enabling point** — a place where the
decision to use one behavior or another actually gets made (a build flag,
a classpath, which object gets constructed). The source code at the seam
itself stays identical between production and test; only the decision made
at the enabling point differs.

Motivating question: a method makes a call, buried inside it, to some other
subsystem that's painful to exercise under test. How do you run the rest of
the method under test without triggering that call, while leaving the call
intact in production, without literally deleting or editing that line? Three
kinds of seam answer this differently, depending on which build-pipeline
stage supplies the enabling point: [preprocessing seams](preprocessing-seams.md),
[link seams](link-seams.md), and [object seams](object-seams.md) — the same
call site can often have more than one of these available simultaneously.

Seam-thinking is meant to become a permanent lens for reading and writing
code, not just a legacy-code rescue tactic: seeing code in terms of seams
makes it easier both to find ways to test existing code and to structure new
code so it stays testable from the start. [Branch by abstraction](branch-by-abstraction.md)
scales the same idea up: introducing a seam around a whole component so its
implementation can be swapped incrementally, on mainline, without a long-lived
branch.
