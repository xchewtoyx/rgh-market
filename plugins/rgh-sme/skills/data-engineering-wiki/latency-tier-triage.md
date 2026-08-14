---
type: concept
title: Latency Tier Triage
description: >
  Forcing a vague "we want real-time" business request into one of three
  concrete latency tiers, each with a different architecture and a different
  data-quality cost.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 20"
---

Simply asking business stakeholders whether they want "real-time" data is
close to worthless — asked with no constraint attached, almost everyone says
yes. The useful move is to force the request into one of three concrete
tiers, each of which implies a genuinely different architecture rather than
just a dial turned further toward "fast":

- **Instantaneous**: the display reflects the source system's true state at
  every instant, updating synchronously as the source changes. Implemented
  by querying the source directly rather than caching anything in the
  pipeline — see [data federation and virtualization](data-federation-and-virtualization.md)
  for the mechanism. Query complexity has to stay limited, since all
  processing runs on the source system itself. A plausible real use case:
  live inventory availability, where a person is committing stock to a
  customer right now.
- **Intra-day**: updated many times a day without claiming to be the
  absolute current truth — the
  [data warehouse](data-warehouse-architecture.md) analogue of a
  15-minute-delayed stock quote. This is
  [micro-batching](micro-batch-vs-true-streaming.md) through a real, if
  compressed, pipeline: change data capture, extraction,
  staging, cleaning, conforming, key assignment, and load — all still
  present, just running far more frequently than a daily cycle. The
  technology shift from a daily pipeline shows up mainly in the first two
  steps: extraction now has to tap a high-bandwidth channel (message queue
  traffic, a continuously growing transaction log, low-level triggers) that
  a once-a-day pull never needed.
- **Daily**: valid as of the previous working day's batch download or
  reconciliation. Frequently the *better* choice even when faster delivery
  is technically possible, because source systems often run end-of-day
  correction processes on raw data — a daily pipeline can wait for that
  reconciled, stable output instead of pulling pre-correction data. It's
  also the simplest extraction case: the pipeline just waits until the
  source signals it's ready.

Each step down in latency buys speed by giving something up, most sharply in
data quality: the tightest [quality screens](quality-screens.md) — the ones
spanning multiple fields, records, or tables — often don't fit inside a
tight real-time processing budget, forcing a choice between shipping
under-validated data fast or running a slower, fully-screened path behind
it. Naming which tier a request actually needs, and being explicit with
stakeholders about what that tier trades away, is what turns "we want
real-time" from a slogan into a buildable requirement.

A practical middle ground doesn't require picking only one tier: run
intra-day delivery during the day for the freshness it buys, then still run
the full daily pipeline overnight to correct whatever the faster path
couldn't fully validate. Business users get low latency for the common case
without the pipeline having to pretend intra-day data is as trustworthy as
the reconciled daily batch.
