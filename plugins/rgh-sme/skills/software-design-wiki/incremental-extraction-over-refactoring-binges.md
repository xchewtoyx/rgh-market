---
type: concept
title: Prefer Incremental Class Extraction Over Refactoring Binges
description: >
  Even once several responsibilities are clearly identified inside a large
  class, extract them incrementally as work touches each area rather than
  in one large all-at-once refactoring push — a binge reliably destabilizes
  a system for a while, however carefully it's done.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

Resist the temptation toward a large, all-at-once refactoring binge, even
once [several responsibilities](single-responsibility-principle.md) inside a
class have been clearly identified. Direct observation: "in nearly every
case that I've seen, when teams go on a large refactoring binge, system
stability breaks down for a little while, even if they are being careful
and writing tests as they go." A dedicated binge can be reasonable early in
a release cycle, with accepted risk and available time — otherwise, the
default is to identify responsibilities, make sure the team shares that
understanding (see
[telling the story of the system](telling-the-story-of-the-system.md)), and
extract classes **incrementally, on an as-needed basis**, spreading risk
over time while other work continues.

The realistic first-pass goal for most legacy systems: achieve
[SRP](single-responsibility-principle.md) at the **implementation** level
(extract classes, delegate to them internally) before attempting SRP at the
**interface** level, which requires migrating every client and having tests
around them (see the
[Interface Segregation Principle](interface-segregation-principle.md)).
Implementation-level extraction is a stepping stone that makes the harder
interface-level work easier later, not a separate, optional cleanup.

After extraction work reveals what an ideal decomposition could look like —
often via [scratch refactoring](scratch-refactoring.md) — resist the pull
toward leaping at that idealized target in one move: **"the structure you
have in your application works. It supports the functionality; it just
might not be tuned toward moving forward."** Use the exploratory view purely
to learn what's possible, then deliberately set it aside; real progress
means staying sensitive to the code's actual current state and nudging it
in a better direction step by step.
