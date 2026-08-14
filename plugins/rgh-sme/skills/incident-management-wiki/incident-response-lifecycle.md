---
type: concept
title: Incident Response Lifecycle
description: The ten-step sequence an incident moves through from detection to organizational learning, used to locate where a response is breaking down.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 1"
---

The incident lifecycle names ten steps a response passes through: detect the
issue; determine whether it's an incident or merely an [event](dispatch-vs-notification.md);
dispatch the response team; assemble it (measured by [mean time to
assemble](mean-time-to-assemble.md)); establish command and set objectives
(see the [incident command system](incident-command-system.md)); lead
resolution; notify stakeholders; resolve and release resources; run an
[after action review](after-action-review.md); and feed findings back as
quality improvement. Quality assurance and improvement are folded into the
review step rather than treated as separate stages.

The lifecycle is a diagnostic tool as much as a description: when a response
runs slow or badly, naming which step broke down (a detection gap, a slow
assembly, an unclear command handoff, a skipped review) is more useful than
treating "the incident went badly" as one undifferentiated failure. The
[incident response process framework](incident-response-process-framework.md)
gives seven attributes to evaluate an organization's execution of this whole
lifecycle, not just one incident's run through it.
