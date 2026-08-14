---
type: concept
title: Canary Release
description: >
  Deploying a new version to a small subset of production traffic alongside
  the existing version, then gradually increasing its traffic share only if
  telemetry stays clean, to bound the blast radius of a bad release.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 8, 27"
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 13"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 16"
---

The new version runs on a small subset of production servers or a specific
user cohort (e.g. 5% of the fleet) while the existing version continues
serving the rest. Production telemetry — latency, error rates, log anomalies —
is monitored on the canary specifically; if it stays clean, traffic allocation
is increased in steps (5% -> 25% -> 50% -> 100%). Rollback is routing traffic
away from the canary nodes back to the stable ones.

Unlike [blue-green deployment](blue-green-deployment.md), which validates a
new version against synthetic smoke tests before any real traffic sees it, a
canary validates against a controlled slice of *real* production traffic —
catching problems that only manifest under genuine load or data patterns,
at the cost of some real users being exposed to the new version before it's
fully vetted. The same traffic-split mechanism, aimed at comparing business
outcomes between two non-defective variants instead of detecting defects, is
[A/B testing](ab-testing-via-release-routing.md) rather than canarying.

A concrete grouping used by Facebook: an "A1" group of servers seen only by
internal employees, promoted to an "A2" group serving a small percentage of
real customers once acceptance criteria are met, promoted finally to the
remaining "A3" fleet — each promotion gated on the previous group meeting its
criteria first.

Deciding to roll back based on telemetry can itself be automated — see
[cluster immune system](cluster-immune-system.md) for wiring canary telemetry
directly into an automatic rollback decision instead of relying on a human to
watch the dashboard.

## A canary failing is a process failure, not a successful catch

It's tempting to read a canary that catches a bad release as the canary
"working" the same way a failing test working as intended. The framing is
backwards: a failing automated test is a genuine success — a defect was
caught before it could reach anyone — but a failing canary means a defective
change already made it past every earlier gate and reached real users,
however few. Canarying is a deployment-safety backstop that bounds the blast
radius of a mistake that should have been caught earlier, not a substitute
for the testing that should have caught it. A team that finds itself relying
on canaries to routinely catch what should have been unit, integration, or
[acceptance tests](automated-acceptance-testing.md) has a testing gap, not a
working canary process — canaries should fail rarely enough that any failure
justifies pausing releases to root-cause the gap and add the missing test
coverage, rather than treating canary catches as routine and moving on.

## Three requirements of a working canary process

A canary process needs, at minimum: a mechanism to deploy the change to a
population subset (with the canary fraction scaling to population size — a
fixed 1% is a different real number for a 100-node fleet than a 10,000-node
one); an evaluation process that classifies the result "good" or "bad" (see
[canary evaluation metrics](canary-evaluation-metrics.md) for what to
measure); and integration of that evaluation back into the release process
itself, either an automatic pause/rollback or an escalation to a human. A
canary that stops at "deploy to a subset" without the evaluation and
integration steps is just a smaller blast radius for an otherwise-manual
release process, not an automated safety mechanism. This shape generalizes
beyond live request/response traffic — see [canarying batch and pipeline
systems](canarying-batch-pipelines.md).

## Sizing the canary: a simple risk model

A rough model for how much of the error budget a canary can consume:
canary risk ≈ (fraction of population in the canary) × (the defect's
failure rate) × (canary duration). This makes the core sizing trade-off
explicit — a larger or longer-running canary finds problems with more
statistical confidence but burns more error budget if the change turns out
to be bad — and it's deliberately a worst-case, simplified model (assumes
uniform load and, in the worst case, complete failure of every canary
request); the point is a model simple enough to actually use, not a
maximally accurate one. Run only one canary at a time: overlapping canaries
add cognitive load and risk one canary's telemetry contaminating another's
signal.

## Before/after is not a substitute for canarying

Comparing metrics from before and after a full rollout ("canarying in
time instead of population") looks like a cheaper alternative, but it isn't
one: time is a confound in its own right (day-of-week and time-of-day
traffic shape differences alone can dwarf the effect being measured), and a
genuinely bad change gets shipped to 100% of traffic to find out, rather
than to a small canary fraction. This is a different, weaker technique from
canarying, not an equivalent one.

## Staging by failure domain, not just percentage

At larger scale, "increase traffic in steps" is often expressed as expansion
across failure domains rather than a flat percentage: canary -> a single
datacenter -> a set of regional datacenters -> the global fleet, over days or
weeks. This bounds the *blast radius* of a bad release in a way a pure
traffic-percentage ramp doesn't automatically guarantee — a canary that's 5%
of traffic but concentrated in one datacenter behaves very differently from
one spread evenly worldwide if that datacenter itself has a problem. Before
starting this progression for a major launch, see
[launch readiness review](launch-readiness-review.md).
