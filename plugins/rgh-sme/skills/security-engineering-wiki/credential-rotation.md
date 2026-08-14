---
type: concept
title: Credential and Key Rotation
description: >
  Rotating and expiring keys and credentials limits an adversary's window,
  forces re-theft that creates detection opportunities, and must itself be
  exercised and measured or it will fail when urgently needed.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
---

# Credential and Key Rotation

Time is the third [compartmentalization](compartmentalization.md)
dimension. An adversary who stole a key or credential keeps that access
only until rotation: to persist they must maintain presence and reacquire
the new secret — each theft another detection opportunity — and routine
security hygiene (patching the original hole) may cut them off entirely
even if the theft is never detected.

**The reliability tradeoff**: wall-clock expiration is dangerous if a
failure prevents rotating *to* new credentials before the old ones lapse —
you've scheduled your own outage. Balance rotation frequency against the
risk of downtime or data loss when the rotation mechanism fails.

**Rotate routinely so emergency rotation works.** A compromise will one
day demand a nonnegotiable emergency rotation; only regular practice makes
that survivable. If rotation is expensive, drive its cost down. TLS
certificates are the everyday instance of this argument: a manually
renewed certificate is a rotation cycle nobody practices until it lapses
and takes the service down, which is why automated renewal (e.g. short
90-day Let's Encrypt certificates renewed by a scheduled job well before
expiry) is worth building even where the underlying risk being mitigated —
certificate compromise — is rare; the automation earns its keep primarily
by removing "forgot to rotate" as an outage cause. Measure two outcomes
([continuous validation](continuous-validation.md)):

- **Rotation latency** — time for a full cycle. Measuring it reveals
  services that can't actually update their configuration (never designed
  for rotation, never tested, or newly broken), how long each service
  takes (a file change and restart, or a gradual worldwide rollout), and
  what else delays the cycle — rollbacks, change freezes for services out
  of error budget, rollouts serialized across failure domains.
- **Verified loss of access** — certainty the old key is useless.
  Proving all copies destroyed is hard; prefer demonstrating that *using*
  the old key fails, then destroy it. Failing that, deny-list (CRL)
  mechanisms, plus alerts if any ACL still references the old key's
  fingerprint.

Side benefit: practiced rotation is cryptographic agility — the proven
ability to swap encryption primitives when one is broken, a key part of
[designing for a changing landscape](design-for-changing-landscape.md).
Rotation infrastructure is also load-bearing for
[recovery](design-for-recovery.md), where rotating secrets is a standard
post-compromise step.

**When rotation itself is too slow**: some keys (a certificate authority's
root) are trusted so broadly that reissuing takes years, not a maintenance
window. See [root key isolation](root-key-isolation.md) for how to contain
that risk when rotation can't be your primary defense.

One common, avoidable trigger for emergency rotation: a secret committed
to version control in plaintext. See [secrets committed to version
control](secrets-in-version-control.md) for why encrypting or deleting it
afterward doesn't undo the exposure.
