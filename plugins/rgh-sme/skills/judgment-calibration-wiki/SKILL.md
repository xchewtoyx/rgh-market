---
name: judgment-calibration-wiki
description: "Retrieve judgment calibration wiki concepts. Use when the question is about judgment calibration: The dual-process frame and bias mechanism; Statistical-reasoning failure modes; The overconfidence family; Calibration and scoring; Structured estimation method; Belief updating as its own skill; Debiasing technique and deliberate practice; Team and aggregation epistemics for judgment; Choice under uncertainty and its distortion. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# judgment calibration wiki

This skill retrieves atomic concept notes for **judgment-calibration**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- The dual-process frame and bias mechanism: System 1 / System 2, substitution (answering an easier question), WYSIATI, associative coherence, anchoring, availability, representativeness, the affect heuristic — the vocabulary for locating where a judgment came from and why it may be unreliable.
- Statistical-reasoning failure modes: base-rate neglect and causal versus statistical base rates, the conjunction fallacy, the law of small numbers, regression to the mean mistaken for causation, denominator neglect and frequency-format framing.
- The overconfidence family: illusion of validity and of skill, hindsight and outcome bias as general mechanisms, the narrative fallacy, the halo effect, the planning fallacy, optimism and competition neglect.
- Calibration and scoring: precise probability language versus vague verbiage (the wrong-side-of-maybe fallacy), Brier scores, calibration versus resolution, benchmarking against naive baselines, skill-versus-luck diagnosis via regression to the mean, forecastability triage and epistemic versus aleatory uncertainty.
- Structured estimation method: Fermi decomposition, outside-view-first and reference-class forecasting, disciplined inside-view synthesis, perspective aggregation ("dragonfly eye"), regression-corrected intuitive prediction.
- Belief updating as its own skill: diagnosing underreaction (belief perseverance, identity-protective cognition) and overreaction (dilution effect), frequent granular Bayesian-spirit updates, scope sensitivity across time horizons.
- Debiasing technique and deliberate practice: premortems, decorrelating errors by collecting independent judgments before discussion, structured trait-by-trait scoring, simple models and checklists beating expert judgment (Meehl, Dawes, Apgar), the two conditions for trustworthy expert intuition (regular environment, prolonged practice with fast clear feedback), forecast postmortems, and calibration training as ongoing practice.
- Team and aggregation epistemics for judgment: wisdom-of-crowds mechanics, extremizing, what makes teams produce better-calibrated judgments than individuals or groupthink, precision questioning, adversarial collaboration, question clustering for unscorable big questions.
- Choice under uncertainty and its distortion: prospect theory (reference dependence, loss aversion, diminishing sensitivity), framing effects, mental accounting and the sunk-cost fallacy, narrow versus broad framing and risk policies.

Boundaries:

- Also retrieve from `decision-alignment-wiki` for turning a calibrated estimate into a decision document and getting stakeholders aligned
- Also retrieve from `evidence-verification-wiki` for whether a present or past claim is true, adequately sourced, and independently reviewable
- Also retrieve from `resilience-engineering-wiki` for hindsight and outcome bias as they figure in accident causation, blame, and sociotechnical safety
- Also retrieve from `incident-management-wiki` for incident postmortem practice
- Also retrieve from `capacity-performance-wiki` for capacity and demand forecasting as domain practice

## How to retrieve

Do not load every note in this folder. Do not load the whole bundle into context.

1. Scan `concepts.json` in this skill folder, beside SKILL.md and the `*.md`
   notes. Match the question against each concept's `description`, `title`,
   and `concept_id`. When the question is broad, prefer higher `pagerank`
   and `concepts[].inbound_link_count` as starting seeds. Do not grep note
   frontmatter. Folded YAML `description: >` breaks line-oriented grep.
2. Read only the matching `*.md` file in this same folder. The filename
   stem is the `concept_id`.
3. Follow basename CommonMark links (`[label](other-note.md)`) hop by hop.
   Read a linked note only when the current note invokes a concept the task
   needs next.
4. Stop when the question is answered. Cite the concept id, title, and the
   note's `sources:` frontmatter.

## Do not

- Do not answer from `fleeting/` literature notes (unatomized, not
  quality-gated). If a concept exists only there, treat it as absent.
- Do not invent wiki notes, index pages, hubs, or tag schemes.
- Do not create `index.md` or README files inside the wiki.
