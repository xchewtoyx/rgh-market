---
type: concept
title: STRIDE Threat Classification
description: >
  A six-category checklist — Spoofing, Tampering, Repudiation, Information
  disclosure, Denial of service, Elevation of privilege — for systematically
  enumerating threats against a component instead of relying on
  unstructured brainstorming.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 9"
---

# STRIDE Threat Classification

STRIDE gives threat modeling a checklist instead of an open-ended "how
could this be attacked?" prompt. Walk each component or trust boundary
against all six categories in turn; a category that seems inapplicable is
itself worth writing down, since the same walk repeated on the next
design review may surface that it no longer is:

- **Spoofing** — an entity claiming to be something it isn't. Defended by
  verified [identities for active entities](system-identities.md) and a
  sound [authorization policy framework](authorization-policy-framework.md)
  that never assumes an unauthenticated caller is who it claims.
- **Tampering** — unauthorized modification of data or code, in transit or
  at rest. Defended by integrity controls at the boundary the tampering
  would cross — see [encryption as a baseline control](encryption-baseline-controls.md)
  and, for the supply-chain instance of this category,
  [verifying artifacts, not just people](verify-artifacts-not-people.md).
- **Repudiation** — a party denying they performed an action, with nothing
  strong enough on record to refute it. Defended by
  [audit log design](audit-log-design.md) and, where the dispute needs to
  hold up against a party motivated to deny it,
  [nonrepudiation](nonrepudiation.md) built from cryptographic proof rather
  than logging alone.
- **Information disclosure** — exposing data to a party not entitled to see
  it. Defended by [data minimization](data-minimization.md) (data that was
  never collected can't be disclosed) and
  [access classification by risk](access-classification-by-risk.md) driving
  who gets read access in the first place.
- **Denial of service** — degrading or denying availability to legitimate
  users. Covered at working depth by
  [DoS defense in depth](dos-defense-in-depth.md) and
  [DoS mitigation and response](dos-mitigation-response.md).
- **Elevation of privilege** — gaining capability beyond what was granted.
  Defended by [least privilege](least-privilege.md) as the design-time
  control and [testing least privilege](testing-least-privilege.md) as the
  check that the grant boundary actually holds.

STRIDE and [attack trees](attack-trees.md) are complementary, not
competing: STRIDE is component-scoped — for *this* interface or data
store, what could go wrong across all six categories? — while an attack
tree is goal-scoped, working backward from one attacker outcome across
however many components it touches. Running STRIDE per component and
feeding notable findings into an attack tree's leaves combines the two:
STRIDE's coverage guarantee (nothing gets skipped) with the attack tree's
depth on any one path.

Once STRIDE produces a list of threats, it says nothing about which to
fix first — that prioritization step is
[DREAD risk scoring](dread-risk-scoring.md).
