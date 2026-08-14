---
type: concept
title: Checklist Item Selection Trade-offs
description: Criteria for deciding which steps earn a place on a short operational checklist when many candidate items compete for limited space.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 7"
---

Because a usable checklist is capped at a handful of items (see [Runbook and Checklist Design](runbook-checklist-design.md)), most candidate steps proposed during drafting must be cut. Deciding what survives requires weighing more than "is this step correct" — it requires trading off frequency, severity, and the risk introduced by the check itself.

## Selection Criteria

When narrowing a long candidate list down to the items that make the final checklist, weigh each candidate against:

- **Severity over frequency alone**: A rare failure mode still earns a slot if it is fast to check and catastrophic when missed (e.g. confirming the correct target before an irreversible action). Don't cut an item just because its trigger condition is uncommon.
- **Net risk of the check itself**: Drop items whose verification step could itself cause harm, especially in contexts or sites with less-experienced operators (e.g. a check that requires administering a risky intervention has different risk profiles in high-resource vs. low-resource, high-experience vs. low-experience environments). A checklist item is not free just because it targets a real risk — the act of executing it must not introduce a comparable or greater one.
- **Cost of the surrounding failure**: Compare the item's failure mode against baseline harm elsewhere in the process. An extremely rare failure mode competing with the same checklist space as a common, high-harm failure mode should usually lose out to the latter.
- **Communication-forcing items**: Retain items whose main value is forcing cross-role communication (e.g. team introductions, briefings) even when they don't map to a single failure mode. Their payoff is surfacing problems the checklist's other items can't anticipate — see [Checklist Forcing Function Types](checklist-forcing-function-types.md) for this distinction.

## Consequence

Item selection is inherently a local judgment call, not a universal formula — the same candidate item can be correctly included at one site and correctly cut at another (differing baseline incidence, differing resource levels, differing operator experience). Checklist authors should expect and document these trade-off decisions rather than treating the final item list as self-evidently correct, so a future maintainer understands why an item was left out instead of re-adding it blindly.

For how the surviving items should be organized and paced during execution, see [Runbook and Checklist Design](runbook-checklist-design.md).
