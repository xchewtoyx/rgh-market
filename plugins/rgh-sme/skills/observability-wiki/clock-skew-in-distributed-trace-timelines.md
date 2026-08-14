---
type: concept
title: Clock Skew in Distributed Trace Timelines
description: Span timestamps come from each service's own wall clock, so unsynchronized clocks across hosts can make a trace waterfall show effects like a child span starting before its parent or overlapping incorrectly, even though causality was preserved.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 2, Overview of the Patterns"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §2.1"
---

Every [span](trace-anatomy-and-spans.md) records its start timestamp from the wall clock of the host that emitted it. Machine clocks drift relative to each other (temperature, vibration, NTP sync gaps), so two spans that are causally ordered — a parent's outbound call and the child span it triggers on another host — can carry timestamps that make the child appear to start *before* the parent, or make a waterfall visualization show impossible overlaps. This is a display/reconstruction artifact of clock skew, not evidence the instrumentation or [context propagation](context-propagation.md) is broken.

Distributed systems that need a real ordering guarantee (not just an approximate one for human debugging) solve this with logical or hybrid clocks rather than trusting wall-clock timestamps alone:

- A **Lamport clock** — a counter incremented on every event and carried forward on every message, bumped to `max(local, received) + 1` on receipt — guarantees causally-later events get higher counter values, but only gives a partial order: two events with no message path between them still can't be ordered.
- A **hybrid logical clock** pairs wall-clock time with a Lamport-style tiebreaker counter, so causally-later events still sort higher even when the receiving node's own clock lags behind the sender's.
- A **bounded clock-skew wait** (e.g. Google Spanner's TrueTime) makes a write wait out the cluster's known maximum clock skew before it becomes visible, trading write latency for a hard external-consistency guarantee.

For observability purposes, the practical takeaways are narrower than adopting any of these: (1) don't over-trust small (sub-tens-of-ms) ordering differences between spans on different hosts in a waterfall view — treat them as within clock-skew noise rather than as an instrumentation bug to chase; (2) if a system's tracing SDKs support a monotonic or logical sequence number alongside wall-clock timestamps, prefer it for strict causal ordering; (3) large, consistent clock-skew symptoms (a whole host's spans reliably offset by seconds) are themselves worth alerting on — they usually indicate broken NTP sync on that host, which also silently corrupts log-timestamp correlation across services.

A lighter-weight technique tracing analysis tools can apply without adopting logical clocks at all: exploit the fact that an RPC client always sends its request *before* the server receives it (and, symmetrically, the server always sends its response before the client receives it). Even without trusting either host's absolute clock, this ordering constraint gives a valid lower and upper bound on the server-side span's true timestamps, which is enough to sanity-check or correct a display timeline without requiring any change to how spans are generated.
