---
type: concept
title: Decomposition for Measurability
description: >
  A quality that seems too vague to measure ("security," "quality,"
  "risk") almost always decomposes into a small set of concrete,
  observable sub-variables that can be estimated even when the whole
  cannot be estimated directly.
sources:
  - title: How to Measure Anything
    resource: "How to Measure Anything: Finding the Value of Intangibles in Business (Douglas W. Hubbard), ch. 4"
---

Before accepting that something is "immeasurable," ask what decision the
measurement is actually meant to support, and what observable
consequences would be different if the thing being measured were better
or worse. Most concepts that stall a requirements discussion — "IT
security," "quality," "risk," "ecological sustainability" — turn out to
be a vague label sitting on top of a definable set of events: a
frequency and severity of specific, undesirable occurrences (a virus
outbreak, unauthorized access, a data-integrity failure). Once
"improved security" is reframed as "reduced frequency and/or severity of
this named list of events," the same probability-and-loss reasoning used
for any other risk applies to it directly.

The practical technique is **decomposition**: break the vague quantity
into a handful of sub-variables that are each individually easier to
estimate, then combine them (for example, an annual cost estimate built
from event frequency, people affected, productivity loss per person, and
loaded cost per person, each given as a range). This is worth doing even
when a decomposed sub-variable is still an estimate rather than a hard
number, because decomposition has a measurable accuracy benefit
independent of anyone's expertise: experiments comparing direct estimates
of an unfamiliar quantity against estimates built by decomposing it into
a handful of sub-variables and combining them found decomposition
reduced error by a factor of ten to a hundred for high-uncertainty
quantities, even though it made no difference for quantities people could
already estimate well directly.

This is the mechanism behind a workable [fit
criterion](fit-criterion.md) for a [non-functional
requirement](non-functional-requirement.md) that initially seems to
resist quantification: rather than declaring "usability" or "resilience"
untestable, decompose it into the specific observable events or measures
that "better" and "worse" would actually look like, and attach numbers to
those instead of to the vague label directly. It also doubles as a
gate on whether a requirements discussion has a real decision behind it
at all: an attempt to build even a minimal quantitative model — estimated
cost versus estimated benefit — routinely surfaces disagreements that
were never actually resolved, only assumed away, which is worth finding
out before, not after, the requirement is signed off.
