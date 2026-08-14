---
name: telemetry-state-wiki
description: >
  Retrieve atomic wiki notes from the telemetry-state bundle shipped in this plugin. Use when the question falls in this charter: Signals, patterns, and methods for noticing current mental, emotional, sensory, and physical state — interoceptive awareness, body scanning, mood/energy signals, sensory signals, emotional signals. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# telemetry-state-wiki

This skill retrieves from the `telemetry-state` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

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

## Boundaries

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
