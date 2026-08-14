---
type: concept
title: Partial Verification Over Unexecuted Completeness
description: Running incomplete verification is better than not running a theoretically complete verification plan you never actually execute.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring: Improving the Design of Existing Code (2nd ed.) (Martin Fowler), ch. 4, Building Tests"
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 22, Monster Methods"
---

# Partial Verification Over Unexecuted Completeness

Aiming for exhaustive verification coverage before starting is a common way to end up verifying nothing at all: the scope of "complete" checking grows faster than the time available to build it, and the effort stalls before any check ever runs. **Partial verification over unexecuted completeness** is the principle that a smaller set of checks that actually run and catch most problems beats a comprehensive plan that never gets executed.

## Applying it

- Target verification effort at the parts of a claim or system you are actually worried about, not at every checkable statement uniformly — see [claim verification triage](claim-verification-triage.md) for prioritizing which claims to check first when time is limited.
- Treat coverage as a floor to raise incrementally, not a gate that must be met before any verification counts. A check that covers the highest-risk 60% of a claim, run today, has already shifted confidence; a plan for 100% coverage that is still being designed has not (see [non-conclusive evidence still shifts probability](non-conclusive-evidence-still-shifts-probability.md)).
- Do not let the impossibility of proving a negative (verification can never establish the total absence of error) become a reason to skip verification that would catch most errors. The unreachable standard of certainty is not the right comparison point — the comparison is "checked partially" versus "not checked."

## Sizing effort to the decision, not just cutting scope

The flip side of this principle is not "verify as much as possible" — it is "verify enough to inform the decision at hand." See [value of information for verification effort](value-of-information-for-verification-effort.md) for explicitly bounding verification spend by what the answer is actually worth, which can argue for spending *less* on verification just as often as this note argues against spending *none*.

## Allocating scarce verification effort by failure visibility

Not every part of a change deserves the same verification effort even when time is short. A useful split: concentrate dedicated checks on logic whose failure would be **silent** (wrong, but nothing about running it looks wrong — a miscalculation, a state mutation nobody would notice) and spend little or none on logic whose failure would be **immediately visible** on ordinary use (a cosmetic display glitch, an obviously malformed value). The visible-failure code still needs to work, but its own failure mode is close to a self-verifying property — you get evidence for free the first time anyone looks at it, whereas the silent-failure code gets no such free evidence and needs it built deliberately.

## Failure mode this guards against

Perfectionism about verification scope is itself a source of unverified claims: a reviewer who insists on designing a fully comprehensive check before running anything produces the same outcome — zero verification performed — as a reviewer who never intended to check at all. When a full verification plan cannot be completed in the time available, cut scope rather than cutting execution.
