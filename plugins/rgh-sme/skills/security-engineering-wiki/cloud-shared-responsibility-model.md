---
type: concept
title: Cloud Shared Responsibility Model
description: >
  The cloud provider secures the physical infrastructure; the customer
  secures everything built on top — and most cloud breaches trace to
  customer-side misconfiguration, not provider failure.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 10"
---

# Cloud Shared Responsibility Model

Renting cloud infrastructure splits security responsibility along a fixed
line: the vendor secures the physical data center, hardware, and the
underlying platform; you secure the applications, configuration, and data
you run on top of it. This division doesn't reduce your total exposure —
it relocates most of it to the customer side. In practice, most cloud
security breaches are caused by end users, not the cloud provider —
driven by misconfiguration, oversight, and sloppiness on the customer
side (a public storage bucket, an instance with unrestricted inbound
access — see
[network exposure misconfiguration](network-exposure-misconfiguration.md))
rather than a failure in vendor-operated infrastructure.

This is a distinct concern from
[cloud provider as a trust boundary](cloud-provider-trust-boundary.md),
which is about the risk the *provider's own* staff, hardware disposal, and
legal exposure add to your threat model. Shared responsibility is about
the complementary risk on your own side of that boundary: the provider
being trustworthy does not protect you from your own misconfiguration, and
statistically, misconfiguration is where the actual breaches happen.

One structural reason the cloud can still be the safer default despite
this: cloud platforms generally implement something closer to
[zero trust](zero-trust-networking.md) — every action requires
authentication rather than trusting a network perimeter — and let a
customer leverage the provider's own large security engineering
workforce for the infrastructure layer. A hardened, air-gapped perimeter
(the extreme opposite of zero trust) still has legitimate uses for the
most sensitive systems, but even a fully air-gapped system remains
vulnerable to human security failure — the shared responsibility line
never moves entirely off the customer.
