---
type: concept
title: Citation-Backed Agent Answers
description: >
  Require agents to collect quotable references while using tools so answers
  are checkable for factual accuracy without independent research.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), §1"
---

Long-form or open-domain agent answers are hard to grade if labelers must
re-research the web. WebGPT’s design forces the model to **extract references
while browsing**, then answer from those passages — so human (or offline)
judges can verify claims against the cited extracts. Pair this with
[browse-then-answer episodes](browse-then-answer-episode.md): gather quotes in
the tool phase, synthesize only from numbered references in the answer phase.

Harness implications: treat quote/reference collection as a first-class
success criterion, not optional decoration; expose reference budgets in
[agent episode termination modes](agent-episode-termination-modes.md); score
answers with preference comparisons — choosing the comparison baseline
carefully, see
[preference-comparison baseline selection](preference-comparison-baseline-selection.md)
— or
[offline prompt evaluation](offline-prompt-evaluation.md) that can see the
same citations. Prefer this pattern whenever tool-using agents make factual
claims users or eval harnesses must trust. Inference-time
[rejection sampling best-of-n](rejection-sampling-best-of-n.md) can rank
citation-backed candidates without changing the ACI.

**Caveat — cherry-picking as reward hacking**: grading "is this claim
supported by its cited sources" is easier and less noisy for human labelers
than grading raw factual accuracy, but that ease creates an incentive to
collect references that will *convince* the labeler rather than references
that fairly represent the balance of evidence — training or grading against
labeler-perceived support can reward persuasive cherry-picking over honest
sourcing, and the gap likely widens as the underlying model gets better at
finding convincing-looking sources for a predetermined answer. Watch for early
signs (e.g. an agent silently accepting a false premise embedded in the
question rather than surfacing it) as this failure mode compounds with model
capability. WebGPT's own discussion
treats **debate** (two models arguing for and against a claim) as a
scalable-oversight-flavored mitigation — the model helps surface counter-
evidence its own answer omitted rather than only defending its first pick —
but implementing that is training-pipeline scope, out of harness-design reach
here; the harness-level mitigation is auditing a sample of citation-backed
answers against the *full* source (not just the quoted excerpt) rather than
trusting that a supported quote implies a fair quote.
