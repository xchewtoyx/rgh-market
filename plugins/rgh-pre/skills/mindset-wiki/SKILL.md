---
name: mindset-wiki
description: >
  Retrieve atomic wiki notes from the mindset bundle shipped in this plugin. Use when the question falls in this charter: Cognitive patterns and mental models that shape day-to-day wellbeing: growth vs fixed mindset, self-talk, cognitive reframing, resilience, self-compassion. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# mindset-wiki

This skill retrieves from the `mindset` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

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

## Boundaries

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
