---
type: concept
title: Eval Sample Sourcing
description: >
  Three ways to find enough example problems for evaluation at scale — mine
  existing records, harvest app usage, or generate samples with an LLM.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 10"
---

Scaling an [example suite](example-suite.md) past what a human can hand-pick
needs a systematic source of example problems. When the system is already in
some kind of use, the highest-fidelity source is often already sitting in
plain sight and worth mining before reaching for any of the three sources
below: whatever the team already checks manually before each release, plus
real user-reported failures pulled from the bug tracker or support queue.
Converting those into test cases guarantees the suite reflects actual usage
rather than an imagined one, and prioritizing by user impact directs effort
at what matters most — no synthetic sourcing technique matches a failure a
real user actually hit. Once that seam is exhausted, three further sources
extend the suite, each with different tradeoffs:

1. **Mine records that already exist** — find where the app's problem, or a
   subproblem of it, was already solved historically without AI, and mine
   that as a sample source (e.g. tens of thousands of human-filled form
   fields for an AI-assisted form-filling feature). Often only a *similar*,
   not identical, problem is minable at scale; the goal is a source ubiquitous
   enough in real-world corpora to provide volume, but similar enough to the
   actual application problem to support valid conclusions — a stepping stone
   between lab and reality. A code-completion assistant with no large-scale
   open corpus of "what will the user type next?" can still mine open-source
   repositories: take a function, delete its body as if the cursor were
   there, and ask the model what it would type — imperfect (deleted-body
   length differs from a typical real suggestion; later file edits like
   added imports have already happened in the source) but a near-infinite
   well of samples.
2. **Let the project generate them** — the app itself becomes a data source
   as real usage accumulates. This is maximally realistic, but comes with
   real drawbacks: no data exists until a first prototype has shipped;
   significant app updates can obsolete earlier collected data; and recording
   user telemetry requires a high standard of consent and safe handling. App
   interaction data is a good source of example *problems* (inputs) but not
   necessarily example *solutions* (outputs), since any recorded user action
   is itself heavily influenced by what the app already suggested. This
   source is most useful when a gold-standard solution isn't required at
   all; otherwise, reserve this data for online evaluation instead, which
   sidesteps some of the data-handling problems and adds its own advantages.
3. **Make them up with an LLM** — ask the model to generate samples at scale.
   Works especially well when you can start from a solution and derive the
   problem from it, and LLMs excel at generating situations outright when no
   gold-standard solution is needed at all. A recommended hierarchical
   approach: ask the model for a list of topics (or supply your own); if
   problems have combinable aspects, combine several small option lists
   multiplicatively to cheaply cover a large, well-distributed topic space;
   for more samples than topics, ask for several samples per topic in one
   generation rather than repeatedly re-querying at a higher temperature,
   which tends to produce more real variety. Two risks: generated examples
   can be overly simplistic, exaggerated tropes, or outright incorrect if the
   model lacks complete command of the problem space; and a more dangerous
   risk is an "incestuous" bias when the model generating the test samples is
   the same as, or closely related to, the model being tested — evaluating
   whether to switch from model A to model B using samples model A itself
   generated biases the outcome toward A.

These sources can be combined. The result is a large sample set, possibly
with gold-standard solutions attached and possibly not, which determines how
those solutions can then be assessed.
