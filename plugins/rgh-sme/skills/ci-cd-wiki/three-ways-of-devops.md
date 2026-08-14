---
type: concept
title: The Three Ways of DevOps
description: >
  The foundational DevOps framing that pipeline practices exist to serve fast
  flow (First Way), fast feedback (Second Way), and continual organizational
  learning (Third Way) — a lens for judging whether a specific pipeline change
  actually helps.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 1"
---

# The Three Ways of DevOps

A high-level frame (originating in *The Phoenix Project*) for why the
concrete pipeline practices in this bundle matter — three principles, each
answering a different question about the flow of work between Development and
Operations:

- **The First Way — fast flow, left to right**: work should move quickly from
  commit through to the customer. Practices: making work visible, reducing
  batch size, [building quality in](bring-the-pain-forward.md) rather than
  inspecting for defects afterward, and optimizing for global rather than
  local goals. This is the underlying justification for most of this bundle's
  content — the [deployment pipeline](deployment-pipeline.md),
  [continuous integration](continuous-integration.md),
  [independent deployability](independent-deployability.md) — all exist to
  serve fast, low-friction flow.
- **The Second Way — fast feedback, right to left**: problems should surface
  as early and as loudly as possible, and be swarmed until a real
  countermeasure exists — not just patched once and forgotten. This is what
  [fail-fast pipeline design](fail-fast-pipeline.md) and the
  [commit stage](commit-stage.md)'s speed budget are structurally built to
  provide: a defect found in minutes at commit time is a completely different
  problem than the same defect found in production weeks later.
- **The Third Way — continual learning and experimentation**: a generative,
  high-trust culture where local discoveries (a fix, a technique, a tool) get
  converted into global improvements available to the whole organization,
  rather than staying siloed with the team that found them. This Way is
  primarily organizational and cultural — the specific practices for building
  that culture belong to change-engineering; this bundle's contribution is
  making sure the pipeline's own audit trail and metrics (see
  [compliance through pipeline automation](compliance-through-pipeline-automation.md),
  [the DORA four key metrics](dora-four-key-metrics.md)) actually surface the
  data a learning culture needs to act on.

A useful test for any proposed pipeline change: which Way does it actually
serve? A change that doesn't measurably improve flow, feedback speed, or the
organization's ability to learn from what happened is probably solving the
wrong problem.
