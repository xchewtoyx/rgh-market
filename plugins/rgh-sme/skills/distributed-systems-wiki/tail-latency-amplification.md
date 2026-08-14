---
type: concept
title: Tail Latency Amplification
description: >
  Fanning a request out to many backends means overall latency is gated by
  the slowest one, so a small per-node tail probability becomes a much
  larger probability of a slow response overall.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 17"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §2.2"
---

# Tail Latency Amplification

Even when a service's typical response is fast, a meaningful tail of
requests takes far longer — congestion, GC, scheduling contention, and
queueing anywhere along the path can each stall an individual call, largely
outside the calling service's control. A worked example: 1,000 sampled
cloud VM-launch requests had a mode of ~22s and a mean of ~28s, but the 95th
percentile was 57s — 5% of requests ran 2–10x the average. Monitoring and
capacity planning have to account for this tail, not just central tendency.

The tail matters far more once requests **fan out**. If a single call to
one backend has a 1% chance of being slow, a request that must wait on
[100 backends in parallel](partitioned-secondary-indexes.md) (a
scatter/gather read, for instance) has roughly a 1 − 0.99^100 ≈ 63% chance
that *at least one* of them is slow — and the caller's overall latency is
gated by whichever backend responds last. Fanning out doesn't just add
backends' individual risk, it compounds it: the more calls a single
response depends on, the more likely one of them lands in the tail, so
apparent (false) failure or slowness at the aggregate level becomes common
even though every individual backend is usually fine. This is the same
gating effect that shows up in [fan-out](fan-out.md) read paths and
scatter/gather [secondary-index queries](partitioned-secondary-indexes.md).

Two mitigations that trade extra work for a bounded wait:

- **Hedged requests.** Issue more requests than the number of responses
  actually needed, and cancel or ignore the stragglers once enough have
  returned — e.g. issue 11 requests to satisfy a need for 10, and cancel
  whichever one is still outstanding once the other 10 complete.
- **Alternative (staged) requests.** A cost-aware variant of hedging: issue
  the minimum batch first, then issue a small number of follow-up requests
  once most of the original batch has completed (e.g. issue 10, then 2 more
  once 8 of the original 10 are back), cancelling stragglers once the
  target count is reached. This spends fewer redundant requests than
  hedging everything up front, at the cost of a small added delay before
  the follow-ups are sent.

Where completeness itself is negotiable rather than just delayable, [trading
harvest for yield](yield-and-harvest.md) is the complementary move: return
a partial result now instead of waiting out the tail at all. On the write
side, [write buffering](write-buffering-for-latency.md) attacks the same
tail from a different angle: acknowledge from memory instead of storage, and
push the durability cost onto the replica quorum rather than the caller's
wait.

## Why SLAs are set — and measured — at the tail

This is also the direct argument for stating and monitoring performance
contracts in tail-percentile terms rather than as an average. Amazon's own
account: a single e-commerce page render can call over 150 internal
services, often in multi-level dependency chains, and each one's own
performance contract (SLA) has to hold for the whole chain to meet its
bound — the same amplification math above, applied to an organization's
service graph instead of a single scatter/gather fan-out. Amazon settled on
the 99.9th percentile specifically because a mean- or median-based SLA
hides exactly the customers most exposed to amplification — e.g. those
with the largest personalization histories, whose requests are
systematically more expensive to serve and therefore land in the tail more
often — so averaging silently excuses poor service to a real, identifiable
segment rather than reflecting a random sampling fluke. Going further than
p99.9 was evaluated and rejected on cost grounds: each additional nine got
measurably more expensive to guarantee for materially less benefit, an
ordinary cost/benefit stopping point rather than a universal constant.
