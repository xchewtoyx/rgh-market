---
type: concept
title: Trusted Computing Base and Security Boundaries
description: >
  The set of components whose failure could breach a security policy;
  keeping it small, behind a boundary that trusts nothing crossing it, is
  what makes security properties verifiable.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 6"
---

# Trusted Computing Base and Security Boundaries

The trusted computing base (TCB) for a security policy is the set of
components — hardware, software, human — whose correct functioning is
sufficient to enforce the policy; equivalently, whose failure could breach
it. The TCB must uphold the policy even if everything *outside* it —
including the rest of your own system — misbehaves arbitrarily. The
interface between TCB and everything else is a **security boundary**;
whatever crosses it (IPC, packets, RPCs) must be treated with suspicion,
data and message-ordering alike.

**TCBs are per-policy and layered.** The OS kernel plus privileged
daemons form the TCB for inter-user process separation (resting on
hardware mechanisms like virtual memory); an application enforcing its
own document-sharing policy has its own TCB at that layer, in which the
unprivileged application code *is* included. A bug anywhere in the
relevant TCB can breach the policy — so a small TCB is both safer and
[understandable](design-for-understandability.md): you can reason about
its correctness in isolation. If a component's correctness depends on
assumptions outside its control, it isn't a TCB.

**Worked example — shrink the TCB by decomposition.** A monolithic
widget-store app (one server process, one database, all modules with full
DB access) makes the *entire* application the TCB for "only users can
access their own shipping addresses": SQL injection in catalog search, or
RCE anywhere in the server, exposes address data. Split into
microservices — frontend, catalog backend, purchasing backend, each with
its own database, all inter-service requests treated as untrusted — and
the TCB collapses to the purchasing backend plus its database: a
compromised catalog backend simply *can't* reach address data.

**Draw the boundary against the threat model, not around a box.**

- If the purchasing backend will hand *any* user's address to the
  frontend, the frontend is in the TCB — compromising it exposes
  everyone. Requiring an **end-user context ticket** (a short-term
  internal ticket minted by the central auth service from the user's
  external credential) with each request means a compromised frontend can
  at worst leak data of users active *during* the attack.
- In the *web* threat model, origins are the trust domains: if catalog UI
  and checkout share `https://widgets.example.com`, an XSS in catalog
  code can act on checkout — the whole frontend is back in the TCB.
  Serve checkout from its own origin (and ensure it isn't *also*
  reachable under the catalog origin) so same-origin policy becomes the
  boundary.

TCB decomposition is the security twin of
[compartmentalization](compartmentalization.md) (a TCB is often its own
failure domain), and small TCBs are what make
[security invariants](security-invariants.md) arguable with informal but
principled reasoning.
