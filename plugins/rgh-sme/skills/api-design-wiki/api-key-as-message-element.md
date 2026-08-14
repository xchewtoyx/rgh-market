---
type: concept
title: API Key as Message Element
description: >
  A long-lived client token in the message for identification and billing
  without transmitting full account credentials on every call.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 6"
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

An **API key** identifies the calling client on each request — for
[rate limits](rate-limit.md), [pricing plans](pricing-plan-as-contract.md),
and access control — without reusing user account credentials that also gate
billing and administration.

**Forces addressed:** leaking account passwords on every call (Basic auth) is
high impact; keys **decouple** payer/admin roles from dev/ops teams — issue,
revoke, and rotate per client or location without touching the account. Balance
security vs adoption — lighter than SAML for many APIs; pair with HTTPS (or VPN
/ public-key crypto when TLS is impossible).

**Wire placement:** encode as a plain-string [atomic parameter](atomic-parameter.md)
— header or body preferred; query string is least preferred (keys leak into logs
and analytics). Example: `Authorization: Bearer <API_KEY>` (RFC 6750).

**Generation:** serial number padded with random data and signed/encrypted to
prevent guessing while guaranteeing uniqueness; or UUID-based (no serial sync in
distributed systems — still obfuscate because UUIDs are guessable). Optionally
pair with a **secret key** (never transmitted) to sign a request-content hash
alongside the key — see [request fingerprint](request-fingerprint.md) and AWS-style
signing.

**Limits:** a bare key is an identifier — it cannot carry expiration or scopes
in the token itself. **Not for three-party delegation** (user + provider + third
party acting on user's behalf without sharing credentials) — use OAuth 2.0 /
OpenID Connect instead. Not a complete security picture; complements RBAC/ABAC
after authentication.

Document header name, format, and rotation in the [API description](api-description.md).
[Experimental preview](experimental-preview.md) access may restrict keys to a
closed group.
