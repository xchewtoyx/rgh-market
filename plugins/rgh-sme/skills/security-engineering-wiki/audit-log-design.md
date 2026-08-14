---
type: concept
title: Audit Log Design
description: >
  Auditing detects incorrect authorization usage, and its power is
  determined at design time by how granular the audited actions are and
  what metadata each event captures.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Audit Log Design

Auditing exists primarily to detect incorrect authorization usage: an
operator abusing their powers, compromised credentials being exercised, or
rogue software acting against another system. Its effectiveness is largely
fixed by the design of the system being audited, along two questions:

- How granular is the access-control decision being made or bypassed?
  (*what, where*)
- How clearly is request metadata captured? (*who, when, why*)

[Small functional APIs](small-functional-apis.md) are the single biggest
lever: they produce event-level records like "pushed config with hash
123DEAD...BEEF456" that support strong assertions about what a user did or
did not do. Conversely, "opened an interactive session to a large API" is
nearly worthless — session-transcript logging is trivially bypassed by a
motivated insider and hard to read even when intact (see
[breakglass](breakglass.md)). Capture the *useful* parts of actions;
imagining how you would justify the action to a customer is a good test of
descriptiveness.

**Choosing the auditor** depends on the audit's purpose:

- *Best-practice audits* (reliability-oriented, e.g. reviewing the week's
  breakglass events) belong at team level. Peers have the context to spot
  well-disguised unnecessary access, the review applies social pressure to
  prefer safe APIs over breakglass, and recurring breakglass for one task
  flags a missing API primitive.
- *Breach-identification audits* belong with a central team. An advanced
  attacker hops from team to team; each team sees only a couple of
  anomalous actions, while a central view can connect the dots. Central
  teams can also plant non-public tripwire events for early detection.

Attach [structured justification](structured-justification.md) (bug,
ticket, or case IDs) to audit events so verification can be automated
rather than relying on free-text fields. And balance auditor context
against objectivity: an internal reviewer may be too close to the actor;
an external auditor may want to keep being hired.

Culture is the multiplier: without reinforcement, audits become rubber
stamps. Design admin APIs and automation so that auditing is easy, and keep
auditable exceptional events genuinely rare so they receive real scrutiny.
