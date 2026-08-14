---
type: concept
title: Gold-Standard Matching
description: >
  Score a completion by comparing it against a trusted reference solution,
  matching on one carefully chosen aspect rather than the whole output.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 10"
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), Appendix E"
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 46–52"
---

The easiest way to evaluate a solution at scale, when a gold-standard
reference is available (e.g. what a human did without LLM assistance, mined
from historical records per [eval sample sourcing](eval-sample-sourcing.md)):
check how often the app's output matches it. For binary or simple
categorical outputs, this is a direct match-count; for more statistical
power on such outputs, [logprobs](logprobs-fundamentals.md) can sharpen
the signal beyond a raw count.

For free-form text output, exact match becomes meaningless as answer length
and freedom grow — exact matches become vanishingly rare even for genuinely
good completions, and exact matching raises the question of what's actually
being optimized: correctness, or one particular phrasing. For multi-step math
and counting tasks specifically, prefer **last-number exact match** instead:
run [answer cleansing](answer-cleansing.md) (or equivalent) and compare only
the final numerical value to gold, ignoring intermediate reasoning text —
that oracle is what TextGrad-style
[prompt optimization tooling](prompt-optimization-tooling.md) used for GSM8K
and Object Counting on held-out splits. When the gold is an ordered list or
other structure where string equality is brittle (e.g. word sorting), fall
back to a tagged binary LLM judge rather than forcing exact match.

**Partial match metrics** fix the free-form case more generally by picking
one particularly important aspect of the solution and matching only on that —
for generated source code, an exact match after stripping comments, blank
lines, and whitespace; for a travel suggestion, a match on destination
country alone, ignoring everything else. The hard choice is which aspect
actually matters, since in most applications a catastrophic failure in *any*
aspect can theoretically invalidate the whole solution — but some failure
modes are far more likely and severe than others, and worth guarding against
specifically. Example: for a smart-home assistant told "I'm chilly," checking
only whether it regulated the heating system at all (not the exact
temperature it chose) is the sensible partial match, because failing to
recognize heating as the right system is a far more likely and severe
failure than picking a merely-suboptimal temperature.

Two criteria for choosing a good partial-match aspect: it should distinguish
well between a breaking divergence from the gold standard and a benign one
(otherwise the evaluation isn't meaningful), and it should be neither too
specific (the model would have little realistic chance of getting it right)
nor too general (the evaluation becomes meaningless in the other direction).
Both criteria require experimenting with the model to find its typical
mistake patterns and their severity — some circularity is unavoidable, since
the test gets chosen based on what the current setup is already good or bad
at, and then used to guide future development — but this is still far better
than a weak or misleading metric. For structured, non-free-form outputs,
testing one especially critical field is often the right focus — for
tool-heavy applications in particular, whether the right tool was used and
called with correct syntax, per
[tool definition design](tool-definition-design.md).

A general principle for sequencing this: when the model makes several
sequential decisions while generating a completion, evaluate the *first*
decision with a real chance of going wrong, and treat later decision points
as invalidated once an earlier one has failed. In the smart-home example, the
decision order is: use a tool at all, then which specific tool, then which
argument values — a malformed tool call likely makes the whole suggestion
useless regardless of what the arguments would have been, while a correctly
called tool with different argument values than the gold standard still has a
substantial chance of being a reasonable answer.

Pair gold-standard matching with
[offline example suites](offline-example-suites.md); when no gold reference
exists, use [functional completion testing](functional-completion-testing.md)
or [SOMA LLM assessment](soma-llm-assessment.md) instead.

**Not every divergence from gold is a defect.** A candidate can differ from
the gold reference while being an equally valid — sometimes even more
efficient — solution. Example: a code-fix candidate that makes the smallest
edit needed to gate a feature behind an existing flag, while the gold patch
is longer because it also introduces a new named variable and mirrors
patterns used elsewhere for consistency with house style; the candidate is
functionally correct and arguably more efficient, just less consistent with
codebase conventions the test suite doesn't check for. Before treating a
match failure as a real regression, ask whether the aspect that diverged is
one your chosen partial-match aspect actually needs to guard — a
style/consistency divergence that current tests can't distinguish
from the gold behavior is a different, and usually lower-severity, finding
than a divergence that changes what the output actually does. Relatedly, a
candidate that passes today's tests by using a **narrower, hand-rolled**
mechanism where gold uses an existing general-purpose helper can still be a
worse long-term solution even though nothing in the current match criterion
catches it — the helper likely already handles edge cases the current test
suite never exercises, so gold-standard matching on today's suite understates
the candidate's fragility to *future*, not-yet-written cases. When you notice
this pattern, treat "did the candidate reach for the same general mechanism"
as a partial-match aspect worth adding, not only "did it pass" — see
[idiomatic minimal patch preference](idiomatic-minimal-patch-preference.md).

**Static-analysis metrics as an automatic partial-match aspect for code.**
When the output is source code, standard software-engineering complexity
metrics (Cyclomatic complexity, Halstead complexity) computed on the modified
functions give an automatic, gold-comparable quality signal beyond pass/fail
— run the same static analysis on the candidate's changed functions and on
gold's, and compare the delta each introduces. This can surface a
maintainability cost a test suite is blind to: a candidate that solves the
issue with fewer total lines can still raise the complexity of a
**widely-used** function more than gold does (e.g. adding a conditional
branch directly inside a shared class instead of factoring the new case into
a smaller, already-simple helper the way gold does) — "shorter" and "lower
long-term cost" are not the same axis, and a raw diff-size comparison can
reward the worse patch. Use this as one more partial-match aspect alongside
pass/fail and diff-size checks, not a replacement for either.
