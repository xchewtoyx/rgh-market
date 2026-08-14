---
type: concept
title: Confirmation Bias in Debugging
description: A common troubleshooting failure mode is testing only for evidence that supports an initial guess while ignoring contradictory metrics, which can lock an investigation onto the wrong hypothesis.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 12"
---

Once an investigator forms an initial theory, there's a strong pull toward seeking out data that confirms it and discounting data that doesn't. In an active incident this is compounded by time pressure and the desire for the investigation to be over.

The corrective is to actively test hypotheses against the possibility of being wrong, not just to look for supporting evidence — see [testing hypotheses with real data](hypothesis-testing-with-real-data.md). Related failure mode: "poking the system" — making arbitrary changes in production without a clear hypothesis or rollback plan, which can compound an outage rather than resolve it.

A related but distinct bias shows up after the investigation ends rather than during it: see [resulting](resulting-bias-in-postmortem-evaluation.md) for the error of judging whether an in-incident decision was good by whether its outcome was good.

A structural mitigation borrowed from experimental physics is **outcome-blind analysis**: have whoever is examining the telemetry (logs, traces, dashboards) do so without being told the suspected cause or the eventual verdict first. Knowing the hypothesis in advance measurably biases how ambiguous evidence gets read, even among trained analysts explicitly trying to be objective — so where feasible, describe the symptom and let the investigator form their own hypothesis from the data before comparing notes with whoever already has a theory.
