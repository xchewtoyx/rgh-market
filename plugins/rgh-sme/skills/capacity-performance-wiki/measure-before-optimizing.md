---
type: concept
title: Measure Before Optimizing
description: Performance intuition is unreliable even for experienced engineers, so changes should be preceded by measurement that locates a real hot spot and followed by measurement that confirms the change actually helped — with unconfirmed changes backed out.
sources:
  - title: "A Philosophy of Software Design, 2nd Edition"
    resource: "A Philosophy of Software Design, 2nd Edition (John Ousterhout), ch. 20"
---

Intuitions about what's slow are unreliable, even for experienced engineers. Acting on a hunch about where a system is slow risks two costs at once: wasted effort on a change that doesn't move the needle, and permanently added complexity for no real gain. The discipline is to measure both *before* choosing what to change and *after* making the change, rather than trusting judgment at either end.

## Two Purposes of Measuring First

1.  **Locating where tuning effort will actually matter.** Top-level system timing alone tells you the system is slow, not *why* — it doesn't identify a hot spot precisely enough to act on. Effective triage (e.g. via the [USE method](use-method.md) for resource-level bottlenecks, or [off-CPU analysis](off-cpu-analysis.md) for blocked-time bottlenecks) needs to drill down until it isolates a small number of specific hot spots for which there is also a concrete idea for improvement — a located bottleneck with no plausible fix isn't yet actionable.
2.  **Establishing a baseline.** Without a pre-change measurement, there is no way to confirm a change actually helped after making it — only a belief that it should have.

## The Backing-Out Discipline

After making a targeted change, measure again under the same conditions as the baseline. If the change doesn't produce a measurable improvement, back it out — unless it happened to simplify the code anyway. There is no reason to keep added complexity that buys no confirmed speedup; a change justified only by the intuition that it "should" help, absent a measured before/after comparison, is exactly the kind of unverified assumption this discipline exists to catch.

## Relationship to Explaining Changes After the Fact

This discipline is the front half of a pair with [explaining unexpected performance changes](explain-unexpected-performance-changes.md): measuring before and after a *deliberate* change confirms whether that specific change worked, while the discipline of explaining an *unexplained* win or loss applies the same before/after rigor retroactively, to a change whose performance effect wasn't the thing being tested for. Both refuse to accept an unverified performance story, whether the change was intentional or not.
