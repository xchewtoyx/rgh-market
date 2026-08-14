---
type: concept
title: "Hyrum's Law: Every Observable Behavior Will Be Depended On"
description: >
  With enough users of an interface, every observable behavior gets
  depended on by somebody regardless of what the documented contract
  promises — true, but it doesn't move where the documented contract
  boundary should actually sit.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman, with Cesare Pautasso), ch. 15 (Hyrum's Law, hyrumslaw.com)"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 3"
---

**Hyrum's Law**: "With a sufficient number of users of an interface, it
does not matter what you promise in the contract: all observable behaviors
of your system will be depended on by somebody." An interface's
[documentation](interface-documentation.md) deliberately discloses less
than everything an implementation actually does — everything observable
but undocumented is nominally an implementation detail actors use "at
their own risk." Hyrum's Law is the observation that, at sufficient scale,
"at their own risk" doesn't actually protect the implementer: enough
callers exist that *someone* will have noticed and started relying on an
undocumented timing quirk, an error message's exact wording, or the
iteration order of a collection that was never promised to be ordered.

This is true, but the correct response isn't to treat it as an argument
for documenting everything — that would just make every accidental
behavior a permanent commitment. The documented [interface
contract](module-interface-and-implementation.md) still marks the boundary
of what the implementer is actually obligated to preserve; Hyrum's Law is a
warning about the *practical* blast radius of changing something outside
that boundary, not a reason to move the boundary itself. It's the reason
[interface evolution techniques](interface-evolution-deprecation-versioning-extension.md)
matter even for changes that are, strictly by contract, "not breaking
anything": a change can be contract-compliant and still break real callers
who depended on an unpromised detail, and deprecation notice or versioning
is the practical mitigation regardless of whose fault the breakage
technically is.

**Entropy analogy**: Hyrum's Law can never be eradicated, but that does not
mean it cannot be understood, planned for, or mitigated — the same posture as
thermodynamics: entropy never decreases, yet efficiency still matters. Even
with excellent engineers and code review, perfect contract adherence by every
consumer cannot be assumed. Being explicit about interface promises buys
flexibility, but the real difficulty of a future change depends on how
*useful* users find some observable (even unpromised) behavior — the more
exploitable a side effect, the more likely someone depends on it. Given enough
time and users, even an innocuous change will break something; investigation
and repair cost must factor into any change's value analysis.

**Hash iteration order** is a canonical example: most programmers know hash
tables are unordered, but few know whether their runtime promises stable
iteration. Three pressures converge — hash-flooding DoS resistance (nondeterministic
iteration), algorithm improvements (order may change), and Hyrum's Law itself
(programmers *will* depend on order if the language permits). An expert's
short-lived-script answer ("probably fine") differs from a decades-long
codebase answer ("unsafe unless documented"). Dependencies can be **indirect**:
a library that serializes hash-container values into an RPC response causes
the *caller* to depend on iteration order even when the library author never
did. Some languages randomize hash order across versions or runs to discourage
such coupling — yet some code has used iteration order as a cheap random
source, so removing randomness later breaks those users too.

This separates "it works" from "it is correct" at engineering scale: depending
on unpromised order may never fail in a short-lived program, but eventually
efficiency, security, or data-structure evolution makes changing order
valuable — forcing a trade-off between that value and breaking dependents.

**Stylistic corollary**: code leaning on brittle, unpublished dependency
features tends to be called "hacky" or "clever"; code following published
practices and planning for change tends to be called "clean" or
"maintainable." Both styles have legitimate uses depending on expected
lifespan — "It's programming if 'clever' is a compliment, but it's software
engineering if 'clever' is an accusation."
