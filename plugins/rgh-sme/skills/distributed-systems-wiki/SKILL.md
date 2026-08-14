---
name: distributed-systems-wiki
description: "Retrieve distributed systems wiki concepts. Use when the question is about distributed systems: Replication; Partitioning; Transactions and consistency; Coordination and consensus; The failure semantics of distribution; Distribution architecture. Scan concepts.json in this skill folder. Read only matching notes. Follow basename links hop by hop. Do not load every note. Do not answer from fleeting/ notes."
---

# distributed systems wiki

This skill retrieves atomic concept notes for **distributed-systems**. Notes and
`concepts.json` live in this skill folder. This is a consumer retrieval skill:
scan the index, read one matching note, then follow links. Do not curate,
onboard, or rewrite notes.

## When to use

Use for questions this bundle's charter covers.

In scope:

- Replication: leader/follower, multi-leader, and leaderless designs; replication lag and its anomalies (read-your-writes, monotonic reads, consistent prefix); conflict handling.
- Partitioning: key-range versus hash strategies, rebalancing, hot spots and skew, secondary indexes across partitions, request routing.
- Transactions and consistency: what ACID actually guarantees, isolation levels and their anomalies, linearizability versus causal ordering, eventual consistency and convergence.
- Coordination and consensus: quorums, leader election, fencing, distributed locks, membership, split-brain, and why consensus is needed at all.
- The failure semantics of distribution: partial failure, unreliable networks and clocks, process pauses, gray failure, timeout/retry design, idempotency and effectively-once delivery.
- Distribution architecture: event logs as integration backbone, derived data and dataflow, caching tiers, fan-out; cloud-architecture concerns that are distribution concerns — cell-based isolation, multi-region trade-offs, control plane versus data plane, blast-radius partitioning.

Boundaries:

- Also retrieve from `capacity-performance-wiki` for resource-level performance (CPU, memory, I/O, queueing maths)
- Also retrieve from `reliability-engineering-wiki` for resilience architecture patterns (circuit breaking, load shedding, graceful degradation)
- Also retrieve from `data-engineering-wiki` for analytical pipeline design
- Also retrieve from `infrastructure-as-code-wiki` for provisioning and declarative infrastructure delivery

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
