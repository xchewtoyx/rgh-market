---
type: concept
title: Disaster Risk Assessment Matrix
description: A prioritization tool that ranks disaster scenarios by probability times impact to decide which ones deserve a prepared response plan first.
sources:
  - title: "Building Secure and Reliable Systems"
    resource:
      "Building Secure and Reliable Systems (Heather Adkins, Betsy Beyer,
      Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield),
      appendix a"
---

An organization cannot prepare equally for every conceivable disaster, so
preparedness work needs a prioritization method before it needs a plan. A
**disaster risk assessment matrix** lists candidate risks (environmental —
earthquake, flood, fire, hurricane; infrastructure — power outage, loss of
connectivity, authentication system down; security — system compromise,
DDoS, phishing, emerging vulnerabilities) and scores each on two axes:
**probability of occurring within a year** (from "almost never" to
"inevitable") and **impact to the organization if it occurs** (from
"negligible" to "critical"). Multiplying the two gives a rank; the highest-
ranked risks are the ones that get a developed response plan first — worked
through in a [failure scenario mapping
workshop](failure-scenario-mapping-workshop.md) — rather than spreading
preparation thinly across everything that's theoretically possible.

Both axes are organization- and location-specific — an earthquake ranks
very differently for a Los Angeles office than a Hamburg one — so the
matrix should be filled in locally, not inherited wholesale from another
organization's assessment, and re-scored periodically as infrastructure and
threat landscape change. This feeds directly into [preparedness
drills](preparedness-drills.md): the highest-ranked risks are the scenarios
worth rehearsing, not an arbitrary or comprehensive list.

The matrix is only useful if it reflects genuine operational judgment about
real exposure — a risk assessment produced to satisfy a compliance
requirement, disconnected from what operators actually see, is exactly the
kind of "fantasy document" that [safety
bureaucracy](safety-bureaucracy.md) produces.
