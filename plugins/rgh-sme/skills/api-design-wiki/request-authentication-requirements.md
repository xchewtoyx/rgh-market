---
type: concept
title: Request Authentication Requirements
description: >
  Three wire-level properties — origin, integrity, and nonrepudiation — that
  message authentication must satisfy beyond a binary allow/deny decision.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

Honoring a request is yes/no, but verification must establish three properties:

- **Origin** — which registered user sent the request; proof must be something
  only that party could supply after [public key registration](public-key-registration.md).
- **Integrity** — bytes received match bytes sent; tampering in transit must
  invalidate proof even when transport encryption alone would hide corruption
  from application-level checks.
- **Nonrepudiation** — after origin is proven, the sender cannot credibly deny
  sending the request. Requires **asymmetric** credentials: the prover's secret
  must not be shared with the API server, or the server could forge user traffic
  and third parties could not distinguish genuine from server-originated calls.

## Symmetric versus asymmetric proof

Shared-secret and HMAC schemes satisfy origin and integrity for many two-party
APIs but fail nonrepudiation when a disinterested verifier must trust the
signature — server and client hold the same secret.

**Digital signatures** use a keypair: only the private key generates signatures;
anyone with the public key verifies. That yields origin (holder of private key),
integrity (signature binds message bytes via a [request fingerprint](request-fingerprint.md)),
and nonrepudiation (only one party generates valid signatures).

Flow: client generates a keypair, registers the public key at account create,
signs each request, server verifies with stored public key — wire details in
[signature header](signature-header.md). Lighter identification without integrity
proof uses [API key as message element](api-key-as-message-element.md) over TLS;
three-party delegation belongs to OAuth-style protocols outside this bundle's
depth.

Threat modelling and credential lifecycle belong to security engineering; this
note covers **where and how** proof sits in the message contract.
