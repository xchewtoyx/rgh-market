---
type: concept
title: Encryption as a Baseline Control
description: >
  Encryption at rest and in transit is a necessary floor against basic
  interception and physical theft, not a substitute for access control —
  it protects nothing once credentials or the underlying storage are
  already exposed.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 10"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 9"
---

# Encryption as a Baseline Control

Encryption is not "a magic bullet": it does little to stop a breach where
credentials or access were already compromised at the human level — an
attacker holding valid credentials reads data through the same encrypted
channel a legitimate user would. What it does reliably provide is a
baseline defense against comparatively unsophisticated attacks — network
traffic interception, or a stolen laptop's disk being read directly.

- **At rest**: full-disk encryption on end-user devices protects data if
  the device is lost or stolen; server-side encryption across storage,
  databases, and object storage protects the equivalent scenario for
  infrastructure; application-level encryption layered on top of both
  protects against a flaw in any one layer's implementation (the same
  logic as [defense in depth](defense-in-depth.md)'s independent
  encryption layers).
- **In transit**: modern protocols default to encryption (HTTPS is
  effectively mandatory for cloud APIs today); avoid legacy unencrypted
  protocols like FTP entirely, since they're trivially vulnerable to
  interception and tampering even for data that's "public" in principle.
  Trace encryption to where it actually ends: a third-party CDN or edge
  proxy terminating TLS on the client's behalf can leave an unencrypted
  hop from there to the origin server unless the origin connection is
  separately encrypted — "the site is HTTPS" is a claim about the client
  leg only, not proof the whole path is protected.

Two failure modes matter more than the encryption algorithm itself.
First, **key handling** is a more common source of real data leaks than
weak ciphers — see
[secure cryptographic APIs](secure-cryptographic-apis.md) for how to keep
key material out of code and hands that don't need it, and
[credential and key rotation](credential-rotation.md) for limiting how
long a leaked key stays useful. Second, encryption in transit says
nothing about what's on the other end: HTTPS to a storage bucket that is
itself configured for public read access still exposes the data — see
[network exposure misconfiguration](network-exposure-misconfiguration.md).
Treat encryption as one necessary layer among several, never as the layer
that makes the others optional.

**Key scope should match compartment scope.** A single encryption key
covering an entire database gives that one key the same blast radius as
the whole dataset — compromise it once and everything it protects is
exposed at once. Prefer scoping keys to
[compartments](compartmentalization.md) (per security group, per tenant,
per data classification) so a compromised key exposes only its own
compartment's data, the same logic
[root key isolation](root-key-isolation.md) applies to a trust root: the
more broadly a key's blast radius reaches, the more that key itself needs
isolating.
