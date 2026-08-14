---
type: concept
title: Value of Information for Prototyping
description: >
  Before building a prototype to resolve a design uncertainty, estimate
  what a wrong choice would cost, how likely the prototype is to prevent
  it, and compare that expected saving to what the prototype itself costs.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 20"
  - title: How to Measure Anything
    resource: "How to Measure Anything: Finding the Value of Intangibles in Business (Douglas W. Hubbard), ch. 7"
---

A prototype built to resolve a design uncertainty — which of two
candidate architectures to commit to, say — is itself a cost with an
uncertain payoff, and building one is not automatically the responsible
choice just because the underlying uncertainty is real. Value of
Information (VoI) makes that decision explicit by applying Bayes'
Theorem to a small set of estimates: the cost of each candidate choice,
the cost of being wrong and having to refactor away from it later, and
the team's confidence both in each candidate and in the prototype's own
ability to actually distinguish between them.

Worked example: choosing between a $500K three-tier architecture and a
$650K microservices architecture the team has never built before (hence
low confidence in estimating its true cost and risk). If three-tier is
chosen and later found wrong, the refactor cost is roughly $300K; if
microservices is chosen first and found wrong, the refactor cost is
roughly $100K. Feeding these figures and the confidence estimates through
VoI produces two numbers: **EVPI** (expected value of perfect
information) — the most it would ever be worth paying for an experiment
that would give a fully definitive answer — and **EVSI** (expected value
of sample information) — the more realistic figure for an experiment,
like most prototypes, that only partially resolves the uncertainty.

A prototype is worth building when its expected cost is comfortably below
its EVSI; when it isn't, the more honest move is to make the best
available estimate and commit, rather than burning prototype effort that
costs more than the uncertainty it resolves is actually worth. These are
still expected values built on estimates, not guarantees, so they inform
the decision rather than replace the team's own risk appetite — but they
give the [design concept selection](design-concept-selection.md) decision
a documented, revisitable basis instead of "we felt like we should
prototype this one."

A related empirical pattern is worth checking before deciding where to
spend investigation effort at all: the **Measurement Inversion** observes
that, across many decision models, a variable's actual information value
tends to run inversely proportional to how much attention it
conventionally receives — teams keep investigating whatever they already
know how to investigate, which, having been studied before, is often
already fairly well understood and low in remaining uncertainty, while
the variable that would actually flip the decision (chance of the project
being cancelled, risk of low adoption, whether a never-attempted
integration even works) frequently hasn't been looked at at all. Before
committing prototyping effort to the most familiar uncertainty, check
whether a less-examined variable is the one actually worth an EVPI/EVSI
estimate in the first place.
