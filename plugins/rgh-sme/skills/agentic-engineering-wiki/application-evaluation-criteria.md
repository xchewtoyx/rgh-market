---
type: concept
title: Application Evaluation Criteria
description: >
  Score any foundation-model application against four buckets — domain
  capability, generation quality, instruction-following, and cost/latency —
  rather than a single vague "quality" number.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
---

An application that ships without an evaluation contract is worse than one
never deployed: it costs to maintain and costs more to tear down, and many
production AI features have unclear ROI precisely because nobody can tell
whether they help. Structure that contract up front under
[eval-driven development](eval-driven-development.md) as four independent
criteria buckets, illustrated by a legal-contract summarizer:

1. **Domain-specific capability** — does the model understand the subject
   matter at all (legal contracts, code, medicine)? Constrained by
   architecture, size, and training data; evaluated via domain benchmarks.
   See [domain-capability evaluation](domain-capability-evaluation.md).
2. **Generation capability** — is the output coherent, faithful, and safe
   enough for the task? Classic NLG axes (fluency, coherence) matter less
   for strong models; factual consistency and safety dominate. See
   [generation-capability evaluation](generation-capability-evaluation.md).
3. **Instruction-following capability** — does the model obey *your*
   instructions (format, length, vocabulary, banned phrases), independent of
   whether those instructions are well written? Essential for structured
   outputs and product constraints. See
   [instruction-following evaluation](instruction-following-evaluation.md).
4. **Cost and latency** — is the quality worth the wait and the bill?
   Treat non-negotiable thresholds as hard filters before ranking survivors.
   See [LLM model selection criteria](llm-model-selection-criteria.md).

Keep the buckets separate in the suite: a model can understand sentiment
labels (domain) yet emit `HAPPY`/`ANGRY` instead of the required
`NEGATIVE`/`POSITIVE`/`NEUTRAL` set (instruction-following), or produce a
fluent summary (generation) that invents clauses absent from the source
([factual-consistency evaluation](factual-consistency-evaluation.md)). One
aggregate score hides which failure mode to fix. Wire each bucket into
[offline prompt evaluation](offline-prompt-evaluation.md) and
[agent grader types](agent-grader-types.md) so harness and prompt changes
regress against the criteria that actually matter for the application —
not only against the easiest metric to automate.
