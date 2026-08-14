---
type: concept
title: Request Authentication Properties
description: >
  Honoring an inbound API request requires three separable guarantees —
  origin, integrity, and nonrepudiation — not merely verifying who logged
  in once at session start.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

# Request Authentication Properties

Deciding whether to honor an inbound API request is binary (yes or no),
but resolving it requires three **separate** properties — not one
"authenticated" flag.

**Origin** establishes *which user* sent the request: if a request
claims to come from user 1234, it must carry proof only the party
registered as user 1234 could supply. This is the
[identity](system-identities.md) question — distinct from
[authorization](authorization-policy-framework.md), which decides what
that identity may do after origin is established.

**Integrity** means the request content as received is exactly what was
sent. Origin alone is insufficient: a verified sender's payload could
still have been altered in transit (faulty networking or a malicious
middlebox). [Integrity in the CIA triad](cia-triad.md) applies here at
the message level. Relying on transport-layer security (TLS) alone means
trusting the channel rather than the request bytes themselves — TLS
protects the connection, not a canonical representation an verifier can
recompute independently.

**Nonrepudiation** means that once origin is verified, that origin
cannot later credibly deny having sent the request. See
[nonrepudiation](nonrepudiation.md) for the full dispute-evidence
claim; at the request-authentication layer the subtlety is *symmetric*
credentials: if the same secret both proves identity to the server and
lets the server forge requests as that user, a disinterested third party
cannot distinguish a genuine user request from one the server minted
with its copy of the shared secret. Nonrepudiation therefore requires
**asymmetric** credentials — different material held by each party for
signing versus verifying.

These three properties compose: origin without integrity leaves content
tamperable; origin and integrity without nonrepudiation leave disputes
resting on the server's word. [Digital signatures for request
authentication](digital-signatures-for-request-authentication.md)
satisfy all three when implemented with per-request signing rather than
a reusable [session token](session-token-security.md).
