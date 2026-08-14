---
type: concept
title: DoS Defense in Depth
description: >
  DoS is economics — attacker demand versus your capacity — defended by
  layered filtering from network edge to application, shared
  infrastructure economies, and services designed to be cheap to serve.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 10"
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

# DoS Defense in Depth

Denial of service is best framed economically: the adversary tries to
make *demand* for a service exceed the *supply* of its capacity, forcing
you to choose between the expense of absorbing the attack and the losses
of downtime. Any service can be a target (DoS extortion strikes
indiscriminately — and demonstration attacks are usually the extortionist's
entire capability). Since always-on overprovisioning against the largest
attacks is infeasible, defense is about efficiency.

**Think like the attacker**: they focus limited resources on one
constrained resource in your dependency chain — DNS, network bandwidth,
frontend CPU/memory, or a backend like a database; disrupting any step
disrupts the service. Novices flood; sophisticated attackers send
*costly* requests (abusing search endpoints). Scale comes from botnets or
**amplification attacks** — spoofed small requests reflected off open
servers (DNS, NTP, memcache) whose larger responses converge on the
victim; these are mostly identifiable by well-known source ports and
throttled with network ACLs. Prioritize defenses by threat model — how
many machines must an attacker control to hurt you? — not by recency of
the last outage. (Terminology: *DoS* = single-host-sourced, defendable at
application layer; *DDoS* = effective only through distribution,
filtered in infrastructure.)

**Layered, shared defenses** ([defense in depth](defense-in-depth.md)):
edge routers throttle high-bandwidth attacks to protect the backbone;
network load balancers throttle packet floods to protect application
load balancers; those throttle application-level attacks before
frontends. Each inner layer only needs capacity for what breaches the
outer one, and dropping traffic early conserves bandwidth and CPU (edge
ACLs, edge caching proxies). Shared infrastructure gives economy of
scale — an attack overwhelming one site is noise across a whole shared
load-balancing fleet — which is also the model of commercial mitigation
services. Prevent focus: load balancers spread traffic to datacenters
with capacity, and **anycast** disperses a distributed attack across
worldwide locations so it can't concentrate on one. Caution: stateful
firewalls in the inbound data path invite *state-exhaustion* attacks —
use stateless router ACLs as the first line.

**Defendable service design** — cheap-to-serve is hard-to-DoS, and saves
money in normal operation:

- Cache-Control headers so proxies serve repeated content without
  touching backends.
- Fewer requests per pageview (sprite small images — one redesign saved
  10M requests/day), which also reduces bot-detection false positives.
- Minimize egress: attackers can saturate *outbound* bandwidth by
  fetching large resources; right-size images, rate-limit or deprioritize
  unavoidably large responses.
- Above all, [degrade gracefully](graceful-degradation.md) under
  overload — read-only modes, reduced feature sets, and servers designed
  never to crash under any load.

For active mitigation when design isn't enough, see
[DoS mitigation and response](dos-mitigation-response.md). Selling the
cross-team work: capacity planning gets to target real demand instead of
worst-case attacks at every layer, and the same filtering blocks
exploitation of known application vulnerabilities while patches are
prepared.

**Canary requests protect high-fan-out systems from a single query
crashing the fleet.** A "query of death" — a crafted or accidental request
that crashes, hangs, or infinite-loops the server handling it — is far
more dangerous in a server tree that fans a query out to hundreds or
thousands of leaf shards simultaneously: without protection, the same
malicious or buggy query hits every leaf at once and can take the whole
service down in one shot, along with every other in-flight query on those
machines. The mitigation sends the query first to just one or two
leaves — the canaries — and only fans out to the rest once those reply
successfully within a reasonable time; a canary crash or hang flags the
query as dangerous and blocks it before it reaches the remaining shards.
This defends against unpredictable bugs and deliberately crafted
DoS-style queries alike, and complements an updatable banned-query list
for the (typically slower, human-curated) permanent fix.

**Cost is a target independent of availability, especially in pay-as-you-go
cloud infrastructure.** A DoS attack doesn't have to take a service down
to hurt it — driving up its bill can be the entire objective, and elastic,
metered infrastructure makes this a distinct attack shape from a
resource-exhaustion DoS: the service may stay fully available throughout
while an attacker forces excessive billed usage (e.g. driving mass
downloads against a public object-storage bucket priced per byte
transferred). Traditional DoS defenses (edge filtering, load shedding)
don't target this because availability isn't what's under attack — the
matching mitigations are requester-pays pricing (shifting the marginal
cost back onto whoever generates the traffic) and active spend monitoring
with fast access revocation, functioning as the billing-layer analog of
[DoS mitigation and response](dos-mitigation-response.md)'s alerting and
automated response.

**Scraping is a related but distinct threat**: automated bulk extraction
of content by simulating a browser and parsing responses is simultaneously
IP theft, a terms-of-service violation, and — if run fast enough —
functionally a DoS attack. The standard architecture routes query-pattern
telemetry from frontends to a central scraping-detection service, which
flags suspected sources back to the frontends for blocking (high
confidence) or a CAPTCHA-style challenge (lower confidence) — with an
explicit whitelist so sanctioned automated traffic, like search-engine
crawlers, isn't caught by the same filter.
