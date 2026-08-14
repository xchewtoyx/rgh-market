---
type: concept
title: Working Software as Status Evidence
description: A demonstrated, working artifact is stronger evidence that work is actually done than a milestone document or status report asserting that it is.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements (Dean Leffingwell), ch. 22"
---
# Working Software as Status Evidence

A progress claim ("design is complete," "requirements are signed off," "the project is on track") can be supported by two structurally different kinds of evidence: a document or milestone attestation asserting the state is reached, or a working demonstration of the thing itself doing what it's claimed to do. These are not equally trustworthy, even when both are offered in good faith.

## Why the Milestone Document Is the Weaker Evidence
A milestone report is a self-report about a proxy artifact (a document, a checklist, a sign-off), not a direct observation of the underlying capability. It inherits the general weaknesses of any self-reported or proxy claim — see [self-report vs. objective outcome evidence](self-report-vs-objective-outcome-evidence.md) — plus a specific timing failure: review touchpoints built around milestones tend to get *less* frequent exactly when a project is most behind, because a struggling team has the least ready evidence to report and least incentive to expose it. The evidence stream is thinnest exactly when scrutiny should be highest.

Milestone attestations are also a metric that becomes a target the moment they're used to evaluate a team: once "requirements sign-off" or "design complete" is what gets reported upward, the incentive is to produce the sign-off, not to make the underlying requirements actually correct or the design actually sound — the same dynamic as [Goodhart's Law](goodharts-law.md).

## Why a Working Demonstration Is Stronger
A demonstrated, functioning artifact (working software performing the claimed capability) cannot be produced by attesting alone — it requires the underlying thing to actually exist and actually work. This makes it a much harder claim to fake, and it lets a reviewer evaluate the capability directly rather than trusting a report about it. It plays the same evidentiary role in project-status claims that a first-hand demonstration plays in [continuous audit evidence generation](continuous-audit-evidence-generation.md): evidence generated as a direct byproduct of doing the work beats evidence reconstructed or attested after the fact.

## Verification Action
When a status or progress claim is backed only by a milestone document, checklist completion, or sign-off, treat it as a proxy claim rather than direct evidence that the underlying capability exists — ask to see the thing itself (a demo, a running system, a reproducible output) before treating the milestone as confirmation. Be specifically alert to this substitution under schedule pressure: a proxy-document report is most likely to be offered as a stand-in for direct evidence exactly when the team reporting it has the least working capability to show.

## See Also
- [Self-Report vs. Objective Outcome Evidence](self-report-vs-objective-outcome-evidence.md)
- [Goodhart's Law](goodharts-law.md)
- [Continuous Audit Evidence Generation](continuous-audit-evidence-generation.md)
