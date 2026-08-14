---
type: concept
title: Identities for Active Entities
description: >
  Every human, machine, and workload interacting in a system needs a
  meaningful identity — understandable, spoofing-resistant, never reused —
  as the foundation of access control and auditing.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 6"
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

# Identities for Active Entities

An identity is the set of attributes/identifiers relating to an entity;
credentials (passwords, X.509 certificates, OAuth2 tokens) assert it over
an authentication protocol. In a [digital-signature request
authentication](digital-signatures-for-request-authentication.md)
scheme, identity is not intrinsic (no fingerprints) — **an identity is
defined as anyone holding the credential that established it**. A new user
registers by submitting a public key; the server assigns an identifier and
stores the public key for signature verification. This replaces
username/password for origin proof: possession of the private key *is*
the identity check.

**The user must generate the keypair, not the server.** The private key
must stay absolutely secret — there is no secondary verification step.
If the server generates the keypair, [nonrepudiation](nonrepudiation.md)
rests on the server's word that it did not retain a copy; transmitting a
private key over the network risks interception. Client-side generation
(e.g. `ssh-keygen` or platform crypto libraries exporting PEM keys) is a
design requirement, not an operational preference. *Active entities* are all humans, software,
and hardware that interact in the system — and in microservice
architectures most interactions are service-to-service with no human
involved, so **all** entities need identities, not just people. The
quality of every access-control and [auditing](audit-log-design.md)
decision rests on the relevance of these identities.

**IP addresses are not identities**: multiple services share hosts, ports
are reused or arbitrary, instances move across hosts, and IPs are
spoofable — firewall-rule-style identification doesn't model privilege in
a microservice system.

A meaningful identity must have:

- **Understandable identifiers** — `widget-store-frontend-prod`, not
  `24245223`. Humans spot mistakes (and malice) in ACLs of readable names
  far more easily; still check look-alike identifiers when granting.
- **Robustness against spoofing** — a bearer token over cleartext is
  trivially spoofed; a TPM-backed certificate key in a TLS session is
  not.
- **Non-reusable identifiers** — a new hire assigned a departed
  administrator's old email address inherits their privileges.

One organization-wide identity system beats competing global/local
systems: everyone speaks the same language about entities, aiding
[understandability](design-for-understandability.md). (Externalizing
identity via OIDC providers trades that simplicity against trust in the
provider.)

**Google's production model** distinguishes: *administrators* (humans who
mutate system state — the root of all interactions; every action
traceable back to one for accountability, managed via directory/SSO and
group management); *machines* (global inventory, DNS-addressable, machine
identity tied to the admin groups who control its software); *workloads*
(scheduled by orchestration, identity chosen by an authorized requester —
the orchestrator enforces who may schedule *as* whom and on which
machines; workloads shouldn't have root on their hosts); and *customers*
(separate subsystem, used whenever a service acts on a customer's
behalf — see the end-user context ticket in
[trusted computing base](trusted-computing-base.md)).

**Authentication should be an abstraction developers consume, not build.**
Systems like ALTS (or Istio's security model) give zero-config
service-to-service authentication and transport security: an application
simply *runs as* a meaningful identity (admin tool as the administrator;
privileged machine process as the machine; deployed workload as
`myservice-frontend-prod`), and an API returns authenticated peer
information for access control. Without a systematic approach — each team
choosing credential types ad hoc — verifying authentication means reading
all application code, which doesn't scale and will be partly wrong.
[Role separation](role-separation.md) builds directly on these workload
identities.
