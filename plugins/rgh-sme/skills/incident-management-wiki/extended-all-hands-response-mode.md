---
type: concept
title: Extended "All Hands on Deck" Response Mode
description: A temporary, explicitly bounded organizational operating mode for extraordinary incidents that requires suspending normal process and later returning to it deliberately.
sources:
  - title: "Building Secure and Reliable Systems"
    resource:
      "Building Secure and Reliable Systems (Heather Adkins, Betsy Beyer,
      Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield),
      ch. 21"
---

Some incidents — a sustained SLO breach, a serious security breach — outgrow
the normal [incident command system](incident-command-system.md) response
and require an organization-wide "all hands on deck" mode: multiple teams
devoted entirely to operational work, other priorities deferred, and
sometimes best practices (like standard change-review gates) deliberately
relaxed to move fast. This mode is different from routine incident response
in scope and duration, and needs its own discipline to avoid becoming the
new normal:

- **Declare it as temporary, explicitly**: state up front that the
  deviation is time-bounded and give a rough sense of when normal operation
  resumes. An open-ended suspension of normal process (e.g., requiring
  manual review of every production push) quietly becomes permanent toil if
  no one commits to an end point.
- **Stand up a dedicated decision-making group**: a small group with
  authority to grant fast exceptions to standard procedure, so responders
  aren't blocked waiting for normal approval chains. Log every exception
  granted so it can be reviewed and closed out later, rather than becoming
  an invisible permanent carve-out.
- **Review the incentive structure afterward, not just the technical
  cause**: when the postmortem for the triggering incident is written, it
  should examine whether organizational rewards contributed to the
  emergency — for example, a pattern of prioritizing feature launches over
  reliability work that built up the technical debt this incident exposed.
  Addressing that reward-system issue, not only the proximate bug, is what
  prevents the same "all hands on deck" event from recurring — see
  [action item quality](action-item-quality.md).

This complements [pager load management](pager-load-management.md)'s
emphasis on staffing rotations to avoid heroics during routine on-call: the
routine case avoids heroics by design, while this mode is the deliberate,
bounded exception for when heroics are briefly unavoidable.
