---
type: concept
title: Marginal Documentation Migration
description: Bringing a legacy, poorly-documented system up to a new documentation standard incrementally at the edges of active work, rather than attempting to document the whole system at once.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 13"
---

A large undocumented or poorly-documented legacy system cannot realistically be brought up to a good documentation standard in one effort — the scope is too large, and a big-bang documentation project competes directly with the work that actually delivers value, so it tends to stall or get cut. A more durable strategy is migrating documentation coverage incrementally, the same way a strangler pattern migrates code.

## The Approach

- **Apply the new documentation standard at the edges**: When a piece of the legacy system is touched — modified, extended, or investigated for a bug — bring just that piece up to the target documentation standard as part of the work, rather than as a separate initiative.
- **Cover new work fully from the start**: Any new component built alongside the legacy system should meet the full documentation standard immediately, so the undocumented surface area shrinks over time instead of growing.
- **Accept a permanently uneven state**: Under this strategy, the system will have well-documented recently-touched areas and undocumented long-untouched areas for a long time, possibly indefinitely. This is the accepted cost of making progress without a dedicated, hard-to-justify big-bang effort — treat "some parts fully documented, others not yet" as the expected steady state, not a failure to finish.

## Applying This During Handover

When a handover includes a large legacy component that predates good documentation practice, don't commit to documenting all of it as a precondition of the handover — that commitment is unlikely to survive contact with competing priorities. Instead, agree on the marginal standard going forward (every future change brings its touched area up to standard) and be explicit with the incoming owner about which parts of the system are covered by that standard already and which are still legacy-undocumented, so they know where they're working from solid ground versus tribal knowledge they'll need to rediscover.
