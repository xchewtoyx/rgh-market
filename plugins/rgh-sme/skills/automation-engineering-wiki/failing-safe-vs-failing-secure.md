---
type: concept
title: Failing Safe vs. Failing Secure
description: >
  Automation reacting to a condition it can't fully verify has to choose a
  default direction — keep serving to maximize availability, or lock down
  to maximize security — and the two goals point opposite ways.
sources:
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Google), ch. 8"
---

# Failing Safe vs. Failing Secure

When automation hits a condition it can't confirm — a config failed to
load, an integrity check can't run, a dependency it needs to consult is
unreachable — it still has to do *something*, and the two available
defaults conflict directly:

- **Failing safe (open)**: keep serving whatever it can, on the assumption
  that availability matters most. If an ACL fails to load, treat the
  default as "allow all."
- **Failing secure (closed)**: lock down rather than risk operating on
  unverified state. If an ACL fails to load, treat the default as "deny
  all."

There's no universally correct choice — it depends on what the automation
protects. The way to resolve the conflict isn't to pick one default
globally, but to decide, per component, which failure mode is
non-negotiable for that component specifically: security-critical paths
generally need to fail secure (an attacker able to trigger the failure
condition should not be able to use it to force access open), while
availability-critical paths generally need to fail safe. A system with both
kinds of components needs the failure behavior configured per component
rather than inherited from a single system-wide default.

This choice is one instance of the broader question every piece of
automation needs an explicit answer to: what does it do when its normal
inputs are missing or untrustworthy, rather than merely unexpected? Pairing
it with [safeguards against runaway
automation](safeguards-against-runaway-automation.md) covers the other
half — what stops the automation once it's already decided to act.
