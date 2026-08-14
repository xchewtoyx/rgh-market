---
type: concept
title: Calibrated Estimation for SLO Targets
description: >
  When neither historical data nor an obvious aspiration exists, a trained
  90% confidence-interval estimate from the engineers who know the system
  gives a defensible, explicitly-uncertain starting SLO target instead of an
  arbitrary guess dressed up as a fact.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd Edition (Hubbard), ch. 5"
---

[Choosing SLO targets from historical data](choosing-slo-targets-from-historical-data.md)
covers the case where enough production history exists to read a target
straight off percentiles. Before that history exists — a new service, or an
existing one with no prior measurement of the property in question —
teams often default to picking a single round-number target (e.g. "99.9%,
that sounds about right") and treating it as settled. That single number
hides how uncertain it actually is and gives no signal about how much to
trust it.

**The fix is a calibrated range, not a point guess.** Ask whoever best
understands the system (the engineers who built it, an SRE who has run a
comparable service) for a 90% confidence interval instead of a single
number: a range they believe has a 90% chance of containing the true
achievable value once the service is live. A wide range (say, a target that
could plausibly land anywhere from 99% to 99.95%) is a legitimate, honest
answer — it is simply a report of real uncertainty, not a failure to
produce a number. Narrowing that range later, once real traffic exists,
is what [SLO evolution triggers](slo-evolution-triggers.md) are for.

**Calibration is what makes the range trustworthy.** An uncalibrated
estimator is systematically overconfident: their stated 90% ranges actually
contain the true value far less than 90% of the time. Two cheap techniques
counter this bias when eliciting a target range from an engineer or SME:

- **The equivalent-bet test** — for a candidate 90% range, ask whether they'd
  rather bet on the true value falling inside it, or on a random draw with a
  stated 90% chance of the same payoff. Preferring the random draw means the
  range is too narrow (overconfident); adjust it wider until they're
  genuinely indifferent between the two bets.
- **The absurdity test** — instead of anchoring on a first guess and padding
  it slightly (which tends to produce ranges that are too narrow), start
  from an implausibly wide range (e.g. "somewhere between 90% and 100%") and
  narrow it by asking which values are clearly impossible, working inward
  from both ends until only genuinely plausible values remain.

**Why this matters more than it looks like it should**: an uncalibrated
point estimate presented as a target invites two failure modes downstream —
treating a guess as a hard commitment (making it politically costly to
correct once real data shows it was wrong), and setting an alert threshold
off a number nobody actually believed with high confidence in the first
place. A calibrated range, by contrast, is explicit that this is a
provisional [aspirational SLO](aspirational-slo.md) until [choosing SLO
targets from historical data](choosing-slo-targets-from-historical-data.md)
takes over — the range itself is the honest statement of "how much do we
actually know right now," which is the correct starting point before
committing engineering effort to hit a number.
