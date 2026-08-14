---
type: concept
title: The 7Ws Framework
description: Classifying every event detail as one of seven interrogatives (who, what, when, where, why, how, how many) to discover a business event's dimensions and facts by asking a repeatable sequence of questions.
sources:
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 1-2"
---

Every detail worth capturing about a [business process](business-process.md)'s events falls into one of seven categories, each itself a natural-language interrogative that can be turned directly into a discovery question for stakeholders:

| 7W | Captures | Typical examples |
|---|---|---|
| Who | People and organizations involved | Customer, Employee |
| What | The things acted upon | Product, Service |
| When | Time | Date, Time of day |
| Where | Locations | Store, Delivery address |
| Why | Reasons and causality | Promotion, Weather — see [causal dimension](causal-dimension.md) |
| How | Transaction identifiers and status codes | Order ID (a [degenerate dimension](degenerate-dimension.md)), call status |
| How many | Quantities and measures | Revenue, quantity — these become [fact-table](fact-table.md) facts, not dimensions |

Six of the seven Ws (everything except how many) become [dimension-table](dimension-table.md)s or [degenerate dimension](degenerate-dimension.md)s; the seventh, how many, becomes facts. This is the same who/what/when/where/why/how checklist that [dimension attribute discovery](dimension-attribute-belonging-test.md) falls back on once the obvious attributes for a dimension have already been surfaced and further prompting is needed.

## Why this mirrors how stakeholders already think

The 7W questions a modeler asks to discover a schema are the same questions a stakeholder unconsciously asks when framing a business question: "which sales locations are performing better than last year" is a where/when/how-many question; "which customers are responding early to product promotions" is a who/when/what/why question. Explicitly walking stakeholders through the 7Ws during discovery isn't teaching them a new skill so much as making visible a way of thinking about their data they already use — which is also exactly why the resulting model tends to match how they'll want to query it later.

## A repeatable discovery sequence

The 7Ws are most effective asked in a specific, repeatable order rather than an arbitrary one:

1. **Who** and **what** first, to identify the event itself — "who does what?"
2. **When** next, to place the event in time and begin capturing concrete example stories for it.
3. Further **who**, **what**, **when**, and **where** questions, asked as many times as needed, to discover every person, organization, product, service, timestamp, and location genuinely associated with the event.
4. **How many**, **why**, and **how** last, to capture quantities, causes, and remaining descriptive detail once the event's core participants and timing are established.

Real conversations don't stay perfectly on-sequence — a "how many" answer (an order has a discount) naturally prompts a "why" question ("why do some orders have discounts?"), whose answer ("promotions") prompts a "how" question ("how are promotions identified?" — a discount code). Following these natural digressions is fine; the discipline that matters is returning to the overall sequence afterward to check that every W has actually been covered before the event is considered fully described, rather than letting the conversation's own momentum decide what gets asked. Keeping a simple visual of the sequence visible during a discovery session helps participants anticipate what's coming next and keeps the conversation self-directing.

## The three steps: discover, document, describe

Modeling one event, end to end, breaks into three steps: **discover** the event by asking "who does what?" until a clear subject-verb-object activity is identified; **document** it by capturing concrete example data in a table, one column per event detail (see [modeling by example](gathering-business-requirements.md)); and **describe** it fully by working through the 7Ws systematically, using its [event story type](event-story-types.md) — discrete, evolving, or recurring — to guide which further questions matter most, so that every relevant detail and its meaning have actually been captured rather than just listed. Example data for each detail is gathered against five [event story themes](event-story-themes.md) (typical, different, repeat, missing, group) rather than collected ad hoc, and a candidate detail that surfaces mid-interview is checked with the [position-sensitivity test](position-sensitivity-test.md) before being accepted as a detail of the event itself rather than of an existing subject or object.
