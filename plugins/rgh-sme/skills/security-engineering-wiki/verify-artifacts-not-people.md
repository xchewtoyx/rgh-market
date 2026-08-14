---
type: concept
title: Verify Artifacts, Not Just People
description: >
  A deployment control that checks who requested a change can be bypassed
  by a mistaken or compromised insider; the environment being changed must
  instead verify properties of the change itself.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 14"
---

# Verify Artifacts, Not Just People

Controls placed earlier in a pipeline — code review, tests, an approval
gate — have no effect on a change that reaches the target system by some
other path. It is not enough to verify *who* initiated a deployment or
configuration change, because that person may be mistaken, or may be an
attacker wearing a legitimate insider's credentials
([insider risk](insider-risk.md)). The environment receiving the change
must instead independently verify *what* is being deployed against the
properties you actually require — that it passed review, came from the
right source, passed tests — rather than trusting that it must be fine
because an authorized identity presented it.

This is why the receiving environment itself must be a
[choke point](trust-segmentation.md) that every change is forced through,
and why the check belongs there rather than solely in the tooling that
produces the change: a control an adversary can route around by talking
directly to the target isn't a control on the target, only on the well-behaved
path. The deep technique for building this — signed build provenance,
policy engines that evaluate it, admission controllers — is a delivery-
pipeline concern; what belongs here is the design principle and the threat
it answers.

**Configuration is not exempt.** A configuration change (a backend pointer,
an ACL, a feature flag) can cause exactly the same damage as a code change,
so it needs the same rigor: checked into version control, peer reviewed,
and — where the receiving environment can arrange it — verified the same
way as code, not pushed by a human with standing access. Treating
configuration as a second-class, unreviewed change path is a common way
this principle quietly fails in practice; see
[security design review](security-design-review.md) for building that
expectation into the design phase rather than discovering the gap during
an incident.

**The principle has a designed escape hatch and a bound on it.** An
environment that only ever accepts verified artifacts cannot respond to an
emergency that needs a change no verified pipeline can produce in time —
that gap is exactly what [breakglass](breakglass.md) exists for, and why
breakglass use must be rare, alarmed, and audited: it is the one path
where "who" substitutes for "what" by design, and its safety depends on
that substitution staying visible and exceptional.
