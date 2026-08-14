---
type: concept
title: Fencing Tokens
description: >
  Attach a monotonically increasing generation number to every grant of
  authority so receivers can reject actions from an actor whose authority
  was already revoked elsewhere — no synchronized clock required.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 11, Generation Clock"
  - title: Site Reliability Engineering
    resource:
      "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 23,
      Managing Critical State"
---

# Fencing Tokens

A process holding authority — leadership of a cluster, a lock, a lease —
can be paused (a GC pause, a network partition) without crashing. While
it's unreachable, the rest of the system may reasonably conclude it's
dead and hand that authority to someone else. When the paused process
wakes up, it still *believes* it holds the authority it had before, and
will keep acting on that belief unless something stops it. If a
downstream system trusts the actor's self-report of its own authority
instead of independently verifying it, the actor's stale belief becomes
the downstream system's problem too: it honors a request from a party
whose privilege was already revoked elsewhere, simply because nothing
forced it to check.

**The fix**: attach a monotonically increasing generation number (also
called a term, epoch, or fencing token) to every grant of authority, bump
it every time authority changes hands, and stamp it on every message and
persisted record the authority-holder produces afterward. A receiver
rejects any message carrying a lower generation than the highest it has
already observed, and an actor that gets rejected this way learns
immediately that it has been deposed and must stop acting. Comparing two
integers requires no synchronized clock — the technique is a direct
application of Lamport timestamps (each participant tracks
`max(own, received)` and advances on every message), which is what makes
it robust to exactly the clock and scheduling problems
([avoid wall-clock dependencies](avoid-wall-clock-dependencies.md)) that
created the stale-authority hazard in the first place.

The security property this buys is not "the paused process can't act" —
it still can, briefly, in isolation — it's that **every other participant
in the system is structurally incapable of accepting what it says**,
which is what actually bounds the blast radius. This is the same shape as
[explicit revocation mechanisms](explicit-revocation.md): the defense
isn't preventing a compromised or stale actor from trying, it's making
sure every party the actor could talk to independently enforces the
current state rather than trusting the actor's claim about itself.

Where this generalizes beyond leader election: any design where a
long-lived credential or session token can outlive the authority it was
issued under needs the equivalent check — a version or generation
attached to the grant, verified by the receiver, not asserted by the
holder. Systems that skip this and serve requests (particularly reads)
without re-confirming current authority reintroduce the exact hazard
fencing tokens exist to close — a stale leader silently answering a
request as if it were still authoritative, invisible to the client that
asked.
