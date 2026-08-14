---
type: concept
title: Root Key Isolation
description: >
  Keep a long-lived trust root offline and behind multi-party physical
  controls, do day-to-day signing with online intermediates, and pre-stage
  alternate roots across the ecosystem so a root compromise doesn't become
  unrecoverable.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 11"
---

# Root Key Isolation

Some keys anchor trust for years and are extraordinarily expensive to
rotate — a certificate authority's root key, or any key whose public half
is distributed broadly enough (browsers, operating systems, devices) that
[credential rotation](credential-rotation.md) can take years rather than
days. Theft or misuse of that key is the most severe risk the system
faces, and the usual rotation playbook — reissue and revoke — is too slow
to be a real mitigation.

The pattern that contains this risk:

- **Keep the root itself offline**, behind multiple layers of physical
  protection that each require [multi-party authorization](multi-party-authorization.md)
  to pass. The root signs almost nothing directly.
- **Use online intermediate keys for day-to-day operation.** Intermediates
  do the actual signing; if one is compromised, revoke and reissue it
  without touching the root — an application of
  [compartmentalization](compartmentalization.md) to key material, trading
  the intermediate as the sacrificial layer.
- **Pre-stage alternate roots across the ecosystem before you need them.**
  Getting a new root broadly trusted (embedded in browsers, operating
  systems, hardware) can take years, so a root compromise discovered after
  the fact leaves no fast path to a clean replacement. Distributing backup
  root material to the same relying parties ahead of time — even though
  it's unused — means you can swap to it immediately if the primary root
  is ever compromised or must be retired.

This is [credential rotation](credential-rotation.md) applied to a key
whose rotation cost is measured in years rather than a maintenance window:
since you can't rely on rotating your way out of a compromise, you instead
minimize the chance the root is ever touched (offline, intermediates
absorb operational exposure) and pre-pay the recovery cost (alternate
roots already staged) so the one rotation you can't do quickly is a
rotation you'll rarely need.
