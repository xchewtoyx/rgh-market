---
type: concept
title: Structured Justification
description: >
  Tie privileged access to a machine-checkable business reference (bug,
  ticket, customer case) so justification can be validated automatically
  instead of read as free text.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Structured Justification

Associate every sensitive access event with a structured reference — a bug
number, ticket, incident, or customer case ID — rather than a free-text
reason. Structure is what makes verification programmatic: if support staff
view a customer's payment details, automation can check that the referenced
case was opened by *that* customer, and that ticket #12345 is a real,
open, assigned ticket rather than a random number typed to satisfy a regex.
Free-text fields make such checks effectively impossible and keep
[auditing](audit-log-design.md) manual.

Used as an *authorization* input (not just an audit annotation), structured
justification turns access-by-default into access-on-demonstrated-need.
The customer-service anti-pattern: representatives get standing access to
all customer records "for efficiency." The gradient of improvement: block
by default; first allow access only to reps with an open assigned ticket;
then narrow to the specific customer, specific data, time-bound, with
customer approval. Each step is a stronger guarantee that access was
appropriate and properly scoped.

Usability caveat: if finding a valid justification (or an approver) is too
hard, engineers will work around the control with generic justifications
("team foo needed access") that satisfy the letter but not the purpose.
Patterns of generic justifications should themselves trigger alarms in the
auditing system. Structured justification composes naturally with
[temporary access](temporary-access.md) and
[multi-party authorization](multi-party-authorization.md).
