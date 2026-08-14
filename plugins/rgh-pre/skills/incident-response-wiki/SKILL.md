---
name: incident-response-wiki
description: >
  Wiki runbooks are not a substitute for professional or emergency care. When a note's escalation step says to involve a person, a professional, or an emergency service, surface that plainly as the answer rather than trying to resolve the situation in-wiki or substituting a synthesised alternative. Retrieve atomic wiki notes from the incident-response bundle shipped in this plugin. Use when the question falls in this charter: Runbook-style procedures for acute situations, structured the way an SRE runbook is: detection, immediate stabilisation, escalation, safe-mode operation, gradual restoration. Then scan `concepts.json` descriptions, read a seed note, and follow filename links one hop at a time. Never load the whole bundle.
---

# incident-response-wiki

This skill retrieves from the `incident-response` wiki bundled in this plugin. Notes live alongside this file as `<concept_id>.md`. `concepts.json` is the only index.

## In scope

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

## Boundaries

- The catalogue of failure-mode patterns an incident might correspond to belongs
  to `failure-modes` — incident-response is the procedure for handling one once
  it's underway, not the diagnostic pattern itself.
- Steady-state, preventive interventions belong to `controls-design` —
  incident-response starts once prevention has failed or wasn't enough.
- Do not attempt to substitute for professional or emergency medical care: where
  escalation to outside help is the correct response, say so plainly as a step
  in the runbook rather than trying to resolve the incident in-wiki.

## Escalation caveat

Wiki runbooks are not a substitute for professional or emergency care. When a note's escalation step says to involve a person, a professional, or an emergency service, surface that plainly as the answer rather than trying to resolve the situation in-wiki or substituting a synthesised alternative.

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
