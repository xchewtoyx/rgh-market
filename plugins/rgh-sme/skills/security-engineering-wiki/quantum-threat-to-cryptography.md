---
type: concept
title: Quantum Threat to Cryptography
description: >
  Quantum algorithms don't just make attacks faster — Shor's algorithm
  breaks the math behind asymmetric encryption outright, while Grover's
  algorithm halves the effective strength of hashes and symmetric keys.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 26"
---

# Quantum Threat to Cryptography

Most deployed asymmetric encryption relies on a classical asymmetry: given
two large prime numbers, computing their product is easy, but factoring
that product back into the primes is classically infeasible. **Shor's
algorithm** breaks this asymmetry — a sufficiently powerful quantum
computer factors such a product in time polynomial in the bit-length of
the primes, rather than the exponential time classical computers need.
This isn't a speedup on the existing attack; it eliminates the hardness
assumption the whole scheme depends on. Every system relying on that
class of asymmetric cryptography for confidentiality or authentication is
affected, once the hardware exists.

**Grover's algorithm** hits hashes and symmetric keys differently: it's a
quadratic speedup on brute-force inversion, meaning a quantum attacker
needs roughly the square root of the classical work — inverting a 256-bit
hash takes on the order of 2^128 quantum iterations, not the 2^256
classical ones. This halves the *effective* bit strength of a hash or
symmetric key rather than breaking it outright; the standard mitigation is
doubling key/output length, not switching algorithm families.

**Why this belongs in design now, not when the hardware arrives.** Data
encrypted today with a Shor-vulnerable scheme can be captured and stored
by an adversary now, then decrypted retroactively once quantum hardware
catches up — a "harvest now, decrypt later" threat that only matters for
data with a long confidentiality lifetime, but for that data the migration
deadline is effectively already in the past. Protocol migrations
historically take decades (NIST is reportedly exploring quantum-resistant
transport protocols years ahead of need for exactly this reason), so
[credential and key rotation](credential-rotation.md)'s cryptographic-
agility payoff — the proven, exercised ability to swap primitives without
a system rewrite — is the concrete design property that makes this threat
survivable instead of an eventual forced emergency migration. This is the
sharpest current instance of [designing for a changing
landscape](design-for-changing-landscape.md): the landscape change is
predictable in direction, uncertain only in timing.

Practical posture: inventory which systems and stored data rely on
Shor-vulnerable asymmetric schemes and how long that data must stay
confidential; track NIST's post-quantum cryptography standardization for
migration targets; and treat "can this system's crypto primitives be
swapped without a rewrite" as a [security design
review](security-design-review.md) question for anything with a multi-year
confidentiality horizon, not just a future concern to revisit later.
