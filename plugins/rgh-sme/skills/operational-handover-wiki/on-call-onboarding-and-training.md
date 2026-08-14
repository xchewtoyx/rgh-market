---
type: concept
title: On-Call Onboarding and Training
description: Designing a structured, cumulative learning path to build independent operating competence in new on-call engineers.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Beyer et al.), ch. 28"
  - title: "Site Reliability Workbook"
    resource: "Site Reliability Workbook (Beyer et al.), ch. 18"
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 15"
---

When transitioning a system to new operators, onboarding must focus on building independent operating competence rather than just showing them how to complete a single task. This is achieved through a structured, cumulative training curriculum rather than throwing trainees directly into operational firefighting.

## Key Onboarding Principles

- **Structure Over Chaos**: Trainees follow a defined learning path that gradually exposes them to more complex failure domains.
- **Targeted Project Work**: Onboarding projects should focus on meaningful tooling or architectural improvements rather than menial, low-value toil. This helps the trainee understand the system's inner workings.
- **Progressive Responsibility**: Trainees transition from shadowing primary on-call engineers to serving as the primary responder with a senior engineer acting as dedicated backup, before joining the standard rotation independently.

## Core Training Curriculum

A standard onboarding checklist must cover operational competence across these focus areas:
- Administering and configuring production jobs
- Service architecture, data flows, and critical dependencies
- Monitoring, white-box alerting, and dashboard navigation
- Traversal and execution of [runbooks and playbooks](runbook-checklist-design.md)
- Triage and debugging workflows, including the [system baseline for troubleshooting](system-baseline-for-troubleshooting.md) needed to recognize abnormal behavior
- Traffic redirection (draining servers or routing away from failure domains)
- Deployment rollback and mitigation procedures
- Rate-limiting and load-shedding configurations
- Capacity management and resource limits

## Active Training Techniques

To accelerate the transition to independent competence, organizations utilize four core learning techniques:

1. **Study of Historical Postmortems**: Trainees read past incident reports to understand recurring failure modes, architectural edge cases, and successful mitigation strategies.
2. **Wheel of Misfortune (Role-play)**: Senior engineers lead interactive, simulated incident scenarios. The senior engineer acts as the "system" (answering queries, providing simulated log lines), while the trainee practices triage, runbook traversal, and incident communication.
3. **Failure Injection**: Trainees run controlled failure injection scenarios (chaos engineering) in staging or non-production environments to practice diagnosing and fixing real system breaks.
4. **On-Call Shadowing**: Trainees spend several rotations shadowing primary responders, observing live incident management workflows without the pressure of primary responsibility.
5. **Collaborative Debugging**: A team works a real, live issue together in one room (or call), with only two people at keyboards — a "driver" who executes actions and a "note taker" who records the trail — while everyone else calls out what to try next. Because every step is proposed out loud before it happens, newcomers see experienced engineers get stuck, backtrack, and be wrong in front of the group, which normalizes not-knowing and builds the psychological safety needed to ask questions during a live incident later. Unlike a scripted Wheel of Misfortune, this technique needs no advance setup — most systems always have a live issue to work.

These techniques mostly transfer procedural and architectural knowledge. The harder-to-teach perceptual half of expertise — recognizing when a runbook's trigger condition has actually occurred, or when an instrument reading should be distrusted — is exactly what informal on-the-job training tends to skip, since experienced staff were rarely taught to articulate it themselves. See [Cognitive Task Analysis for Capturing Tacit Expertise](cognitive-task-analysis-for-tacit-expertise.md) for a more deliberate way to extract and codify that half before it's lost.
