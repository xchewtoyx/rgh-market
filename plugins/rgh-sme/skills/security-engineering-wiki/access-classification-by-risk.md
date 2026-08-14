---
type: concept
title: Access Classification by Risk
description: >
  Classify data and actions by the damage inappropriate access could cause,
  so controls can be proportionate instead of all-or-nothing.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Access Classification by Risk

Not all data or actions are created equal, so protecting everything to the
same degree either over-burdens low-risk work or under-protects the crown
jewels. Before choosing controls, classify access by impact, security risk,
and criticality — public data vs. company data vs. user data vs.
cryptographic secrets; read APIs vs. admin APIs that can delete data.

A minimal scheme might be *public* / *sensitive* / *highly sensitive*, with
each cell of {classification} x {read, write, infrastructure access} rated
low/medium/high risk. Two structural points from that exercise:

- **Infrastructure (administrative) access is high risk at every
  classification level** — the ability to bypass normal access controls,
  reduce logging, change encryption requirements, SSH directly to a
  machine, or reconfigure a service threatens both availability and
  confidentiality regardless of the data class.
- **Read access can be as damaging as write access.** Reliability thinking
  starts with "who can shut things down or misconfigure them," but overly
  broad read permissions are how mass data breaches happen. Rate them on
  their own scale.

The classification framework should be clearly defined, consistently
applied, and broadly understood, so teams can design services that "speak"
it. It can be as light as two or three ad hoc labels or as heavy as a
programmatic central inventory of APIs and data types — sized to the
system's complexity, but covering its most important entities.

The classification then drives which controls apply where: standing group
ACLs for low risk, [temporary access](temporary-access.md),
[multi-party authorization](multi-party-authorization.md), or
[three-factor authorization](three-factor-authorization.md) as risk rises,
with "no permanent access" the appropriate ceiling for the most sensitive
classes. This is how [least privilege](least-privilege.md) stays affordable:
you spend control-complexity only where the risk justifies it.
