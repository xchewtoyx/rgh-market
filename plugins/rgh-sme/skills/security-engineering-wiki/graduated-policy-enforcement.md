---
type: concept
title: Graduated Policy Enforcement
description: >
  Automated policy checks shouldn't all respond the same way to a
  violation — tier enforcement by risk into hard blocks, override-with-
  approval, and advisory-only, so proportionate control doesn't collapse
  into either universal strictness or universal noise.
sources:
  - title: Infrastructure as Code, Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Wang), ch. 8"
---

# Graduated Policy Enforcement

An automated policy engine that evaluates every change against security
and compliance rules faces a design choice that matters as much as the
rules themselves: what happens when a rule is violated? Treating every
violation identically forces a bad trade-off — block everything and
legitimate, well-understood exceptions grind through the same friction as
genuine mistakes (which teaches people to route around the checker
entirely), or warn on everything and the signal that actually matters
gets lost in noise nobody reads. A three-tier response scales enforcement
to the risk each rule actually protects against:

- **Hard mandatory** — violations that block automatically with no
  override path: the kind of misconfiguration that has essentially no
  legitimate justification (a database provisioned with public internet
  access, storage created unencrypted). No approver should be able to
  wave this through, because there's no scenario where doing so is
  correct.
- **Soft mandatory** — violations that block by default but carry an
  explicit override path requiring a second party's sign-off (opening a
  port to `0.0.0.0/0` on a load balancer that occasionally does need to be
  public). This is [multi-party authorization](multi-party-authorization.md)
  applied to policy violations instead of production actions: the rule
  encodes the default risk judgment, and a human with the missing context
  can consciously override it, with that override itself recorded as
  part of the change's [audit trail](audit-log-design.md) rather than
  silently bypassing the check.
- **Advisory** — recommendations that surface without blocking anything
  (an outdated TLS cipher suite, a stale machine image). These exist to
  inform, not gate, and mixing them into a blocking tier is how a policy
  engine trains people to stop reading its output.

**Assigning a rule to a tier is a [risk-classification](access-classification-by-risk.md)
decision, not a policy-engine implementation detail** — the same judgment
that decides how much control a given class of access deserves decides
how much friction a given class of violation deserves before it ships.
Getting the tier wrong in either direction reproduces a familiar failure:
over-tier everything into hard mandatory and legitimate exceptions
pressure teams to weaken or bypass the checker altogether (the same
dynamic behind [the cultural cost of compliance
controls](compliance-control-cultural-cost.md)); under-tier a rule that
actually matters into advisory and a real risk ships with nothing more
than an ignored warning attached.
