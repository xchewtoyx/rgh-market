---
type: concept
title: Use an Automated Refactoring Tool Exclusively When Working Without Tests
description: >
  A tool that verifies Extract Method's own safety doesn't verify safety of
  adjacent manual moves like reordering statements — mixing tool-verified
  and manual edits before tests exist blurs the line between known-safe and
  unverified changes.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 22"
---

Even a genuinely [safe automated refactoring tool](automated-refactoring-tool-caution.md)
has a key limitation: most tools handle Extract Method itself safely, but
**don't** verify the safety of adjacent moves people are tempted to make at
the same time — reordering statements to group them before extracting, for
instance. "No current tool does the analysis needed to see whether
reordering can be done safely. That's a shame because it can be a source of
bugs."

The discipline this motivates: when using a tool without tests yet in
place, **use the tool exclusively** — no manual reordering, no manual
expression-splitting, not even manual variable renaming unless the tool
itself supports it as a checked operation — to maintain a clean line
between changes known-safe (tool-verified) and changes that aren't. **"When
doing automated refactoring without tests, use the tool exclusively. After
a series of automated refactorings, you can often get tests in place that
you can use to verify any manual edits that you make."** Aim tool-assisted
extractions at two goals: separating logic from awkward dependencies, and
introducing seams that make it easier to get tests in place for further
refactoring — even coarse, "hokey"-named extractions are a good starting
point, since names and boundaries can be improved once other tests exist to
back further changes. "You can do a lot of coarse work safely and handle
the details after you get other tests in place."
