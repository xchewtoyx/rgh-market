---
type: concept
title: Example Suite
description: >
  A minimal offline-eval starting point — a handful of example inputs run
  through the app, with results eyeballed by hand rather than auto-scored.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 10"
---

The simplest starting point for [offline evaluation](offline-evaluation-proxies.md)
has three components:

1. A set of 5-20 example inputs to the app, or to one of its central steps,
   ideally spanning the expected range of real-world scenarios.
2. A script that runs the app's prompt-making against each example and asks
   the model for the completion, writing both the assembled prompts and the
   completions out to files.
3. A way to eyeball differences among those files — e.g. committing them to
   the repository and reading the diffs when something changes.

This is not a test suite in the automated pass/fail sense — differences must
be judged by hand as an improvement or a regression. Two advantages make it
worth building anyway: it can start the moment the first prompts exist, before
any automated way to assess output has been built; and growing familiarity
with the same examples over time reveals a project's typical completion
shortcomings, letting prompts be adjusted to address specific, observed
problems rather than guessed-at ones. In a real PR-summarization project,
eyeballing a mined example suite surfaced concrete, fixable issues — summaries
too terse, too verbose, or making unfounded assumptions about a PR's
motivation — each addressed with a targeted prompt tweak.

Example suites are for directed exploration, and they're scale-limited by how
many examples a human is willing to eyeball per change; detecting subtle
effects needs hundreds or thousands of examples, which requires solving two
harder problems: where the example problems come from at that scale (see
[eval sample sourcing](eval-sample-sourcing.md)), and how solutions to them
get assessed automatically instead of by hand (see
[offline evaluation proxies](offline-evaluation-proxies.md)). Moving from
ad hoc tinkering to an example suite needs only a first working
implementation; graduating from an example suite to a full evaluation harness
needs both many more examples and automatic scoring.
