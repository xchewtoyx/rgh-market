---
type: concept
title: Dispatch vs Notification
description: The distinction between summoning a responder to act (dispatch) and merely informing someone of a status (notification), and why blurring the two produces uncoordinated pile-on responses.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 1, ch. 3"
---

Four terms, precisely distinguished, form the vocabulary an [incident response
lifecycle](incident-response-lifecycle.md) depends on:

- **Event**: a point-in-time fact about the system (a threshold crossed, a
  deploy completing) that doesn't rise to an incident and needs no incident
  commander. Events may or may not turn into incidents.
- **Alert**: the state of a monitoring check triggered by an event — often the
  first sign an event is occurring, but investigation is still needed to tell
  event from incident.
- **Notification**: a message sent to inform someone, with no expectation
  that they act. It is an FYI.
- **Dispatch**: reaching out to a specific person or function *with the
  expectation that they respond and act*. Dispatch is an order, not a
  request — in the originating fire-service usage it is a binding commitment
  between responder and dispatcher, backed by advance training and
  readiness.

Organizations that treat "notify" as if it implied "dispatch" produce the
**spray-and-pray pattern**: a large group is notified, everyone joins a
bridge assuming someone else is in charge, and no one has actually been
tasked to act. The fix is discipline about which verb is used for which
message, not better tooling — the authors warn that automating a
notification system without first fixing this distinction "is just a
quicker way to get the wrong incident responders." Getting this distinction
right is also what an [incident commander's](incident-command-system.md)
authority depends on: dispatch only means something if there is a
command function empowered to decide who gets dispatched and why.

Once a distinct set of responders has been dispatched, the [mean time to
assemble](mean-time-to-assemble.md) them is the lifecycle stage this
distinction directly controls.
