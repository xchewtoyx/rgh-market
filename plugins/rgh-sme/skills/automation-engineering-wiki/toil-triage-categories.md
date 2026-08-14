---
type: concept
title: Toil Triage Categories
description: >
  Not all toil is a live automation candidate — sorting it into not-yet
  automated, not worth automating, and impossible-to-automate-but-still
  streamlinable determines what to do with each kind instead of treating
  all manual work the same.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

# Toil Triage Categories

Faced with a backlog of [toil](toil.md), not every item gets the same
treatment. Sorting it into three categories determines what to actually do
with each piece:

- **Not yet automated.** Automation itself takes time to design, build,
  and test, so a backlog is inevitable and has to be prioritized like any
  other engineering work. For this category, writing the manual process
  down as a well-designed [checklist](checklist-design-principles.md) is
  not a consolation prize — accurately *describing* a process correctly is
  usually the hardest part of eventually automating it, so a good checklist
  is most of the automation work already done.
- **Not worth automating.** Some tasks are infrequent, too situational, or
  too volatile to justify the engineering investment automation would
  need — the ROI genuinely doesn't clear the bar. Recognizing this
  explicitly matters as much as recognizing what *is* worth automating:
  time spent automating a task that will rarely run again is time not
  spent on higher-value toil.
- **Cannot be automated (inherently human).** Maintaining stakeholder
  relationships, running a purchasing bid, evaluating a new technology,
  negotiating a schedule — these need human judgment and won't become
  scripts. They can still be *streamlined* short of full automation:
  better self-serve documentation reduces one-off explanation requests;
  making a common request (a capacity forecast, an access grant)
  self-service via a form or API turns what would be a standing job into
  near-zero effort; standardizing the *evaluation pipeline* itself for a
  periodic decision (qualifying a new hardware model, say) captures
  results for reuse next time instead of starting from scratch; and best
  of all is **elimination** — a decision or process removed entirely needs
  no maintenance and cannot have a bug, e.g. consolidating from three
  supported configurations down to two, or auto-approving a class of
  request that used to need manual sign-off.

A recurring pattern within the "not yet automated" category is worth
naming on its own: automating only the *common* case, and deliberately
leaving edge cases unaddressed, often causes the edge cases to disappear on
their own — see the case study in [uniformity as an automation
prerequisite](uniformity-as-automation-prerequisite.md). Teams defending an
edge case as uniquely necessary frequently abandon it voluntarily once the
automated common path is simply much better than what they had before,
which is cheaper than trying to automate every special case up front.
