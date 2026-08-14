---
type: concept
title: Goodhart's Law
description: A metric that becomes a target stops being a trustworthy measure, because the people or systems it evaluates adapt to optimize the metric rather than the underlying goal it was meant to track.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
---
# Goodhart's Law

**Goodhart's Law**: "When a measure becomes a target, it ceases to be a good measure." Once people know a specific number is being used to evaluate or reward them, they have an incentive to optimize that number directly, which can diverge sharply from optimizing the underlying thing it was originally meant to track. A closely related formulation, **Campbell's Law**, states that the more a quantitative indicator is used for decision-making, the more it becomes subject to corruption pressures and the more it distorts the very process it was meant to monitor.

## Recognizable Patterns
- A bounty or incentive program targeting a proxy (e.g., paying per unit of evidence of a problem) can incentivize *manufacturing* more of the proxy rather than solving the underlying problem.
- Rankings or scores based on a public formula get gamed at exactly the input variables the formula weights, sometimes right up to (but not crossing) a defined threshold.
- Individual or team incentive metrics (sales volume, citation counts, publication counts) get optimized directly — through gaming, timing, or self-referential behavior — independent of the metric's original purpose.
- Project milestone attestations (e.g., "design complete," "requirements signed off") become the target once they're what gets reported upward — teams optimize for producing the sign-off rather than for the underlying design or requirements actually being sound, see [working software as status evidence](working-software-as-status-evidence.md).

## Verification Action
- **When designing a metric**: ask whether the people or systems being measured will predictably change their behavior to move the number, independent of the underlying goal.
- **When reading someone else's metric-based claim**: ask whether the metric is a target for the party reporting it, and if so, whether the reported number could have been produced by optimizing the metric directly rather than by the underlying outcome actually improving. This is especially important for [benchmark claim verification](benchmark-claim-verification.md), where a reported number is frequently the exact metric a vendor or team is incentivized to maximize.

## See Also
- [Benchmark Claim Verification](benchmark-claim-verification.md)
- [Cherry-Picking](cherry-picking.md)
