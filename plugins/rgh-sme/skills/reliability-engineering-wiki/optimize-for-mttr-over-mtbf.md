---
type: concept
title: Optimize for MTTR Over MTBF
description: >
  Given a choice, investing in faster recovery (Mean Time To Recovery) beats investing in less-frequent failure (Mean Time Between Failures), because change velocity itself is what makes fast recovery cheap.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 2nd Edition (Morris), ch. 21"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 16"
---

Two different strategies exist for improving reliability, and they pull in
opposite directions on change velocity:

- **Optimize for MTBF (Mean Time Between Failures)** — prevent failures from
  happening at all. This is the traditional posture: treat every change as
  risk, review it heavily, and make changes rarely so there are fewer
  opportunities for something to go wrong.
- **Optimize for MTTR (Mean Time To Recovery)** — accept that failures are
  inevitable in any [complex system](normal-accident-theory.md), and instead
  invest in detecting and reversing them fast. This treats recovery itself
  as the thing to engineer, not an afterthought.

MTTR-first is the better default, for a structural reason: **the same
capability that lets you deploy changes quickly and safely is what lets you
recover from a bad change quickly** — automated, tested, repeatable
deployment. A team that can push a fix (or a rollback) through its pipeline
in minutes has effectively built its recovery mechanism directly into its
normal delivery process, rather than as a separate, rarely-exercised
emergency procedure. This is why the empirical link between deployment
speed and stability isn't a paradox — see [speed-stability
correlation](speed-stability-correlation.md) — fast, frequent, small
changes lower MTTR by construction, and lower MTTR gets more of the
reliability benefit than trying to drive MTBF toward zero ever will,
because [100% reliability is the wrong
target](hundred-percent-reliability-is-the-wrong-target.md) in the first
place.

This doesn't mean MTBF stops mattering — obviously prefer changes that don't
break things — but when the two are in tension (e.g., a change-approval
process that slows deployment frequency in the name of preventing failures),
the MTTR-first strategy usually wins on total reliability delivered, because
slowing changes down to "prevent" failure also slows down the fix the next
time prevention fails anyway.
