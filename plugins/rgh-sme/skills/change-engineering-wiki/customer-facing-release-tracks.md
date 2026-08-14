---
type: concept
title: Customer-Facing Release Tracks
description: >
  For a multi-tenant service releasing frequently, offer customers a choice
  between an immediate "rapid" track and a delayed "scheduled" track, so
  their own planning and testing needs don't have to block your release
  cadence.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 3"
---

# Customer-Facing Release Tracks

A multi-tenant service that deploys frequently creates a problem for
customers who need advance notice of behavior changes — for training,
user-acceptance testing, or their own downstream release planning. Silent,
continuous upgrades give internal delivery speed no external visibility,
which is fine for a consumer product but breaks down for business
customers who need to plan around a change.

The fix is to offer two tracks rather than picking one cadence for
everyone: a **rapid release** track that gets new features as soon as they
ship, and a **scheduled release** track that receives the same changes on
a published delay (e.g. two to three weeks later), giving customers on
that track a predictable window to prepare. Customers self-select the
track (or the specific day) that matches their own risk tolerance and
planning cycle.

This is the customer-relationship counterpart to
[decoupling deployment from release](decoupling-deployment-from-release.md):
that technique separates *installing* code from *exposing* it so the
provider can de-risk delivery internally; release tracks extend the same
separation outward, letting each customer control when a given release
becomes visible to *them*, without forcing the provider to slow down its
own deployment cadence to accommodate the most change-averse customer.
