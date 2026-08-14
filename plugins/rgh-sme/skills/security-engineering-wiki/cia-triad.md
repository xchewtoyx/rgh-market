---
type: concept
title: CIA Triad Through the Reliability Lens
description: >
  Confidentiality, integrity, and availability can each be breached with
  no adversary at all — a reliability flaw and an attack can produce the
  same loss, so both lenses must guard the same properties.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 1"
---

# CIA Triad Through the Reliability Lens

Confidentiality, integrity, and availability (the CIA triad) are the
classic attributes of secure systems, but security and reliability view
the same three properties through different lenses — the difference being
the [presence of a malicious
adversary](security-reliability-intersection.md). Each property can be
lost purely through reliability failure:

- **Confidentiality**: a push-to-talk microphone stuck in transmit
  broadcasts private cockpit conversation — a hardware reliability flaw,
  no adversary, genuine confidentiality breach. (A buggy chat system that
  misdelivers messages is the software equivalent.)
- **Integrity**: cryptographic end-to-end integrity checks at Google
  caught data corruption that turned out to be single-bit flips from
  uncorrectable memory errors; SREs recovered everything by brute-forcing
  the one-bit-flip space against the original checksums — a security
  technique rescuing a reliability incident. (Noncryptographic checks
  existed but hadn't caught it.)
- **Availability**: an adversary can halt a system via an exploited weak
  spot or a botnet DDoS — but from the victim's seat, a malicious flood, a
  design flaw (a software update making devices spike traffic in
  synchrony), and a legitimate stampede (an earthquake triggering
  near-identical queries region-wide) are often indistinguishable.

Design consequences: mechanisms that protect a property should work
regardless of cause — end-to-end integrity checking catches both bit rot
and tampering, and [DoS defenses](dos-defense-in-depth.md) must absorb
success-disasters and attacks alike. Conversely, a "mere reliability bug"
in a path that touches confidential data *is* a security issue; triage it
as both.
