---
type: concept
title: Context Source Proximity and Stability
description: >
  Sort candidate context sources by how close they are to the application and
  how often they change, since both predict how hard they are to use.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
---

Two dimensions for systematically sorting *gatherable* context, starting from
what the application can obtain rather than from what would ideally help (the
inverse of [context mind mapping](context-mind-mapping.md)). Pick whichever
dimension fits the application; there's no need to apply both.

**By proximity to the application** (nearer generally means easier to
obtain):

1. What the application has directly at its fingertips — current app or
   system state (what's on screen, the current time or date).
2. What the application has already saved (e.g. user profile information).
3. What the application could record for itself even though it doesn't yet
   (e.g. previous user activity it hasn't started logging).
4. What's obtainable via public APIs (e.g. current weather).
5. What requires asking the user directly or accessing permissioned systems
   (e.g. purchase histories, emails).

Farther-away information is harder to obtain and needs to be more useful to
justify the engineering effort of reaching it.

**By stability** (more stable generally means easier to prepare in advance):

1. Always the same for a given user (e.g. profile information).
2. Changes slowly over time (e.g. purchase histories).
3. Ephemeral (e.g. current time, live interaction state).

Less stable sources are harder to prepare ahead of time, so their
[latency](context-gathering-latency-tiers.md) implications are harder to
mitigate by precomputing — an ephemeral, distant source is the worst
combination for a high-urgency application.
