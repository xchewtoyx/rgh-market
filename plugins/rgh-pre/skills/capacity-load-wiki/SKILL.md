---
name: capacity-load-wiki
description: >
  Retrieve atomic wiki notes from the capacity-load bundle shipped in this plugin. Use when the question falls in this charter: Models of demand and load across cognitive, emotional, sensory, social, and physical dimensions. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# capacity-load-wiki

This skill retrieves from the `capacity-load` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

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

## Boundaries

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

## Retrieval

Do not grep YAML frontmatter (folded `description: >` breaks line-oriented grep) and do not load this whole bundle into context.

1. **Scan.** Read `concepts.json`. Match the question against each concept's `description` (and `title`).
2. **Pick a seed.** Choose the best description match. If several look equally relevant, prefer higher `pagerank`, then higher `inbound_link_count`.
3. **Read.** Open `<concept_id>.md` in this directory.
4. **Follow links one hop at a time.** CommonMark links use filenames (`[label](other-concept.md)`). Read a neighbour only when the current note invokes a concept the task actually needs next.
5. **Truncate by budget.** Stop adding notes once you would exceed about 12000 characters of note body, or once the question is answered. `concepts.json` `links` (`source_concept_id`, `target_concept_id`, `text`, `target`) can hint the next hop without opening every file.

Stay progressive. Cite the concept note you used and its `sources:` frontmatter when the wiki backs a claim. If nothing matches, say this bundle does not cover the topic.

## Rules

- Never load the whole bundle.
- Never grep frontmatter.
- Do not answer from fleeting literature notes, even if `fleeting/` is visible in the clone.
