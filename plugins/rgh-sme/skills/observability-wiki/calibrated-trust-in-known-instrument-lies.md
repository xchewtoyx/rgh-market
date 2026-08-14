---
type: concept
title: Calibrated Trust in Known Instrument Lies
description: Experienced operators don't treat an instrument as simply reliable or unreliable — they learn the specific, named conditions under which a given signal is known to mislead, and build a compensating check for exactly that case, which lets them keep trusting the instrument everywhere else.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power (Gary Klein), ch. 10"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

A Navy electronic warfare technician described his own console as "a liar" — he knew it could report aircraft that weren't actually there under specific, identifiable hardware/algorithm conditions, and had built his own habitual double-check for exactly that situation. Critically, this didn't make him distrust the console generally: understanding *why* the false signal occurred let him keep relying on it for everything else. Contrast the two failure modes a less experienced operator falls into instead: either trusting every reading uncritically (and getting fooled the moment the known failure condition recurs), or, after being burned once, becoming broadly suspicious of an instrument that is actually reliable outside that one narrow case.

The general principle: trust in a telemetry source should be scoped to specific, named failure conditions, not treated as a single global reliability score. A dashboard, sensor, or derived metric that is known to misbehave under one particular circumstance (a sampling edge case, a known race in an aggregation pipeline, a metric that saturates before the resource it measures actually saturates) is still trustworthy everywhere else — the fix is documenting and checking for that one condition, not discounting the whole signal by some fixed margin or ignoring it after a single bad experience. An inference-stack example: nvidia-smi "GPU utilization" honestly reports time-busy, but operators who treat that as efficiency will be fooled — compensate with [MFU/MBU](model-flop-and-bandwidth-utilization.md) rather than discarding the vendor gauge. See [telemetry quality failure modes](telemetry-quality-failure-modes.md) for the taxonomy of ways a signal can go wrong; this note is about the operator-side skill of knowing *which specific* failure mode applies to *which specific* signal, well enough to keep using it safely.
