---
type: concept
title: Secure-by-Construction Frameworks
description: >
  Common frameworks with built-in conformance checks and vulnerability-
  proof APIs make whole bug classes impossible in application code, and
  align security with developer productivity.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 4, 6, 12"
---

# Secure-by-Construction Frameworks

A shared application framework can take *full responsibility* for classes
of security and reliability concerns rather than merely defaulting to
safe settings. Google's internal microservices/web framework illustrates
the pattern:

- **Conformance checks** (static and dynamic) enforce practices in
  application code — e.g. only immutable types cross concurrent execution
  contexts (drastically fewer concurrency bugs), and isolation constraints
  between components (changes in one module can't easily break another).
- **API design plus conformance checks** prevent developers from
  *accidentally being able to introduce* common web vulnerability classes
  (OWASP Top 10-style) — beyond "secure by default" to actively ensuring
  no application on the framework carries those risks.
- Built-in monitoring, health checking, and SLA-aware deployment
  automation (releases stop when error budget is spent) come for free.

Why it works organizationally — the win-win: developers adopt the
framework because it automates chores and speeds daily work, *not*
because it's secure; security engineers and SREs get one common surface
to build on; security and production-readiness reviews collapse to "are
the builds green?" for the covered concern classes, freeing review time
for design-level issues; and fixes to the central framework propagate to
every application on rebuild.

**Application ("batteries-included") frameworks** take the idea further:
individual frameworks (RPC, authn, authz, monitoring, release) offer too
much flexibility, and engineers mis-assemble them — e.g. a developer
wires up RPC and authentication but forgets an authorization policy, and
the service "works fine" while any authenticated client in the fleet can
call it. An application framework provides a canonical, tested set of
subframeworks with safe defaults (no authorization policy → all callers
denied) covering dispatching and deadline propagation, input
sanitization, authn/authz/auditing, logging, health and monitoring,
quota, load balancing, deployments, testing, dashboards, and capacity —
one shared vocabulary across development, security, and SRE.

**RPC backend pattern.** Most backends need the same wrapper around
their request logic: logging, authentication, authorization, throttling.
An interceptor-chain framework (each interceptor with *before*/*after*
stages sharing a context object; errors short-circuit forward execution
but still run completed interceptors' *after* stages in reverse) gives
clean separation: the authentication interceptor does the crypto via a
specialized library and deposits verified caller info in the context; the
authorization interceptor just consults it; the framework exports error
and latency metrics, cancels requests that can't meet their deadline,
monitors hard dependencies (redirecting traffic when they fail), and
provides retry-with-exponential-backoff so no developer hand-rolls
cascading-failure-prone retry logic.

**Framework-level answers to the common vulnerability classes** (OWASP
Top 10-style): typed query builders for injection and hardened templates
for XSS ([safe types](safe-types.md)); well-tested authentication before
requests reach the application; distinct types plus enforced encryption
for sensitive data ([secure crypto APIs](secure-cryptographic-apis.md));
XML parsers with XXE disabled; handlers *required* to declare access
controls, with end-user credentials enforced at the backend;
secure-by-default configuration (no debug output in production, one flag
monitored off for public users); deserialization libraries built for
untrusted input (protocol buffers); popular, actively maintained
dependencies kept updated; and logging/monitoring in a low-level library
rather than ad hoc. Evaluate a framework's security posture before
adopting — and prefer reusing established solutions (never roll your own
crypto framework) over building.

This only happens when security and SRE collaborate on the framework from
the design phase — woven into the fabric, not bolted on. Manual review
still matters, but differently: reviewers can't hold whole-program
context or maintain vigilance over hundreds of templates; a strong review
culture instead pushes developers to structure code so its security and
reliability properties are *obvious to review*, with frameworks and
automation carrying the mechanical burden. It is the
clearest case of security aligning with
[sustained velocity](initial-vs-sustained-velocity.md): adherence costs
modest incremental effort, and in exchange whole vulnerability classes
stop appearing during ongoing development and maintenance.
