---
type: concept
title: Verification Checkpoint Proximity
description: Placing a verification check as close as possible to the thing being verified, since each additional inferential hop between them is a separate opportunity to be wrong.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 12"
---

# Verification Checkpoint Proximity

Once [effect propagation analysis](effect-propagation-analysis-for-verification-scope.md) has traced every point where a change's effects could become observable, several of those points are usually usable as a place to actually check the change. They are not equally good. **Verification checkpoint proximity** is the principle that a checkpoint close to the change is worth more than a checkpoint far downstream, even when both would technically catch a regression.

## Why proximity matters

A checkpoint far from the change point only provides evidence through a chain of reasoning: "the change affects X, which affects Y, which affects the thing I actually checked." Each link in that chain is a separate claim that could itself be wrong, and a distant checkpoint gives no direct way to confirm the whole chain actually holds — the only way to validate it is to deliberately break the change point and confirm the distant checkpoint's check actually reports a failure (the same logic as [test oracle self-validation](test-oracle-self-validation.md), applied to the inferential chain connecting cause to observation rather than to the check itself). A close checkpoint collapses that chain to nearly nothing, so there is very little left to be wrong about.

## Pinch points: a deliberate, temporary exception

When several related changes each require their own close-in checkpoint, and building each one independently is too costly to do up front, it can be more practical to find a single narrower point downstream where *all* of the changes' effects converge and are observable together — a **pinch point**. A pinch point is a property of a specific set of changes, not a fixed property of the code: adding a different, unrelated change to the same class may not go through the same pinch point at all, and a pinch point can silently stop covering a change if the code changes shape.

Treat a pinch point as scaffolding, not a destination. It answers "did something in this whole area break," which is real evidence, but it does not localize *which* part broke as precisely as a close checkpoint would, and it tends to grow slow and unwieldy as a permanent substitute for closer checks. The intended lifecycle is: use the pinch point to verify safely while working, then add closer checkpoints for each piece as it stabilizes, and let the broad pinch-point check retire once those closer checks exist.
