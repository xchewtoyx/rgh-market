---
type: concept
title: Preference-Comparison Baseline Selection
description: >
  Choose what a generated answer gets compared against as carefully as the
  comparison procedure itself — a mismatched baseline makes the result look
  objective while actually measuring something else.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), §4.1"
---

When evaluating agent output via pairwise preference comparison (human raters
or an LLM judge picking the better of two answers), the choice of *what to
compare against* is not neutral — a baseline that looks like a more
"objective" external benchmark can actually make the comparison less
meaningful than one that looks less independent. WebGPT evaluated ELI5
long-form answers against two baselines and found the seemingly weaker one
(comparing to the same human demonstrators whose behavior trained the
[reward model](rejection-sampling-best-of-n.md)) more meaningful than the
seemingly stronger one (comparing to highest-voted Reddit reference answers),
for four reasons that generalize beyond this case:

- **Matched criteria.** The candidate and baseline must have been produced
  (or judged) under the same instructions and goals. Demonstrators followed
  the same detailed criteria the model was trained and judged against;
  Reddit answers were written for a different audience and intent — ELI5
  askers want a novel simplified explanation, not a link to something already
  on the web, so a highly-upvoted Reddit answer optimizes a different target
  than the one being evaluated.
- **Fact-checkability.** A baseline that carries no references (a Reddit
  answer) can't be fact-checked the same way a
  [citation-backed answer](citation-backed-agent-answers.md) can — raters end
  up trusting fluency over verifiable support for one side of the comparison
  only.
- **Blindability.** Even with citations stripped, a candidate's writing style
  can still leak which side is which if the baseline has a distinctive
  register (Reddit voice vs. demonstrator voice). A baseline drawn from a
  similar production process is harder to identify by style alone, which
  keeps the comparison honest.
- **Effort parity.** A public corpus of "whatever answers happened to get
  written" mixes serious effort with low-effort responses; a baseline
  produced under the same effort/quality bar as the candidate isolates the
  variable actually being measured.

Design implication: prefer a baseline produced under the *same* task
instructions as the system under test — even a smaller, "less independent"
set of human-executed episodes — over a larger but criteria-mismatched public
corpus that merely looks like a stronger, more objective yardstick. This is a
narrower companion to
[grounding LLM assessment in human evaluation](grounding-llm-assessment-in-human-evaluation.md):
that note validates a *judge*; this one validates what the judge is asked to
compare against. The same caution applies to **automated proxy metrics**:
WebGPT observed that an automated truthfulness metric tuned to track human
judgment for the base-model family it was validated on went out of
distribution once applied to a structurally different system (a browsing
agent, not a bare completion model) — re-validate a proxy metric against
human judgment for the *specific* system generating the outputs, not just the
model family it was originally calibrated on, per
[GenAI radical fragility](genai-radical-fragility.md).
