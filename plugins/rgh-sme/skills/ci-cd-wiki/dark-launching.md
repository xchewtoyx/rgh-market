---
type: concept
title: Dark Launching
description: >
  Deploying full functionality to production while keeping it invisible to
  users, then exercising it with real (discarded) production traffic at
  increasing simulated load, to validate production-scale behavior before any
  customer-facing exposure.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 27"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 16"
---

# Dark Launching

A [feature toggle](feature-toggle.md) keeps a feature invisible to users, but
dark launching goes further: session code actively calls the new
functionality on real production traffic — the result is discarded or logged
rather than shown to the user, but the code path genuinely executes under
real load, data shapes, and concurrency. Simulated load can be ramped up
gradually (e.g. starting at 1% of sessions making invisible calls) well
before any real launch, for weeks in the case of large or risky changes
(a new search backend, a new account-creation flow, an expensive new
database query).

## Why this beats a canary alone

A [canary release](canary-release.md) exposes a small slice of *real* users
to the *visible* feature. Dark launching validates the feature's production
behavior — performance, resource consumption, correctness under real data —
entirely before any user sees it, so the eventual visible rollout (which can
then use canary-style progressive exposure) starts from a position of much
higher confidence, with far fewer unknowns left to discover from live user
reaction.

## Limits with stateful systems

Dark launching works cleanly when the discarded call is side-effect-free.
Against a stateful system it's more fragile: a shared cache, for instance,
gets warmed by the dark traffic just as it would by real traffic, which
inflates hit-rate and latency measurements for the *real* traffic sharing
that same cache — the measurement itself contaminates what it's trying to
validate. Where the system under test genuinely can't be isolated from
production state this way, treat the resulting performance numbers as
optimistic and prefer a true [canary release](canary-release.md) (which at
least reflects the shared-resource contention a real rollout will
experience) for the final confidence check.

## Applied to ML model rollout

The same pattern — real traffic, real code path, discarded output — is
called **shadowing** when the thing being dark-launched is a candidate ML
model rather than a feature: production requests are sent to the model, but
its predictions are never served to users. See [pre-rollout model comparison
testing](pre-rollout-model-comparison-testing.md) for where this sits
relative to sandbox comparison and canary testing in a model's rollout
sequence.

## Real launch becomes a small step

Once dark launching has already exercised the code path at production scale,
the actual customer-facing launch reduces to flipping the exposure
configuration and shipping whatever UI renders the now-visible result —
a fast, low-risk, and (importantly) equally fast-to-reverse step, since it's
the same [feature toggle](feature-toggle.md) mechanism running in both
directions.
