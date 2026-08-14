---
type: concept
title: Debugging Versus Security Investigation
description: >
  Debugging is code-focused; a security investigation pivots to the
  adversary — and normal debugging moves can destroy evidence or tip off
  an attacker, so recognize the signs of compromise and escalate early.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 15"
---

# Debugging Versus Security Investigation

A bug investigation asks what the *system* did: what data was sent, what
happened to it, how the service diverged from intent. A security
investigation quickly pivots to the *adversary*: what has the user who
submitted that job been doing, what else are they responsible for, is
there a live attacker, what will they do next? Different people too —
any engineer should debug; trained security/forensic specialists should
investigate compromises.

**Standard debugging moves become hazards** once compromise is possible.
Deleting odd files "to fix errant behavior" has deleted attacker
implants — alerting the attacker, who in one case responded by
destroying the entire system (see
[incident OpSec](incident-operational-security.md)). Adding code or
deprecating systems mid-investigation has side effects. Also keep an
access log of investigator actions from the start: you may later need to
prove — possibly in court — which actions were the attacker's and which
were yours.

**Recognizing a compromise** — oddities that individually are just bugs
but in accumulation suggest tampering:

- Logs or data needed for debugging are missing, truncated, or corrupted.
- Your hypothesis has drifted from system behavior to the actions of *an
  account or user*.
- Behavior inexplicable as accident (the web server "crashes" into
  interactive shells).
- Files abnormal for their type (a 1 GB `rick_roll.gif` with TAR
  headers), deliberately hidden, or camouflaged with near-familiar names
  (`explore.exe`).

**When to escalate**: engineers hesitate to "make a scene" before proof,
but investigating to the point of proof may be exactly wrong. Horses vs.
zebras: most bugs are just bugs — while staying alert for stripes. The
moment you genuinely suspect compromise is the moment to bring in
security professionals and the
[crisis-management](security-crisis-management.md) process; urgency,
legal involvement, and operational-security constraints all change at
that point.

Two supporting habits from the debugging side that serve security:
know your system's *normal* (baselines filter routine noise — SSH
brute-force chatter, typo'd passwords, port scans — and even Chrome's
deliberate random-domain DNS probes have been mistaken for malware C2),
and fight normalized deviance (long-tolerated weirdness hides both bugs
and attackers — rotate fresh eyes in, listen to newcomers, use red
teams). And sometimes the right fix for an unmaintained, possibly
compromised legacy system is deletion — replacing it with something
simpler improved posture in real cases where new team members didn't
know the system existed.
