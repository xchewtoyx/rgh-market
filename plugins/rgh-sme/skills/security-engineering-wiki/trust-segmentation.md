---
type: concept
title: Trust Segmentation
description: >
  Split a privileged workflow across independently implemented roles —
  signer, pusher, rate limiter — so compromising or breaking one cannot
  compromise the whole.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Trust Segmentation

Designing each piece of a system to do one task well lets you *isolate
trust*: no single role's compromise or bug is sufficient to cause the
worst outcome. It is the systems-level complement to
[small functional APIs](small-functional-apis.md) — the narrow API limits
what a caller can ask for; segmentation limits what any one caller's
compromise implies.

The configuration-distribution example: even with a narrow config-push API,
a compromised push-automation role could still push a malicious config.
Countermeasures:

- **Independent signing.** Sign the config separately from the automation
  that pushes it (ideally proving it came from revision control with a
  known hash). If the pusher role is compromised, it still cannot make the
  web server accept an attacker's config. Receivers log the config hash —
  correlating back to version control and flagging unknown configs — and
  ideally store rejected configs for later investigation.
- **Independent rate limiting.** Require a bearer token from a central rate
  limiter, implemented and tested independently of the rollout automation
  and targeted per host. A bug in the automation is then unlikely to also
  defeat the rate limiter, so a runaway rollout cannot hit the whole fleet
  at once. Because it is independent, the same rate limiter is reusable
  for config pushes, binary rollouts, reboots — any task wanting a safety
  check.

The pattern generalizes: identify the catastrophic outcome, list the roles
whose combination produces it, and ensure those roles are separately
implemented, separately credentialed, and separately testable. Human-facing
equivalents of the same idea are
[multi-party authorization](multi-party-authorization.md) (two people) and
[three-factor authorization](three-factor-authorization.md) (two
platforms).
