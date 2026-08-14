---
type: concept
title: Security Postmortem
description: >
  After ejecting the attacker, a blameless postmortem with
  security-specific questions converts the incident into short-term fixes
  and long-term posture strategy — and the lull before the next incident
  is preparation time.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 18"
---

# Security Postmortem

Investigation and recovery notes flow into the formal postmortem, whose
action items address the underlying problems — both the technology the
attacker exploited and the response process itself. Security-specific
questions to add to standard blameless-postmortem practice:

- Main contributing factors — and do variants or similar issues exist
  elsewhere in the environment?
- What testing or auditing should have caught these earlier; can such
  processes be built now?
- Did the expected detection control (IDS etc.) fire? If not, how do
  detection systems improve?
- Were detection and response times acceptable?
- Was the target data protected well enough to deter access; what new
  controls follow?
- Could the recovery team actually use the tools — versioning,
  deployment, testing, backup/restore — effectively?
- Which normal procedures were bypassed during recovery
  ([crisis responses bypass process](security-crisis-management.md)) and
  what remediation does that require *now*?
- Which temporary mitigations need refactoring; which bugs filed during
  the incident need fixing
  ([recovery technical debt](security-incident-recovery.md))?
- What industry/peer best practices would have helped prevent, detect,
  or respond?

Sort action items with explicit owners into **short-term** (low-hanging
fruit: add 2FA, cut patch latency, start a vulnerability-discovery
program) and **long-term** initiatives that fold into the security
program strategy (a dedicated security team, backbone encryption, OS
changes). Recovery can jump-start posture improvement — Google's
Operation Aurora aftermath produced both overnight changes and multi-year
programs (BeyondCorp, FIDO security keys).

The closing frame: the routine steady state after this incident *is* the
routine state preceding the next one. The lull is when you learn, adapt,
identify new threats, and prepare.
