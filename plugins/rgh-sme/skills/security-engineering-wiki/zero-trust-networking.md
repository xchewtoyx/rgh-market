---
type: concept
title: Zero Trust Networking
description: >
  Network location grants no privilege; access decisions combine user
  credentials and device credentials instead of trusting the corporate
  perimeter.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

# Zero Trust Networking

In a zero trust model, being *inside* the company network confers no
privileged access: plugging into a conference-room port grants nothing more
than connecting from the open internet. Access is granted from what the
system knows about the **user** (their credentials) and about the **device**
(its credentials and management state). Google implemented this at scale as
BeyondCorp.

Zero trust is the network-layer underpinning of
[least privilege](least-privilege.md): it removes the ambient authority
that a flat internal network otherwise hands to anyone (or any malware)
that gets a foothold inside the perimeter. A hardened perimeter's
implicit promise — everything inside is trusted because getting in is
hard — fails the moment any trusted human inside is compromised (phished
credentials, a coerced insider), which is exactly the scenario a
perimeter has no answer for once breached. Cloud infrastructure makes the
perimeter harder to even draw cleanly: a private network with no external
connectivity still has a management/control-plane API reachable from the
internet, since that's how the provider's own tooling manages the
account — there effectively is no fully air-gapped cloud boundary to
harden in the first place, which is a structural reason zero trust fits
cloud-native architecture better than perimeter thinking does.

Two operational consequences matter at design time:

- **Decision quality depends on data quality.** Every granular access
  decision is policy plus context — user role, group memberships, device
  attributes, API sensitivity. If the systems producing that context are
  low quality, the security decisions are wrong. Treat the pipelines
  feeding authorization context as security-critical.
- **You need a fallback for when the authorization system itself fails.**
  A bad policy push can mass-deny legitimate access. The
  [breakglass](breakglass.md) fallback for zero trust is, ironically,
  trusted network locations again — designated "panic rooms" whose extra
  *physical* access controls offset the trust placed back in connectivity.

Because denials happen at fine granularity across many layers, plan for
[diagnosing access denials](diagnosing-access-denials.md) from day one.
