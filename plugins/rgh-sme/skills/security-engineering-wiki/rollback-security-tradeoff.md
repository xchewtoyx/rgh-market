---
type: concept
title: Rollback Versus Rollback Prevention
description: >
  Reliability demands rollback to last known good; security demands that
  attackers can't roll you back into patched vulnerabilities — resolved
  with deny lists, security version numbers, and signing-key rotation.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 9"
---

# Rollback Versus Rollback Prevention

Incident mitigation usually starts with rolling back suspect changes —
most human-attention-requiring production issues are self-inflicted. But
after deploying a security patch you must *prevent* rollback (an attacker
reapplying the vulnerable version) while keeping your own option to roll
back voluntarily, because patches have bugs too. The two extreme policies
both fail: *allow arbitrary rollback* reintroduces weaponized
vulnerabilities; *never allow rollback* removes the path to known-good and
forces roll-forward through build infrastructure. Application software is
easy (deny/allow lists in the deployment system's release policy);
**self-updating components** — package daemons that overwrite themselves,
firmware that reflashes itself — are the hard case, since maliciously
modified versions can resist replacement. Assume all updates are
cryptographically signed over image and version metadata. Three composable
techniques:

- **Deny lists.** Hardcoded in the release, a deny list only handles
  accidents: leave room to roll back and an attacker "unzips" —
  incrementally stepping back version by version to a known
  vulnerability; close the room and you're at never-rollback. Better:
  keep the deny list in component-local state that survives
  up/downgrades, each release contributing its known-bad list (union into
  state). Fast enough for incident response; but the list needs
  monitoring, grows unboundedly, and removal features reopen unzipping.
- **SVN/MASVN.** A *Security Version Number* per release, incremented
  when a critical fix proves stable, gives a compact ordered security
  milestone. A *Minimum Acceptable SVN* held in component state is the
  low-water mark: updates require `Release[SVN] >= ComponentState[MASVN]`,
  and each release ratchets state up to its own hardcoded target MASVN.
  Typical rhythm: release *i* patches and bumps SVN but not MASVN (the
  patch might be buggy); release *i+1* raises MASVN once *i* proves
  stable, permanently banning *i-1* and older. This garbage-collects deny
  lists (do deny-listing fast under incident conditions, MASVN
  maintenance calmly) and keeps rollback-target *policy* separate from
  rollback *infrastructure* — consistent with
  [fast-mechanism, policy-guarded design](decouple-rollout-speed-from-policy.md).
- **Rotating signing keys.** Removing trust in an old public key
  invalidates everything signed with it. Rotate gradually — trust keys
  *k* and *k+1* together, drop *k* after stability — so
  [rotation](credential-rotation.md) is regularly exercised. Key rotation
  is also the recovery path from the worst case: an attacker who briefly
  controls release management and ships MASVN=max to brick the scheme;
  respond with a new key, plus careful dedicated logic to recognize and
  reset the absurd state, revoked aggressively once used.

**Hardware constraints**: one-time-programmable fuses give forward-only
MASVN with real reliability risk; the standard pattern is OTP protecting a
tiny bootloader that implements robust MASVN/key logic in mutable storage
one layer up. Spare parts sitting years in inventory wake with ancient
firmware that trusts only retired keys — either walk them through
intermediate releases that trust both keys, or carry old-key signatures on
new images (which only old firmware validates). Budget key/signature
space for the device's lifetime.
