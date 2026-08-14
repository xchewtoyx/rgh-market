---
type: concept
title: Security Invariants
description: >
  Properties that must hold for all possible system behaviors, no matter
  how the environment misbehaves — the form in which security assertions
  are stated and verified.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 6"
---

# Security Invariants

A system invariant is a property that is always true no matter how the
environment behaves or misbehaves — malicious requests, hardware
failures, arbitrary misuse. The *system* is fully responsible for
upholding it. Security assertions are invariant claims; if the system
allows any behavior violating the desired property, that's a
vulnerability, not an edge case.

Example invariants worth writing down for a design (note that reliability
and security ones sit naturally side by side):

- Only authenticated, authorized users can access the persistent data
  store.
- All operations on sensitive data are audit-logged per policy.
- All values from outside the trust boundary are validated or encoded
  before reaching injection-prone APIs (SQL, HTML).
- Backend query volume scales proportionally to frontend query volume
  (violated by retry storms without backoff — a self-inflicted DoS).
- If a backend misses its deadline, the frontend degrades gracefully.
- Overloaded components serve errors rather than crashing.
- A system receives RPCs only from, and sends only to, designated
  systems.

**Verification is a spectrum.** At one end, tests plus spot code-reading —
low confidence, since untested behavior harbors bugs (the persistence of
SQL injection, XSS, and buffer overflows on top-vulnerability lists is
the evidence; absence of evidence is not evidence of absence). At the
other, formal proof — a machine-checked microkernel proof took ~20
person-years; practical only for microkernels and cryptographic cores.
The practical middle ground: design explicitly for
[understandability](design-for-understandability.md) so that principled,
informal arguments give high confidence at reasonable cost — small
[TCBs](trusted-computing-base.md), centralized enforcement, and
[types that encode properties](safe-types.md) shrink what must be
reasoned about. Weigh verification effort against the harm a violation
would cause.
