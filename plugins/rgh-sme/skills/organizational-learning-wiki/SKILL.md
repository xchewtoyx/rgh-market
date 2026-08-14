---
name: organizational-learning-wiki
description: "Retrieve organizational learning wiki concepts. Use when the question is about organizational learning: Psychological safety as a group-level construct; Silence and voice dynamics; Leadership practice for learning cultures; Team learning as a discipline distinct from individual learning; Mental models and shared vision as organisational routines; Failure taxonomy and blameless learning at organisational scale; Systems thinking as a shared diagnostic language for learning failures; Knowledge flow as a social phenomenon. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# organizational learning wiki

This skill retrieves atomic concept notes for **organizational-learning**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Psychological safety as a group-level construct: its definition (a shared belief that the environment is safe for interpersonal risk-taking), what it is not (niceness, trust, personality, lowered standards), how it is measured (survey instruments), and the evidence base linking it to learning, error reporting, engagement, and performance.
- Silence and voice dynamics: the asymmetry of voice and silence, implicit theories of voice, and named learning anti-patterns — the seven learning disabilities, defensive routines and skilled incompetence, dangerous-silence case patterns, information islands and single-point-of-failure expertise, and group-interaction anti-patterns that suppress sharing.
- Leadership practice for learning cultures: setting the stage (framing work and failure types), inviting participation (situational humility, proactive inquiry, structures for input), responding productively (appreciation, destigmatising failure, sanctioning clear violations); the leader as designer, teacher, and steward of learning capacity.
- Team learning as a discipline distinct from individual learning: dialogue versus discussion, suspending assumptions, balancing inquiry and advocacy, the left-hand-column technique, and practice fields — AARs, rehearsal, microworlds — as the rehearsal space management teams usually lack.
- Mental models and shared vision as organisational routines: surfacing and testing the assumptions behind positions; building shared vision as deliberately non-convergent inquiry; creative tension between vision and current reality.
- Failure taxonomy and blameless learning at organisational scale: preventable versus complex versus intelligent failure, standing failure-analysis rituals (failure parties, focused event analysis), and blame's effect on reporting — as ongoing organisational practice.
- Systems thinking as a shared diagnostic language for learning failures: feedback loops, delays, and archetypes (limits to growth, shifting the burden, growth and underinvestment) used to depersonalise conflict and replace blame with structural explanation.
- Knowledge flow as a social phenomenon: networks of collaboration versus capture-and-disseminate knowledge management, learning infrastructures beyond training alone, and tacit knowledge moved through storytelling and review rituals rather than databases.

Boundaries:

- Also retrieve from `resilience-engineering-wiki` for safety-science theory for high-risk sociotechnical systems
- Also retrieve from `incident-management-wiki` for incident-triggered postmortem mechanics
- Also retrieve from `operational-handover-wiki` for handover documentation and tacit-knowledge capture for a specific system or task
- Also retrieve from `technical-communication-wiki` for writing craft
- Also retrieve from `decision-alignment-wiki` for convergent, decision-producing conversation and stakeholder alignment

## How to retrieve

Do not load every note in this folder. Do not load the whole bundle into context.

1. Scan `concepts.json` in this skill folder, beside SKILL.md and the `*.md`
   notes. Match the question against each concept's `description`, `title`,
   and `concept_id`. When the question is broad, prefer higher `pagerank`
   and `concepts[].inbound_link_count` as starting seeds. Do not grep note
   frontmatter. Folded YAML `description: >` breaks line-oriented grep.
2. Read only the matching `*.md` file in this same folder. The filename
   stem is the `concept_id`.
3. Follow basename CommonMark links (`[label](other-note.md)`) hop by hop.
   Read a linked note only when the current note invokes a concept the task
   needs next.
4. Stop when the question is answered. Cite the concept id, title, and the
   note's `sources:` frontmatter.

## Do not

- Do not answer from `fleeting/` literature notes (unatomized, not
  quality-gated). If a concept exists only there, treat it as absent.
- Do not invent wiki notes, index pages, hubs, or tag schemes.
- Do not create `index.md` or README files inside the wiki.
