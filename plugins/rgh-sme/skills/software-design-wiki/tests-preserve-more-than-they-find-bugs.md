---
type: concept
title: Tests Preserve Behavior More Than They Find Bugs
description: >
  Manual bug-hunting finds bugs fast in the moment but must be redone from
  scratch on every change; automated tests' real legacy-code value is
  catching future drift from documented behavior, not finding today's bugs.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 13"
---

Manual testing finds bugs quickly in the moment, but has to be redone from
scratch on every subsequent change — "nearly every team ... that depended on
manual testing for its changes has ended far behind." The better strategy:
"concentrate effort on not putting bugs into code in the first place." In the
natural flow of development, tests that specify behavior become tests that
preserve it — their primary value isn't finding existing bugs directly, it's
catching later changes that accidentally diverge from previously-verified
behavior. You do find bugs this way, typically on *later* runs, not the
first.

The practical implication for legacy work: since there's usually no way to
verify "preserving behavior" from a blank slate, the achievable goal is to
wrap the area about to change with a safety net — see
[characterization tests](characterization-tests.md) — accepting that you
won't, and shouldn't try to, find and fix every latent bug as a
prerequisite. "If we make finding and fixing all of the bugs our goal, we'll
never finish."
