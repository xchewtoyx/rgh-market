---
type: concept
title: Record Observations and Rejected Theories During Investigation
description: Writing down what you observe and what you theorized — including theories you've already ruled out — gives an investigation structure, lets someone else pick it up without duplicating work, and often exposes the gap between your mental model of the system and its real behavior.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

During an investigation, write down what you observe, and separately write down your theories — including ones you've already rejected. This has several practical benefits:

- It gives the investigation structure and a record of what's already been tried, which matters because you don't know in advance whether resolution takes five minutes or five months.
- Another investigator can read the notes, understand what's been observed, and take over or contribute without duplicating work already done.
- Writing down what you *expected* to observe, and why, next to what you actually observed, tends to surface the gap between your mental model of the system and its real implementation — bugs often live exactly in that gap.

This is a lightweight process discipline that supports the [core analysis loop](core-analysis-loop.md) and [systematic troubleshooting process](systematic-troubleshooting-process.md) — it's what makes a hypothesis-driven investigation auditable and resumable rather than a sequence of untracked guesses.
