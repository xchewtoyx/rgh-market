---
type: concept
title: Safe Proxies
description: >
  A single audited entry point between administrators and production —
  enforcing ACLs, multi-party authorization, rate limits, and logging —
  retrofittable onto systems you can't modify.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 3"
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
---

# Safe Proxies

A safe proxy routes connections that would have gone directly to a target
system through an intermediary that enforces new security and reliability
controls — a way to make a *running* system safer without substantially
changing it. Clients talk only to the proxy; target systems are
configured to accept calls only from it. Policy ACLs specify which
application-layer RPCs each client role may execute; the proxy checks,
logs, and forwards.

What the single entry point buys:

- Fleet-wide **auditing** of every administrative operation
  ([audit log design](audit-log-design.md))
- A central enforcement point for
  [multi-party authorization](multi-party-authorization.md) on sensitive
  requests
- **Rate limiting** — restarts take effect gradually, bounding a
  mistake's blast radius
- Control over **closed-source third-party systems** you can't modify
- One place to keep adding security/reliability improvements

This is the machinery behind **Zero Touch Prod**: every production change
made by automation, prevalidated by software, or through audited
[breakglass](breakglass.md) — no direct human access. Google estimates
~13% of evaluated outages could have been prevented or mitigated by it —
the same controls serve [insider-risk](insider-risk.md) containment and
outage prevention.

**Tool Proxy** is the CLI instantiation: instead of tracking every
dangerous CLI tool, a proxy binary exposes a generic RPC that
forks/execs the specified command under policy. A policy names the tool,
allowed groups, and MPA approvers with unit tests inline (e.g.
`group:admin` may run `borg`, after `group:admin-leads` approval);
engineers just prepend `tool-proxy-cli --proxy_address ...`. Servers deny
direct administrative connections outside breakglass, so the proxy can't
be sidestepped.

Pitfalls to design against:

- Maintenance/operational cost; a **single point of failure** — run
  redundant instances, hold dependencies to SLAs with emergency contacts.
- The **policy config is itself error-prone** — provide secure-by-default
  templates or generated settings.
- The proxy is an attractive **central target** — it must forward the
  client's identity and execute *as the client*, never under a privileged
  proxy role, so owning the proxy grants little.
- **User resistance** — engineers want direct access; reduce friction and
  guarantee a breakglass path for emergencies.

A **bastion host** is the everyday network-layer instance of this same
pattern: an application database should never accept connections directly
from the internet, so a single locked-down host, reachable only from
specific IPs, sits between the internet and the database, and a client
opens an SSH tunnel to the bastion before connecting onward. It's a
narrower proxy than Zero Touch Prod's RPC-level enforcement (a network
choke point, not an audited, policy-evaluating one), but the underlying
move is identical: force every path to a sensitive backend through one
hardened, observable point instead of exposing the backend itself.

Expose the same external API as the target so the proxy is transparent to
users. For new systems, prefer building on
[frameworks with integrated logging and access control](secure-by-construction-frameworks.md);
the proxy is the cost-effective retrofit
([small functional APIs](small-functional-apis.md) achieved at the
network layer).
