---
type: concept
title: API Success Criteria
description: >
  Relative measures of API success — business value, discoverability, onboarding
  speed, support burden, and lifetime adaptability — that trade off against each other.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 1"
---

**API success is relative.** One team celebrates billions of daily requests with
minimal latency and years of uptime; another counts success as a first external
client completing integration using only published documentation.

Common dimensions:

- **Business value** — operating cost versus revenue under the chosen model (ad-funded
  free, subscription, pay-per-use). Example trajectory: a maps product launched as
  a standalone app, gained an API after users reverse-engineered embedding, then
  monetized via pay-per-use while open alternatives exist.
- **Visibility and discovery** — strong design fails if prospective clients never
  find the API (product docs, developer communities, directories).
- **Time to market** — how fast the provider ships features/fixes **and** how fast
  clients can integrate.
- **Time to first call** — documentation and onboarding quality; lower is better
  ([developer experience](developer-experience.md)).
- **Time to first level-one ticket** — longer is better (fewer support-requiring defects).
- **API lifetime** — successful APIs often adapt to changing client needs; a stable,
  unchanging contract can remain in active use when clients lack alternatives (e.g.
  regulated e-government interfaces).

APIs must enable **rapid short-term integration** while supporting **long-term
independent evolution** — objectives that partially conflict. [API design challenges](api-design-challenges.md)
and [architecturally significant API requirements](architecturally-significant-api-requirements.md)
name the forces behind that tension.
