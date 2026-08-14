---
type: concept
title: DoS Mitigation and Response
description: >
  Automated detection and response that fails static, strategic responses
  that don't teach the adversary, and recognizing when the "attack" is
  synchronized users or your own clients' retry loops.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 10"
---

# DoS Mitigation and Response

When [defendable architecture](dos-defense-in-depth.md) isn't enough,
active mitigation takes over.

**Alert only when action is needed.** Monitor request rate alongside
CPU/memory so a spike is diagnosable as an attack. But if the attack
isn't causing user-facing harm, absorb it: page only when demand exceeds
capacity and automated defenses have engaged (synfloods only when
syncookies trigger; bandwidth attacks only when a link saturates).

**Automated mitigation system** = *detection* (sampled traffic
statistics aggregated centrally; anomaly identification joined with
load-balancer knowledge of capacity) + *response* (e.g. IP blocks,
throttles, JavaScript/CAPTCHA challenges) — buying the response team time.
Design points:

- **False positives are unavoidable** — NAT puts many users behind one
  IP; CAPTCHA bypasses limit collateral damage. Exemption cookies must be
  abuse-resistant: pseudo-anonymous ID (revocable), challenge type
  (harder challenges for more suspicion), timestamp (expiry), solving IP
  (no botnet sharing), and a signature (unforgeable).
- **The mitigation system must survive attacks** — avoid dependencies on
  production infrastructure that DoS can take down, *including the
  response team's tools and comms* (backup channels and playbook storage
  if your chat/docs are your own product; see
  [emergency access](emergency-access.md)).
- **Respond in seconds, canary anyway**: mitigation needs speed that
  conflicts with slow-rollout hygiene; compromise with very brief
  canaries (as little as 1 second) for every change including automated
  responses.
- **Fail static.** If the central controller fails, failing closed is an
  outage and failing open admits the attack; freezing the current policy
  lets the controller die mid-attack without either — and means the DoS
  engine needn't match frontend availability, cutting cost. (A third
  option beside [fail safe/fail secure](fail-safe-vs-fail-secure.md).)

**Respond strategically, not just reactively.** The adversary has
unlimited probe attempts; naive filtering teaches them. Given a botnet
self-labeled `User-Agent: I AM BOTNET`, dropping on that string trains
the attacker to imitate Chrome; instead enumerate the sending IPs and
CAPTCHA-intercept *all* their traffic for a while — defeating A/B probing
and pre-blocking the botnet under any future disguise. Read capability
from the attack (small amplification → maybe one spoofing server; HTTP
DDoS → real botnet), and consider allies: mitigation providers, upstream
network filtering, the operator community.

**The "attack" may be nobody's attack.**

- *Synchronized users*: an earthquake, or a TV game show asking viewers
  to search word completions, produces bot-like bursts from real users —
  sometimes the fix is a product change (word suggestions ended the
  game-show traffic).
- *Client retry loops*: errors trigger retries; retries synchronized by
  the outage produce repeating bursts that block recovery (a
  self-inflicted DDoS commonly ~30x normal for DNS operators). Build
  clients with exponential backoff *plus jitter*. When you don't control
  clients, answer as many requests as possible while staying healthy via
  upstream throttling — every success releases one client from its loop.

Preparation means your service's functionality and failure modes are
determined on your terms, not the adversary's — including deliberate
choices like blocking a hosting provider (with its few real users) or
accepting a short explained outage.
