---
type: concept
title: Multi-Party Authorization (MPA)
description: >
  Requiring a second person to approve a sensitive action prevents
  mistakes, deters and detects insiders, and raises an external attacker's
  cost to compromising two people.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Multi-Party Authorization (MPA)

MPA requires approval from another person before a sensitive action
executes. Its benefits stack: it prevents unilateral mistakes and policy
violations; it discourages bad actors (insiders risk discipline, external
attackers risk detection); it raises attack cost to compromising at least
one more person or crafting a change that survives peer review; recorded
tamper-resistant approvals support later incident response; and it lets you
tell customers that no single person can act alone.

**Granularity matters.** MPA over a broad grant (approval to join a
production-access group, or to assume a role) is a useful
[breakglass](breakglass.md)-adjacent control for unforeseen actions — but
the approver is endorsing a capability, not an action. Approval of a
specific call against a [small functional API](small-functional-apis.md)
lets the approver know precisely what they are authorizing, which is a far
stronger guarantee. Where possible, prefer the granular form.

Pitfalls to design against:

- **Context-starved approvers.** The prompt must clearly identify who is
  doing what — config parameters and targets included — especially on
  mobile screens with limited space. An approval nobody can evaluate is a
  rubber stamp.
- **Social pressure.** An engineer may not feel able to reject a request
  from a manager, a senior engineer, or someone standing at their desk.
  Mitigate with after-the-fact escalation paths to a security team and
  independent audits of a sample of approvals. If the technology and
  social dynamics don't genuinely allow someone to say **no**, the system
  is of little value.
- **Productivity drag.** If finding an approver is too painful, users
  develop workarounds (see
  [structured justification](structured-justification.md) on generic
  justifications). Make approval easy to request and fast to grant.

Threat coverage: MPA protects against unilateral insider risk and against
compromise of a single workstation. It does *not* protect against broad
compromise of the homogeneous workstation fleet all approvers share — that
is what [three-factor authorization](three-factor-authorization.md)
addresses; combining 3FA from the originator with web-based MPA from a
second party covers both threat classes with modest overhead. A shared
[authorization framework](authorization-policy-framework.md) lets you roll
MPA out across all services with a library and config change rather than
per-service code.
