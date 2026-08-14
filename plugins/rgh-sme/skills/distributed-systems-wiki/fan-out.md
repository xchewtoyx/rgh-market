---
type: concept
title: Fan-Out
description: >
  One incoming write triggering many derived writes (or one read triggering
  many backend calls) — the Twitter-timeline trade between write-time
  materialization and read-time assembly.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 1"
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 5"
---

# Fan-Out

Fan-out is the multiplication factor between one operation and the work it
triggers. The canonical case study is Twitter's home timeline (c. 2012:
4.6k tweets/sec posted, 300k timelines/sec read):

- **Read-time assembly:** store tweets once; build each timeline on read by
  joining follows-tweets-users. Writes are trivial; the 300k/sec read side
  buckled under the query load.
- **Write fan-out (precomputed mailboxes):** on each tweet, insert it into a
  cached timeline per follower. Reads become a cheap cache fetch; writes
  multiply by the follower count — 4.6k tweets/sec became ~345k timeline
  inserts/sec at an *average* fan-out of 75. This is moving work to the
  [write path](read-path-and-write-path.md).
- **The heavy tail breaks the average:** follower counts are heavy-tailed;
  one celebrity tweet means 30M+ writes, blowing any delivery-latency
  budget. Averages lie about fan-out — design for the distribution's tail,
  the same skew that produces [hot keys](hot-spots-and-skew.md).
- **Hybrid:** fan out writes for normal users; exempt high-follower accounts
  and merge their tweets in at read time. Segmenting users by their load
  characteristics beats one rule for all.

Read-side fan-out has its own cost: a request that must await many parallel
backend calls (as in [scatter/gather](partitioned-secondary-indexes.md)) is
gated by the slowest of them — [tail latency
amplification](tail-latency-amplification.md) — and when completeness is
negotiable, [harvest can be traded for yield](yield-and-harvest.md). On the delivery side, broadcasting one event
to many consumers is the fan-out that
[message brokers](message-brokers.md) and
[logs](log-based-messaging.md) provide structurally.

## A poison query hits every fanned-out target at once

Wide fan-out has a failure mode distinct from slowness: if the query itself
is the problem — an untested input that crashes, hangs, or infinite-loops
whatever backend processes it (a "query of death") — sending it straight to
every one of a thousand [aggregation-tree](aggregation-trees.md) leaves
crashes all thousand simultaneously, along with every other in-flight query
those machines happened to be serving. A single-target failure is a
localized, [detectable](timeouts-and-failure-detection.md) event; a
fanned-out failure is a self-inflicted, fleet-wide outage delivered by the
caller's own traffic. **Canary requests** mitigate this cheaply: before
fanning a query out to all N targets, send it first to just one or two of
them and wait for a successful reply; only fan out to the rest once the
canaries have proven the query is safe. A canary failure flags the query
(automatically or via a fast-updatable banned-query list) and blocks it from
reaching the remaining targets — trading a small added latency on every
query for bounding the blast radius of the rare dangerous one.

## Serverless parallel invocation

A single trigger (HTTP request, event notification) can **fan out** to many
downstream function invocations run concurrently — the same decomposition
idea as MapReduce's map step: break a large job into independent pieces and
work them in parallel (e.g. resize one uploaded image to many thumbnail
sizes, each size depending only on the original).

The entry point's job is to **initiate** parallel work, not serialize it. A
common pitfall: looping over synchronous invoke calls (default
request/response semantics) makes each iteration wait for the worker to
finish — rebuilding a sequential pipeline while intending parallelism. Fix:
fire-and-forget / event-style invocation so the entry point dispatches all
workers without blocking on responses.

**Pub/sub fan-out** (e.g. SNS topic with multiple subscribers) removes the
entry point from tracking which workers to call: one notification wakes every
subscriber. That fits **disparate** parallel tasks (welcome email, account
setup, social-graph import on signup) but not **homogeneous** tasks with
different parameters — pub/sub delivers the *same* payload to every
subscriber, so N variants of the same operation mean N separately managed
functions unless you add routing logic elsewhere.

**Pub/sub into queues** (SNS → SQS) adds a [load buffer](queue-as-load-buffer.md):
notifications land in queues and workers poll at a controlled rate instead of
all subscribers waking at once. Use when parallel fan-out would overwhelm a
shared downstream (database connection pool, write capacity) — the queue
absorbs the burst while worker count sets sustainable parallelism.
