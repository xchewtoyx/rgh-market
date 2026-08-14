---
name: philosophy-wiki
description: >
  Retrieve atomic wiki notes from the philosophy bundle shipped in this plugin. Use when the question falls in this charter: Philosophical traditions and frameworks for how to live: Stoicism, Epicureanism, existentialism, Buddhist philosophy, virtue ethics, Taoism, and comparable schools of thought, as they bear on personal life rather than abstract metaphysics. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# philosophy-wiki

This skill retrieves from the `philosophy` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

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

## Boundaries

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
