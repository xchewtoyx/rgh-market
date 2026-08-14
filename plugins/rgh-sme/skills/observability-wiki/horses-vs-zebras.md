---
type: concept
title: Horses vs. Zebras
description: Most failures have common, well-understood causes ("horses"), but at large enough scale, the common causes get found and fixed over time, leaving an increasing share of failures caused by rare, previously-unseen conditions ("zebras") — and telling which kind you're facing changes how you should debug.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

"When you hear hoofbeats, think horses, not zebras" — most ailments (and most bugs) are common, not exotic. An engineer debugging an unexpected crash shouldn't first suspect a rare hardware fault; that's usually the wrong hypothesis.

But this heuristic inverts at scale. As a system's common problems ("horses") get found and eliminated over time, rare problems ("zebras") make up a growing share of what's left — a 0.1%-per-year chance of an uncorrectable memory error is negligible for one machine, but across 400,000 memory chips in a large fleet it becomes hundreds of occurrences a year, i.e. routine. What was once an implausible hypothesis becomes, at scale, the default explanation.

This directly maps to [known-unknowns vs. unknown-unknowns](known-unknowns-vs-unknown-unknowns.md): horses are enumerable, previously-seen failure classes; zebras are the novel, previously-unencountered ones. New/small systems should expect mostly horses; older, larger, well-operated systems should expect an increasing proportion of zebras, because the horses have already been found and fixed. Debugging technique should shift accordingly — for zebras, [testing hypotheses against real data](hypothesis-testing-with-real-data.md) matters even more, since intuition trained on common cases is actively unhelpful.
