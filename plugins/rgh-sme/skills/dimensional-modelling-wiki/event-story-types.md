---
type: concept
title: Event Story Types (Discrete, Evolving, Recurring)
description: A three-way classification of business events by how their story plays out over time, used during requirements gathering to identify which fact table type a process needs.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 2"
---

When eliciting a [business process](business-process.md) during requirements gathering, classifying its underlying business event by how the event's story plays out over time predicts which [fact-table](fact-table.md) grain type it needs, before formal grain declaration begins:

- **Discrete events** — point-in-time or short-duration stories that complete at the moment they occur (or shortly after, within the ETL refresh cycle) and are largely unconnected, occurring unpredictably: a customer buying a product, a visitor viewing a web page. None of a discrete event's details change over time once recorded. Discrete events map to a [transaction fact table](transaction-fact-table.md): the full story is known before it is loaded, so each row is inserted once and never updated.
- **Evolving events** — irregular-duration "sagas" that take days, weeks, or months to complete and occur at unpredictable intervals: an online order awaiting delivery, an insurance claim being processed. An evolving event is often really a series of discrete events (order, ship, deliver, pay) that stakeholders view as milestones of one process — the process-performance measures stakeholders actually care about (e.g., order-to-delivery duration) only become visible when these milestones are combined into a single story rather than modeled as separate discrete events. Evolving events map to an [accumulating snapshot fact table](accumulating-snapshot-fact-table.md): loaded shortly after the first milestone, then updated in place as each subsequent milestone occurs until the story completes.
- **Recurring events** — regular-duration "serials" occurring in step with one another at predictable intervals (daily, weekly, monthly): nightly inventory levels, monthly account balances. Recurring events are typically used to sample and summarize discrete events for cumulative measures (stock levels, account balances) that would otherwise be expensive to derive by aggregating every prior discrete event. Recurring events map to a [periodic snapshot fact table](periodic-snapshot-fact-table.md).

This mapping gives requirements gathering a fast diagnostic: asking a stakeholder to narrate how an event's story unfolds over time — does it happen once, does it evolve through milestones, or does it repeat on a schedule — surfaces which of the three fact table grain types the resulting design will need, well before the formal grain statement is written.

## Recording the determination and naming the event

Once every *when* detail for an event is known, record the determination confidently with a short table-level code placed directly in the event name header: **[DE]** discrete, **[RE]** recurring, **[EE]** evolving. For an evolving event, sanity-check the classification by asking for both an initial-state story (the emptiest the event can start) and a final-state story (fully completed) — if these can't meaningfully be told, reconsider whether the event is really evolving or actually discrete.

Event names follow a fixed convention: **uppercase, plural** (CUSTOMER ORDERS, PRODUCT SHIPMENTS), usually a variant of the discovered verb, or subject+verb if the verb is shared with other events (wholesale orders versus purchase orders). If the verb doesn't yield a clean name, a *how* detail — a transaction identifier such as PURCHASE ID — often does (CUSTOMER PURCHASES). Event subjects are subjective: different stakeholders may frame the same underlying event from different starting subjects during discovery, and once all details are known it can be clearer to rename the event around a different subject than the one that originally kicked off the "who does what?" question (a story told as "Salesperson sells product to distributor" may be renamed DISTRIBUTOR ORDERS once distributor turns out to be the more useful analytical subject) — the original subject having done its job of teasing out the details, even if it doesn't survive into the final name.
