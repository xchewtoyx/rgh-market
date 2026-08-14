---
name: reliability-strategy-wiki
description: >
  Retrieve atomic wiki notes from the reliability-strategy bundle shipped in this plugin. Use when the question falls in this charter: Definitions and framings of what is worth keeping available: safety, basic care, relationships, meaningful work, autonomy, recovery capacity — the PRE analogue of service objectives. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# reliability-strategy-wiki

This skill retrieves from the `reliability-strategy` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

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

## Boundaries

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
