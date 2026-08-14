---
type: concept
title: Agile Testing Quadrants
description: >
  A framework classifying test types along two axes — business-facing vs.
  technology-facing, and guiding development vs. critiquing the finished
  product — used to check that a delivery pipeline's test gates cover every quadrant.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 4"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Agile Testing Quadrants

Originated by Brian Marick, expanded by Lisa Crispin and Janet Gregory. Two
independent dimensions produce four quadrants:

| | Business-facing | Technology-facing |
|---|---|---|
| **Support the team (guide development)** | Q1: functional acceptance tests, executable specifications | Q2: unit tests, component tests, API/interface tests |
| **Critique the product (verify requirements)** | Q3: exploratory testing, usability testing, UAT, demos | Q4: nonfunctional tests — capacity, load/stress, security, operational readiness |

The value of the framework for pipeline design is coverage-checking: a
[deployment pipeline](deployment-pipeline.md) that only has a
[commit stage](commit-stage.md) (Q2) and an acceptance gate (Q1) has no
systematic gate for Q3 or Q4, and needs a manual/exploratory testing stage and
a [capacity/nonfunctional test gate](nonfunctional-test-gate.md) added
explicitly, or those quadrants go unchecked. See
[test automation pyramid](test-automation-pyramid.md) for how Q1/Q2 tests
should be distributed across a suite, and
[automated acceptance testing](automated-acceptance-testing.md) for how Q1 is
implemented as a pipeline stage.

## Limits of full automation

Not every testing task belongs in a pipeline gate. Search quality, nuanced
audio/video perception, and complex security review often need **human
judgment**. The productive pattern: humans perform creative **exploratory
testing** — treating the application as a puzzle to break with unexpected
steps and data — then **encode discoveries as automated regression tests**
once a flaw is understood (e.g. security findings feeding continuous scanners).
Automate well-understood behaviors so expensive human effort focuses where it
adds most value — Q3 critique the product, not repetitive checks machines
handle better in Q1/Q2.
