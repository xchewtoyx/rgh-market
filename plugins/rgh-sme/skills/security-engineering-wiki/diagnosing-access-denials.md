---
type: concept
title: Diagnosing Access Denials
description: >
  Calibrate how much a denied caller learns to their privilege level, using
  opaque denial tokens to enable support and self-remediation without
  leaking policy.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Diagnosing Access Denials

Fine-grained [least privilege](least-privilege.md) enforcement means policy
is evaluated at multiple levels, so denials happen in complex ways. A
denial has three possible readings: correct (all is well); correct but
overridable via an advanced control such as
[multi-party authorization](multi-party-authorization.md); or believed
incorrect by the caller (recent group change, subtle policy change) —
producing a support ticket. In all three, the caller is blind to the
reason. How much should the system reveal?

Scale disclosure to the caller's privilege:

- **No/limited privilege**: a bare 403. Denial details can be exploited to
  map the system and probe for a way in.
- **Minimal privilege**: a **token associated with the denial** — opaque to
  the caller, but usable to invoke an advanced control for temporary
  access, or handed to the security-policy team so they can diagnose the
  exact decision without the caller learning the policy.
- **More privileged callers**: token *plus* remediation information (e.g.
  "requires membership of group G"), enabling self-service before invoking
  support.

The tension: too little disclosure overloads the support channel; too much
lets clients reverse-engineer the policy from denial responses and craft
requests that use it in unintended ways. Early in a
[zero trust](zero-trust-networking.md) rollout, start conservative — tokens
only, all clients through the support channel — and open up as confidence
grows.

For the failure mode where the *authorization system itself* is wrong and
mass-denying legitimate access, diagnosis isn't enough — that's what
[breakglass](breakglass.md) recovery is for.
