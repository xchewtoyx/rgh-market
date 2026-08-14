---
name: wiki-router
description: >
  Route wellbeing and Personal Reliability Engineering wiki questions to the matching rgh-pre domain skill(s). Use when you do not already know which bundle applies. Infer or ask which charter(s) fit (questions often span two or three), then hand off. Do not answer the wiki question itself.
---

# wiki-router

Entry point for a consumer that does not yet know which rgh-pre wiki bundle applies. In scope / Boundaries below are copied at build time from `.claude/agents/<slug>-curator.md` `## Charter` (curator files are not in this plugin). Use those splits to decide.

## How to route

1. Compare the question to each bundle's In scope and Boundaries.
2. Select every bundle whose charter covers part of the question (questions often span two or three bundles).
3. If more than one reading is plausible, ask which apply, or proceed with the plausible set and say so.
4. Hand off to the matching `*-wiki` skill(s). Each of those skills owns retrieval for its bundle.
5. Do not answer the wiki question yourself. Do not retrieve notes from this router skill.

If no charter covers the topic, say so and hand off to the nearest `*-wiki` skill(s), named as nearest. Do not invent a bundle name. Do not answer the wiki question in this router.

## Bundle charters

### `philosophy` → skill `philosophy-wiki`

**In scope**

- Philosophical traditions and frameworks for how to live: Stoicism,
  Epicureanism, existentialism, Buddhist philosophy, virtue ethics, Taoism, and
  comparable schools of thought, as they bear on personal life rather than
  abstract metaphysics.
- Frameworks for meaning-making, purpose, and values clarification.
- Ethical reasoning as it applies to personal choices, character, and
  relationships with others.
- Perspectives on suffering, mortality, impermanence, uncertainty, and
  acceptance.
- Ideas about the good life, eudaimonia, flourishing, and what makes a life
  worth living — including critiques and tensions between traditions.

**Boundaries**

- Day-to-day cognitive and psychological techniques for managing thoughts,
  emotions, and attention in the moment belong to `mindset` — philosophy owns
  the underlying worldview and value framework that gives those techniques a
  purpose; mindset owns the operational practice of living it out moment to
  moment.
- Concrete habits, routines, and behavioural mechanics belong to a future
  habit-focused domain if one is added — stay at the level of frameworks and
  reasoning, not step-by-step practice.
- Clinical or therapeutic psychological intervention belongs to a future
  mental-health domain if one is added — philosophy addresses general worldview,
  not diagnosis or treatment.

### `mindset` → skill `mindset-wiki`

**In scope**

- Cognitive patterns and mental models that shape day-to-day wellbeing: growth
  vs fixed mindset, self-talk, cognitive reframing, resilience, self-compassion.
- Emotional regulation techniques and awareness practices: noticing and naming
  emotions, distress tolerance, working with difficult feelings without being
  overwhelmed by them.
- Attention and focus practices: mindfulness, presence, single-tasking, reducing
  rumination.
- Motivation, self-discipline, and how internal narratives shape action and
  follow-through.
- Common cognitive biases and distortions that undermine wellbeing (e.g.
  catastrophizing, all-or-nothing thinking) and techniques to counter them.

**Boundaries**

- The underlying value systems and philosophical frameworks that explain _why_
  something matters belong to `philosophy` — mindset owns the operational,
  moment-to-moment psychological practice; philosophy owns the worldview beneath
  it.
- Concrete habit-formation mechanics (cue-routine-reward, habit stacking,
  environment design) belong to a future habit-focused domain if one is added —
  mindset covers the psychological patterns in play, not habit engineering.
- Clinical or therapeutic diagnosis and treatment belong to a future
  mental-health domain if one is added — mindset covers general self-regulation
  practice, not clinical intervention.

### `telemetry-state` → skill `telemetry-state-wiki`

**In scope**

- Signals, patterns, and methods for noticing current mental, emotional,
  sensory, and physical state — interoceptive awareness, body scanning,
  mood/energy signals, sensory signals, emotional signals.
- Techniques for calibrating confidence in a state reading: spotting unreliable
  signals, distinguishing genuine signal from noise or masking, noticing when a
  reading is likely wrong.
- Practices for surfacing state that isn't consciously noticed until later
  (delayed awareness, blunted interoception).
- Establishing a personal baseline: what "normal" looks like for a given state,
  so deviations are detectable.

**Boundaries**

- How much room is left before a given state becomes a problem belongs to
  `capacity-load` — telemetry-state tells you what's happening now;
  capacity-load tells you how much headroom there is.
- The catalogue of named breakdown patterns (their triggers, progression,
  misdiagnoses) belongs to `failure-modes` — telemetry-state supplies the raw
  signals those patterns are recognised from, but the patterns themselves live
  there.
- What to do once a state is identified belongs to `controls-design` (routine,
  ongoing responses) or `incident-response` (acute responses).
- The cognitive practice of working with an identified state day-to-day belongs
  to `mindset`; the philosophical meaning of a state belongs to `philosophy`.

### `capacity-load` → skill `capacity-load-wiki`

**In scope**

- Models of demand and load across cognitive, emotional, sensory, social, and
  physical dimensions.
- Saturation and headroom: how to reason about how much capacity is in use
  versus available, and how that varies by dimension and over time.
- Recovery models: what restores capacity, at what rate, and under what
  conditions recovery is blocked or accelerated.
- Pacing strategies: spending capacity deliberately, budgeting across activities
  or days, balancing load across dimensions so one doesn't silently drain
  another.
- The distinction itself: how to tell whether a struggle is a capability problem
  (skill or knowledge gap) or a capacity problem (insufficient headroom right
  now).

**Boundaries**

- Recognising when a demand/supply mismatch has become a distinct, nameable
  breakdown pattern (e.g. burnout, overload) belongs to `failure-modes` —
  capacity-load models the mechanics; failure-modes catalogues what goes wrong
  when the mechanics fail.
- Reading current state moment-to-moment (am I tired right now?) belongs to
  `telemetry-state` — capacity-load is the general model of capacity, not a live
  reading.
- Structural interventions that reduce how much capacity a task requires belong
  to `controls-design`.
- What is worth spending capacity on — priorities and values — belongs to
  `philosophy` and `reliability-strategy`.

### `failure-modes` → skill `failure-modes-wiki`

**In scope**

- Recognisable patterns of breakdown or dysfunction: overload, shutdown,
  burnout, avoidance, rumination, hyperfocus, executive dysfunction, and
  comparable patterns.
- For each pattern: typical triggers, early indicators, how it tends to progress
  if unaddressed, and patterns it is commonly confused with (misdiagnoses).
- Distinctions between superficially similar patterns (e.g. shutdown vs.
  avoidance, burnout vs. depression-adjacent presentations), stated precisely
  enough to tell them apart in the moment.

**Boundaries**

- This bundle is diagnostic, not prescriptive: the raw signals used to detect a
  pattern belong to `telemetry-state`; what to do about a recognised pattern
  belongs to `controls-design` (preventive/ongoing) or `incident-response`
  (acute, in-the-moment).
- The underlying capacity/demand mechanics that explain _why_ a pattern occurs
  (e.g. why saturation leads to shutdown) belong to `capacity-load` —
  failure-modes names and describes the pattern, capacity-load explains the
  mechanism behind it.
- Day-to-day cognitive coping techniques belong to `mindset` — failure-modes
  stops at recognition.

### `controls-design` → skill `controls-design-wiki`

**In scope**

- Preventive, steady-state interventions: routines, environmental design,
  accommodations, external scaffolds (reminders, checklists, defaults),
  boundaries with other people or with one's own commitments.
- Design principles for interventions that lower ongoing cognitive cost —
  removing the need for a decision or for willpower in the moment — rather than
  interventions that just demand more discipline or motivation.
- How to choose or design a control in response to a known failure mode or a
  known capacity constraint.

**Boundaries**

- The failure modes a control is meant to prevent belong to `failure-modes`, and
  the capacity constraints it addresses belong to `capacity-load` —
  controls-design is about the intervention itself, not the diagnosis it
  responds to.
- Acute, in-the-moment response once something has already gone wrong belongs to
  `incident-response` — controls-design is steady-state prevention, not crisis
  handling.
- Whether an intervention is worth adopting given competing priorities belongs
  to `reliability-strategy`.
- Individual cognitive or psychological self-regulation techniques (as opposed
  to structural or environmental design) belong to `mindset`.

### `incident-response` → skill `incident-response-wiki`

**In scope**

- Runbook-style procedures for acute situations, structured the way an SRE
  runbook is: detection, immediate stabilisation, escalation, safe-mode
  operation, gradual restoration.
- Detection thresholds: how to recognise an incident is happening, as distinct
  from an ordinary bad day or a manageable dip.
- Immediate stabilisation actions and safe-mode operation — the minimum viable
  functioning to hold steady until the acute phase passes.
- Escalation paths: when and how to bring in outside help (a person, a
  professional, an emergency service), stated clearly rather than implied.
- Post-incident recovery: gradual restoration of function, avoiding relapse into
  the same incident, and debrief practices for learning from what happened.

**Boundaries**

- The catalogue of failure-mode patterns an incident might correspond to belongs
  to `failure-modes` — incident-response is the procedure for handling one once
  it's underway, not the diagnostic pattern itself.
- Steady-state, preventive interventions belong to `controls-design` —
  incident-response starts once prevention has failed or wasn't enough.
- Do not attempt to substitute for professional or emergency medical care: where
  escalation to outside help is the correct response, say so plainly as a step
  in the runbook rather than trying to resolve the incident in-wiki.

### `reliability-strategy` → skill `reliability-strategy-wiki`

**In scope**

- Definitions and framings of what is worth keeping available: safety, basic
  care, relationships, meaningful work, autonomy, recovery capacity — the PRE
  analogue of service objectives.
- Frameworks for evaluating trade-offs between interventions: sustainable
  quality of life versus short-term output, what "reliable" should mean for a
  person's life rather than for a system.
- Prioritisation frameworks for when objectives compete (e.g. work output versus
  relationship availability versus recovery time).
- Meta-level reasoning about the PRE system as a whole: what it's for, and how
  to judge whether the overall approach is working.

**Boundaries**

- The philosophical grounding for _why_ something matters (meaning, values, the
  good life) belongs to `philosophy` — reliability-strategy is the applied,
  PRE-specific translation of that grounding into objectives, not the underlying
  worldview itself.
- The mechanics of capacity and demand belong to `capacity-load`;
  reliability-strategy is about what to protect, not how the demand/supply
  mechanics work.
- Choosing a specific control or runbook belongs to `controls-design` or
  `incident-response` — reliability-strategy sets the objectives those choices
  should serve, not the choices themselves.
