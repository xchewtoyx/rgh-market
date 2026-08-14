---
type: concept
title: Ejecting the Attacker
description: >
  Severing an attacker's access for good — timing the ejection, isolating
  or rebuilding compromised assets, sanitizing code and data, and rotating
  every credential and secret they may have touched.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 18"
---

# Ejecting the Attacker

The end goal of [recovery](security-incident-recovery.md): remove the
attacker, ensure they can't return, and leave the system stronger.

**Timing is a chess move.** Consensus practice: wait until you fully
understand the attack before ejecting, so the attacker can't watch your
mitigations and adapt — rebuilding six known-compromised systems while
the entry vector is unknown just tells a still-active attacker (watching
from a seventh) to destroy what's left, and an attacker in your chat or
email may *infer more than you know*. But apply it carefully: if the
attacker is actively exfiltrating or destroying, you may act early —
knowingly entering the game mid-board, with your checkmate steps planned.
Ejection must be near-simultaneous and complete; partial ejection burns
your knowledge for nothing.

**Isolate (quarantine)** compromised assets: file-level (antivirus
quarantine), host-level (disable the switch port or NIC), or whole
network segments. Zero-trust architectures
([BeyondCorp](zero-trust-networking.md)) amplify this — little inherent
trust between assets means natural isolation boundaries against lateral
movement and instantly revocable access. Isolation lets genuinely
irreplaceable compromised infrastructure stay online (a mission-critical
database on its own restricted network during weeks of rebuild) — but a
compromised asset left online is pernicious technical debt: people forget,
newcomers un-quarantine. Mark assets visibly (stickers), monitor a list of
quarantined MAC addresses for network reappearance, and verify permanent
remediation in the postmortem.

**Rebuild rather than delete malware.** Deleting known malware and moving
on gambles that you found *all* of it; reinstalling from known good
images is typically the right answer (down to BIOS/hardware for firmware
rootkits). Good design makes this cheap: hardware-verified boot means a
power cycle restores known-good; automated release systems and container
redeploys replace compromised instances with standard images
([intended state](intended-state-recovery.md)). Lacking version control
or standard images, introduce them *as part of* short-term recovery —
accepting and tracking the rough-first-pass debt.

**Sanitize code and data.** Verify the attacker didn't tamper with
source, binaries, images, configs, or the systems that build and release
them: obtain known good copies (vendors, backups, uncompromised VCS) and
compare checksums. Binary provenance turns "glibc was backdoored on the
build system" into a tractable query — which binaries were built in the
at-risk window, deployed where, with what dependents. Mark compromised
artifacts clearly and add tests preventing their reintroduction. For
application data, cryptographically verified
[backups](backup-and-restore-integrity.md) make live-vs-backup
comparisons trustworthy; know whether your rebuild tools handle malicious
or only random corruption; monitoring metrics may reveal the attack's
inflection point, lower-bounding how far back to restore — and an
insufficiently old in-place restore *reactivates* backed-up compromises.
Don't tune speed-vs-safety parameters away from defaults unless tested
under realistic production load.

**Rotate credentials and secrets** the attacker may have touched: user,
service, and admin accounts (pass-the-hash means hashes are credentials
too), SSH keys, SSL keys (stolen ones enable man-in-the-middle),
data-at-rest encryption keys (rotate and re-encrypt if the key lived on a
compromised server), application and cloud API keys (keys in source or
config files are a standing vulnerability — assume access, rotate
conservatively). Order matters: admin credentials first, then known
compromised, then sensitive-resource accounts; uncertainty may force a
disruptive all-user one-time rotation. Watch the second-order risks: a
leaked password-history database plus human patterns (`password2019` →
`password2020`) makes forced rotation *predictable*. And seize the
opportunity — mid-recovery is often when 2FA on weak entry points is
easiest to justify (bonus: failed logins now reveal the attacker still
trying), with SSO and FIDO keys on the long-term roadmap
([security change rollout](security-change-rollout.md),
[credential rotation](credential-rotation.md)).
