---
type: concept
title: Style Guide Rule Process and Enforcement
description: >
  Style rules change through solution-based proposals grounded in real code
  patterns, with automated enforcement preferred over engineer memory at scale.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 10"
---

[style guides as design conventions](style-guides-as-design-conventions.md) are
not static — language versions change, rules get circumvented, enforcement tooling
becomes unmaintainable. Every rule documents original pros/cons so teams can
recognize when reasoning no longer holds.

## Changing rules

**Solution-based process**: proposals must identify an existing problem with
patterns found in *actual* code, not hypotheticals. Community discussion on
language mailing lists filters proposals; **style arbiters** (long-time language
experts) make final trade-off judgments by consensus against agreed guide goals,
not personal preference.

**Waivers** are not granted lightly — e.g. C++ macro naming requires project
prefixes because macros are global; exemptions only for genuinely global utility
macros, not convenience. "Integrity of the codebase outweighs consistency of the
project."

## Enforcement

**Social**: training, documentation, readability mentoring in code review.

**Technical** (preferred for compliance checking): automated checks apply a
single unchanging rule definition; tooling scales flat with org growth. ~90% of
C++ style guide rules were automatically verifiable (2018 survey). Tools like
clang-tidy and Error Prone surface warnings with suggested fixes in review;
deprecated-API flagging made new usages "disappear almost overnight."

**Where automation cannot reach**: rules requiring human judgment ("avoid
complicated template metaprogramming," "rarely correct to do nothing in catch")
and social rules like preferring smaller changes — size is hard to define
objectively (large mechanical one-line change across hundreds of files can be
trivial to review; small 20-line change can hide complex side effects).

**Formatters** (clang-format, yapf, gofmt, dartfmt, buildifier) remove formatting
debates from review entirely — enforced via presubmit checks rejecting diffs
formatters would produce. gofmt shipped with Go from day one specifically because
retrofitting format after open-sourcing is nearly impossible; no configuration knobs;
enables meaningful-only diffs in automated migrations (gofix, LSC).

Case study: retrofitting buildifier across 200,000 BUILD files (2012) took one
engineer six weeks with large-scale-change infrastructure. Python CamelCase →
snake_case rule change weighed ecosystem alignment against internal consistency
when independent Python applications grew.

See [ensuring consistency across a team](ensuring-consistency.md) and
[consistency as a design tool](consistency-as-a-design-tool.md).
