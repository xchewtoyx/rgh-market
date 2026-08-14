---
name: failure-modes-wiki
description: >
  Retrieve atomic wiki notes from the failure-modes bundle shipped in this plugin. Use when the question falls in this charter: Recognisable patterns of breakdown or dysfunction: overload, shutdown, burnout, avoidance, rumination, hyperfocus, executive dysfunction, and comparable patterns. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# failure-modes-wiki

This skill retrieves from the `failure-modes` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

- Recognisable patterns of breakdown or dysfunction: overload, shutdown,
  burnout, avoidance, rumination, hyperfocus, executive dysfunction, and
  comparable patterns.
- For each pattern: typical triggers, early indicators, how it tends to progress
  if unaddressed, and patterns it is commonly confused with (misdiagnoses).
- Distinctions between superficially similar patterns (e.g. shutdown vs.
  avoidance, burnout vs. depression-adjacent presentations), stated precisely
  enough to tell them apart in the moment.

## Boundaries

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
