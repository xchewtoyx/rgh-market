---
name: controls-design-wiki
description: >
  Retrieve atomic wiki notes from the controls-design bundle shipped in this plugin. Use when the question falls in this charter: Preventive, steady-state interventions: routines, environmental design, accommodations, external scaffolds (reminders, checklists, defaults), boundaries with other people or with one's own commitments. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# controls-design-wiki

This skill retrieves from the `controls-design` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

- Preventive, steady-state interventions: routines, environmental design,
  accommodations, external scaffolds (reminders, checklists, defaults),
  boundaries with other people or with one's own commitments.
- Design principles for interventions that lower ongoing cognitive cost —
  removing the need for a decision or for willpower in the moment — rather than
  interventions that just demand more discipline or motivation.
- How to choose or design a control in response to a known failure mode or a
  known capacity constraint.

## Boundaries

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
