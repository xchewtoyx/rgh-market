---
type: concept
title: False Analogue Transfer in Safety-Critical Design
description: >
  Justifying a design decision by pointing to a similar-looking predecessor
  system is only valid if the analogue matches on the causally relevant
  dimension, not merely on surface features — a mismatch on the dimension
  that actually matters produces confident, systematic under-investment.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power (Klein), ch. 12"
---

Reasoning from a precedent system is only as sound as the match between the
precedent and the new case on whichever dimension actually drives the risk
being assessed — surface similarity (both aircraft are slow, both have
multiple operators, both carry radar) is not evidence of causal similarity.
A ground-surveillance aircraft's designers reused an existing airborne
command-post aircraft as their reliability analogue for self-defense needs,
reasoning that since the reference aircraft had never had serious
self-defense problems, the new one likely wouldn't either. The analogue
matched on visible configuration but failed on exactly the dimension that
mattered: the reference aircraft flew with a dedicated fighter escort and
watched for airborne threats as its primary task, while the new aircraft had
neither — it flew a slow, predictable, radar-emitting profile deep inside
hostile range with no escort and no way to detect the threat it was most
exposed to. The false analogue caused confident under-investment in a safety
function precisely because the surface match made the comparison feel
self-evidently reasonable; the gap was only closed operationally, after the
design was fixed, by changing how the aircraft was used.

This is a design-time instance of a general discipline: experienced
practitioners select an analogue on causal relevance and then adjust for
known quantitative differences, but a categorical difference in operating
conditions —
not a matter of degree — can invalidate an analogue outright even when the
underlying hardware or configuration is identical. The warning sign is a
design justification that cites a predecessor's *track record* without
separately establishing that the predecessor faced the *same category of
threat* the new system will face. This is one more way [sensitive dependence
on initial conditions](sensitive-dependence-on-initial-conditions.md) enters
a system: a plausible-sounding analogy adopted early, during design, that
nobody revisits once the system is fielded into a genuinely different
operating context.

The mirror-image bias is [distancing through
differencing](distancing-through-differencing.md): where this bias wrongly
imports a precedent's track record because of a surface similarity,
distancing wrongly discounts a genuinely relevant precursor because of a
surface difference. Both misjudge relevance by surface features instead of
the causally relevant dimension underneath them.
