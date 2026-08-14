---
type: concept
title: Bring the Pain Forward
description: >
  If an activity in the delivery process is painful or risky, do it more
  frequently and earlier, in smaller increments, rather than deferring it —
  because repetition forces automation and shrinks each occurrence's blast radius.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1"
---

# Bring the Pain Forward

A guiding principle for pipeline design: integration, testing, database
migration, and deployment are exactly the activities teams are tempted to defer
because they are painful. Deferring them makes the problem worse — changes
accumulate, so when the activity finally happens it is larger and riskier than
if it had been done continuously.

The corrective is to do the painful thing *more* often and *earlier*:
[continuous integration](continuous-integration.md) applies this to code
integration (daily, not at release time); the [deployment pipeline](deployment-pipeline.md)
applies it to deployment itself (every commit is deployed through test
environments automatically); frequent small database migrations apply it to
schema change. Frequent repetition removes the novelty of the task, which is
what forces it to be automated — a step performed once a quarter stays manual
and error-prone; a step performed on every commit has to become a script.
