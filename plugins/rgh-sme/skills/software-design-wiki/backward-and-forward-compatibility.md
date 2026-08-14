---
type: concept
title: Backward Compatibility vs. Forward Compatibility
description: >
  Backward compatibility means newer code can read data or calls produced
  by older code; forward compatibility means older code can still read data
  or calls produced by newer code — the harder, easier-to-overlook
  direction, since old code must tolerate additions it's never seen.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 4"
---

Two distinct compatibility requirements, easy to conflate but pulling in
opposite directions:

- **Backward compatibility**: newer code can correctly read data (or
  handle a call) produced by older code. This is the easier direction —
  the new code was written *with knowledge of* the old format, so it can
  explicitly special-case whatever the old format looks like.
- **Forward compatibility**: older code can still correctly read data (or
  handle a call) produced by *newer* code. This is harder, because the old
  code was written with no knowledge of what the new code might someday
  add — it has to tolerate unrecognized additions gracefully rather than
  choking on them or silently discarding something it didn't understand
  but that mattered.

Both directions matter simultaneously whenever old and new versions of
code coexist and interact with the same data or interface — which is the
normal case during a staged rollout (old and new instances running side by
side while a deployment completes) and is unavoidable wherever data
outlives the code that wrote it (a database row written years ago, read by
whatever code is deployed today). A design that only considers backward
compatibility silently assumes every reader has already upgraded, which is
rarely true for as long as the design assumes.

This is the precise, two-directional version of what [interface
evolution](interface-evolution-deprecation-versioning-extension.md)'s
three techniques are managing: versioning keeps both compatibility
directions trivially true by never asking one version to interpret the
other's data at all; extension asks the *old* consumer to remain forward
compatible with whatever the new producer adds; deprecation is only safe
once nothing depends on backward compatibility with the resource being
removed. See [schema evolution rules](schema-evolution-rules.md) for the
concrete, mechanical rules that make a structured data format achieve both
directions at once.
