---
type: concept
title: Confidentiality Without Anonymity in Reporting Systems
description: >
  Letting analysts follow up with a reporter before de-identifying their
  submission captures far richer safety detail than fully anonymous
  reporting — a design choice distinct from, and often confused with,
  protecting reporters from blame.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 17"
---

Two ways of protecting a reporter are often treated as interchangeable but
produce very different reporting systems. **Anonymity** means the reporter's
identity is never captured at all. **Confidentiality without anonymity**
means the reporter's identity is captured and retained temporarily, strictly
protected from disclosure, specifically so an analyst can follow up and
clarify details before the report is de-identified for the permanent record.

ASRS runs on the second model: voluntary, strictly confidential, but not
anonymous during processing. This is what makes its reports usable — a
report that is unclear, incomplete, or ambiguous can be clarified by going
back to the person who filed it, before anything is lost to a generic
follow-up question no one can now answer. Healthcare's NRLS instead used
mandated anonymity to encourage reporting volume, which succeeded at volume
(over 700,000 reports a year) but foreclosed follow-up entirely: an
ambiguous or incomplete anonymous report simply stays ambiguous or
incomplete forever, however many of them accumulate.

**The trade-off this reveals: maximising the raw count of reports and
maximising the *usable detail* per report pull in different directions**,
and anonymity trades the second for the first. This is a distinct design
axis from [just culture](just-culture.md)'s formal-versus-confidential
reporting distinction (which concerns whether contextual detail survives
being filtered through a line-management report at all) — confidentiality
without anonymity is specifically about whether a report, once filed, can
still be improved after the fact, independent of how much detail it
contained when submitted. A domain low enough on [safety
culture](westrum-typology.md) that reporters would not trust *any*
non-anonymous system is exactly the case where this design choice is not
available and full anonymity becomes the only workable option, at the direct
cost of analyst follow-up — see [five structural dimensions of incident
reporting viability](five-structural-dimensions-of-incident-reporting-viability.md)
for how a domain's safety-culture level constrains which reporting-system
design it can actually sustain.
