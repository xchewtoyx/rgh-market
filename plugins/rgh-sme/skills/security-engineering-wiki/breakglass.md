---
type: concept
title: Breakglass Access
description: >
  An emergency mechanism that bypasses the authorization system entirely,
  kept safe by heavy restriction, close monitoring, regular testing, and a
  culture that keeps its use rare.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 10"
---

# Breakglass Access

Named after "break glass in case of emergency," a breakglass mechanism
grants access that bypasses the authorization system completely. It exists
because the authorization system itself can fail — a bad policy or system
update can mass-deny legitimate access — and because emergencies can
require actions no predefined workflow anticipated
([small functional APIs](small-functional-apis.md) will sometimes prove
insufficient to recover a system). The same tension applies to deployment
pipelines that [verify artifacts, not just people](verify-artifacts-not-people.md):
breakglass is the one path deliberately allowed to substitute "who" for
"what," which is exactly why its use must stay rare and loud.

Guidelines that keep breakglass from becoming a standing backdoor:

- **Highly restricted**: available only to the team responsible for the
  system's operational SLA (typically SRE).
- **Location-bound** in a [zero trust](zero-trust-networking.md)
  environment: usable only from designated *panic rooms* with additional
  physical access controls that offset the trust placed back in network
  location.
- **Closely monitored**: every use generates high-priority
  [audit](audit-log-design.md) events.
- **Regularly tested** by the responsible teams, so it works when actually
  needed.

The cost of breakglass is auditability: opening an interactive session to a
large, flexible API tells you *that* access happened, not *what* was done —
a knowledgeable insider can trivially defeat session-transcript logging.
The antidote is cultural and structural: review breakglass events at team
level (e.g. weekly on-call review), where peers have the context to spot a
well-disguised inappropriate action, and treat each legitimate use as a
signal that the normal administrative API needs a safer primitive for that
task. Without that reinforcement, audits become rubber stamps and
breakglass becomes routine.

Broad [multi-party authorization](multi-party-authorization.md) can serve
as a softer breakglass variant: it enables unusual, unplanned actions while
still requiring a second person.

The same shape recurs at the data layer for retained-but-rarely-needed
sensitive data: grant access only through an emergency approval process
(to fix a problem, or query critical historical data), and revoke it
immediately once the work is done, rather than leaving standing access
"just in case." This is [data minimization](data-minimization.md)'s
complement for data that genuinely cannot be deleted or never collected.
