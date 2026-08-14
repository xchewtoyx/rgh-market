---
type: concept
title: Three-Factor Authorization (3FA)
description: >
  Requiring approval of a risky request from a second, hardened platform
  (typically mobile) defends against broad compromise of the workstation
  fleet.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Three-Factor Authorization (3FA)

[Multi-party authorization](multi-party-authorization.md) has a structural
weakness in large organizations: all the "multiple parties" use the same
centrally managed workstations. The more homogeneous the fleet, the more
likely an attacker who compromises one workstation can compromise them
all — at which point requester and approver are both attacker-controlled.

3FA counters this by requiring, for very risky operations, cryptographically
signed approval from a **second, hardened platform**. In practice: RPCs may
only originate from managed desktop workstations, and when a production
service receives a sensitive RPC, the
[authorization policy framework](authorization-policy-framework.md) demands
signed confirmation from a separate 3FA service that the request was shown
to the originating user on their hardened mobile device and acknowledged
there.

Why mobile as the second platform: the classic alternative — maintaining a
separate trusted workstation per user just for production access — decays,
because users want full features on both machines and the duplicate
infrastructure stops being maintained once management attention moves on.
Mobile platforms are easier to harden and users tolerate restrictions there
(app allowlists, network monitoring, limited endpoints). The core is just
an RPC service that receives the request-to-authorize and exposes it to the
trusted client for approval.

Naming caveat: 3FA strengthens *authorization of a specific request*, not
*authentication of a user* — it is not 2FA/MFA, and the "3" is a shorthand
(it is approval from a second platform beyond your two authentication
factors).

Threat coverage: 3FA protects against broad internal-workstation
compromise but, used alone, gives **no** insider-threat protection — the
insider approves their own request on their own phone. Pair 3FA (originator)
with MPA (second person) for strong coverage of both, with relatively
little organizational overhead. Reserve 3FA for actions classified at the
highest risk tiers (see
[access classification](access-classification-by-risk.md)).
