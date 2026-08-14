---
type: concept
title: Quality Attribute Checklist vs. Catalog
description: >
  Standard quality-attribute taxonomies are a checklist for surfacing
  overlooked concerns, not an authoritative catalog to argue a real
  stakeholder need into or out of — and a concern the catalog has no name
  for still needs a scenario written for it.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 14"
---

Standard quality-attribute lists (ISO/IEC 25010 and similar) are useful
for one purpose: as a checklist that prompts a team to ask about a
stakeholder concern it might otherwise have overlooked, and as a
starting vocabulary to build an organization's own checklist from. They
are not useful for classification. Every such list generates taxonomy
disputes — is functional correctness part of reliability, is portability
a kind of modifiability, does a denial-of-service attack belong to
security, availability, performance, or usability — and time spent
resolving those disputes is time not spent writing a testable
[quality attribute scenario](quality-attribute-scenario.md), which is
where the actual meaning lives. No list is ever complete: real projects
routinely surface concerns no standard catalogs (a system's ease of
sysadmin operation, an organization's ability to retain the specific
talent needed to run it) — and treating "we don't have a category for
this" as a reason to drop it is a mistake, not a scoping decision.

When a genuinely new, previously unnamed quality attribute shows up —
something with no existing tactics or patterns to draw on — the response
is the same elicitation discipline used for the catalogued ones, applied
from scratch:

1. **Capture scenarios first.** Interview the affected stakeholders to
   pin down what the attribute actually means for this system, write
   specific concrete scenarios, then generalize across them into a
   reusable general scenario — the same process that produced the
   catalogued general scenarios in the first place.
2. **Model what the attribute depends on.** Identify the bounded set of
   parameters the attribute is sensitive to and the architectural levers
   that move each one — for example, a performance model might reduce to
   arrival rate, queuing discipline, scheduling algorithm, and a handful
   of other closed parameters, each traceable to a specific architectural
   choice.
3. **Assemble design approaches per parameter**, by revisiting mechanisms
   already known to affect a similar parameter elsewhere, and by seeking
   out prior designs, publications, or domain experts who have solved a
   comparable problem.

Naming a quality attribute is never itself the analysis — "the system
will be scalable" is exactly as empty as "the system will be modifiable"
was in [quality attribute scenario](quality-attribute-scenario.md), no
matter how official the name sounds.
