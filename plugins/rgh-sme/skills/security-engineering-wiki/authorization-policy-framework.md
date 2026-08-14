---
type: concept
title: Authorization Policy Framework
description: >
  Separate authentication from authorization, and pull authorization logic
  out of business code into a shared framework evaluating externally
  supplied policy.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 5, 6"
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 11"
---

# Authorization Policy Framework

Access control is two distinct steps. **Authentication** verifies the
identity of the caller — prefer reusing an existing strong cryptographic
mechanism (TLS, OAuth) over inventing one; its output is a *role*
(principal, username). **Authorization** then decides whether that role may
perform the requested action, potentially weighing: the specific action
(URL, command, RPC method), its arguments, the request source (IP, client
cert metadata), role metadata (location, jurisdiction, risk score), and
server-side context (rate of similar requests, available capacity).

Authorization logic is hard to implement correctly, and complexity
compounds when every service hand-rolls its own. Instead, separate it from
API design and business logic with a policy framework (in the style of
cloud IAM offerings): code asks simple checks — "can X access resource
Y?" — evaluated against an externally supplied policy file. Adding a
control to an action then becomes a policy-config change, not a code
change.

A *widely shared* framework has outsized leverage:

- Support for [MPA](multi-party-authorization.md) or
  [3FA](three-factor-authorization.md) can be added to **all** service
  endpoints with a single library change, then enabled for a subset of
  actions with a single config change.
- Uniformity aids team mobility — everyone knows how access controls are
  implemented — and lets reliability piggyback: requiring MPA for unsafe
  actions gives review-like protection with faster incident response than
  waiting on code review.

Pitfalls:

- **Policy-language Goldilocks problem.** Too simplistic, and authorization
  decisions leak back into the codebase; too general, and nobody can
  reason about the policy. Iterate carefully between the extremes.
- **Policy distribution.** The policy becomes one of the most
  security-sensitive pieces of configuration and usually must be updatable
  independently of the binary — its distribution deserves the same care as
  any privileged config push (see
  [small functional APIs](small-functional-apis.md) and
  [trust segmentation](trust-segmentation.md)).
- **Developers need help.** Encoding the right policy takes collaboration
  between the application developers who own the admin APIs and security
  engineers/SREs who know the production environment; expressiveness alone
  doesn't produce the right balance of security and functionality.

Frameworks also absorb inherently complex cases individual teams would
each botch — e.g. a request chain ingress → frontend → backend acting for
an authenticated customer, where policy must express which workload
identity may retrieve data on whose authority (see
[identities for active entities](system-identities.md) and the end-user
context ticket in [trusted computing base](trusted-computing-base.md)).
Declarative, unified policies additionally enable tooling that evaluates
the security exposure of services and user data across the
infrastructure — impossible over ad hoc per-application authorization
code.

Plan the user-facing half too:
[diagnosing access denials](diagnosing-access-denials.md) determines
whether fine-grained policy is operable.

**The check must run against the actual object on every request, not
once at the entry point.** A page or URL being hard to guess is not an
authorization control — it's an assumption that fails the moment the
identifier leaks (a shared link, a referer header, sequential IDs) or is
simply enumerated. The concrete failure this produces, sometimes named
insecure direct object reference: a request carries an object identifier
supplied by the client (an order ID, an account number) and the backend
fetches or mutates that object without independently checking whether the
authenticated caller is actually entitled to it — trusting that the
caller wouldn't have the ID unless they were supposed to. The fix is
structural, not defense-by-obscurity: every handler that accepts a
client-supplied object reference must run the authorization check against
that specific object and that specific caller, server-side, on every
request — never inferred from how the caller reached the page or what the
UI does or doesn't expose.
