---
type: concept
title: Nonrepudiation
description: >
  A guarantee that neither party to a recorded exchange can later
  credibly deny it happened, built from an audit trail plus cryptographic
  proof of authorship rather than audit logging alone.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 11"
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

# Nonrepudiation

Nonrepudiation means neither the sender nor the receiver of a message can
later deny the exchange took place — a buyer can't disown an order they
placed, an approver can't disown a sensitive action they authorized. It
is a stronger claim than an [audit log](audit-log-design.md) entry by
itself: a log record shows the system's own account of what happened, but
without cryptographic backing an insider with write access to the log (or
a dispute about whether the logged actor was really the person behind the
keyboard) can undermine that account. Nonrepudiation is typically realized with
[digital signatures for request
authentication](digital-signatures-for-request-authentication.md)
plus a trusted third party that can authenticate the signer, so the
proof doesn't rest solely on the system's own say-so.

The mechanism used to prove authorship must be **asymmetric**: if the
same shared secret both lets a user prove identity and lets the server
forge requests as that user, no outsider can tell a genuine user action
from one the operator minted. HMAC and other symmetric schemes therefore
fail [nonrepudiation as a request authentication
property](request-authentication-properties.md) whenever a third party
must verify origin — they remain appropriate only where the server alone
is the verifier.

This is what turns an audit trail from operational record-keeping into
evidence that holds up under dispute — relevant anywhere a
[multi-party authorization](multi-party-authorization.md) approval,
a signed [deployment artifact](verify-artifacts-not-people.md), or a
[breakglass](breakglass.md) action might later need to be attributed
with certainty, including to a party who has a motive to deny it.
