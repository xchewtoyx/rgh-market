---
type: concept
title: Session Token Security
description: >
  A session token is a bearer credential for the duration it's valid, so
  its unpredictability, expiration, and revocation on logout matter as
  much as the login check that issued it.
sources:
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 11"
---

# Session Token Security

Authenticating a user once and then trusting a session token for every
subsequent request only holds as a security boundary if the token itself
resists three failure modes:

- **Predictability.** A session token generated from a weak source (a
  sequential ID, a timestamp, a low-entropy random seed) can be guessed
  or brute-forced, which hands an attacker an authenticated session
  without ever touching the login check that was supposed to gate it.
  Tokens need cryptographically random generation with enough entropy
  that guessing is infeasible — the same underlying requirement as any
  other bearer credential.
- **Unbounded lifetime.** A token with no expiration, or an idle timeout
  long enough to be meaningless, stays valid indefinitely once issued —
  turning a single leaked token (a shared screen, a logged request, a
  stolen device) into standing access rather than a bounded exposure
  window. This is the same reasoning
  [temporary access](temporary-access.md) applies to authorization
  grants generally: bound the lifetime so a leak has a limited window
  instead of an unlimited one.
- **Client-side-only invalidation.** A logout that only deletes the
  token from the client (clearing a cookie, discarding local storage)
  leaves the token itself still valid server-side — anyone who captured
  it beforehand (a proxy log, a browser history sync, a shared device)
  can keep using it after the user believes they've logged out.
  Invalidation must be a server-side action: the server must maintain
  enough state to actively revoke a specific token, not merely rely on
  the client discarding its copy. This is the same underlying requirement
  as [explicit revocation mechanisms](explicit-revocation.md) at fleet
  scale — a credential the holder stopped presenting is not the same as a
  credential the issuer has stopped honoring, and only the latter is an
  actual security boundary.

These three properties compose with the authentication/authorization
split in the [authorization policy framework](authorization-policy-framework.md):
a strong token only bounds *how long* and *how guessably* a session can be
abused, not *what* the authenticated caller is allowed to do once
holding it — that remains a separate, per-request authorization decision.

Per-request [digital signatures](digital-signatures-for-request-authentication.md)
are an alternative boundary: each call carries its own cryptographic
[origin and integrity proof](request-authentication-properties.md)
rather than reusing a bearer token — stronger for
[nonrepudiation](nonrepudiation.md) but heavier to implement and verify.
