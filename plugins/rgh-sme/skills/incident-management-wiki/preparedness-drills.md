---
type: concept
title: Preparedness Drills
description: Scheduled simulations used to practice incident response, test emergency procedures, and build operational muscle memory.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 13, ch. 28"
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield), ch. 16"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 19"
  - title: "Accelerate"
    resource: "Accelerate (Nicole Forsgren, Jez Humble, Gene Kim), ch. 11"
---

Incident response is a perishable skill. To build muscle memory and verify that procedures work, organizations must run regular simulations:
* **Wheel of Misfortune**: A role-playing drill where SRE trainees practice incident response against a simulated system failure led by a senior engineer acting as the production environment.
* **Tabletop Simulations**: Non-intrusive interactive exercises where multi-disciplinary participants (engineers, PR, legal, executives) talk through realistic scenarios and practice decision-making.
* **Disaster Recovery Testing (DiRT)**: Scheduled production failure injections (e.g., failing datacenters, pulling cables) to test emergency failovers under real conditions. Google's DiRT program highlighted that testing business processes and communication (e.g., emergency fuel procurement procedures) is as critical as testing technical systems. Beyond validating procedures, cross-functional DiRT-style exercises build the working relationships and psychological trust between teams that a real incident later depends on — the goal is operational familiarity across team boundaries *before* it's needed, not just a fault-injection test.
* **Red Team Testing**: Offensive security simulations performed without advance notice to test detection and human response capabilities.
* **Game Days**: Popularized by Jesse Robbins ("Master of Disaster" at Amazon). Game days inject large-scale faults across critical systems to surface **latent defects** (e.g., discovering that the tools needed for recovery are themselves disabled by the orchestrated failure).

### Ambiguous Threats and Weak Failure Signals
Organizations fail when they apply a standardized/compliance mindset to ambiguous threats. As shown by the NASA Columbia shuttle disaster (where foam strikes were dismissed as known "maintenance" issues), organizations must maintain an experimental mindset. As incident rates fall, tolerance thresholds must be decreased to actively investigate weak failure signals (near-misses).

These drills identify gaps in playbooks, verify alerts, and train engineers on the [incident command system](incident-command-system.md). Which scenarios are worth this investment in the first place is a prioritization question — see the [disaster risk assessment matrix](disaster-risk-assessment-matrix.md). For a more rigorous, hypothesis-driven version of fault injection than a scheduled game day, see [chaos engineering experiment design](chaos-engineering-experiment-design.md).
