---
type: concept
title: Automation Fear Spiral
description: The self-reinforcing cycle where inconsistent servers make teams afraid to run automation unattended, which prevents the automation from ever being run often enough to keep servers consistent.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 2"
---

The automation fear spiral describes a common failure mode when adopting infrastructure automation tools: a team is afraid to let its configuration tool (Ansible, Chef, Puppet, or similar) run unattended, because it isn't confident about what the tool will do to servers. It lacks that confidence because the servers aren't consistent with each other. And the servers aren't consistent because the automation isn't run frequently and consistently — it's only invoked selectively, tweaked each time for the specific task at hand. This is the same failure pattern as the [apply on change antipattern](apply-on-change-antipattern.md).

The spiral is self-reinforcing: each selective, hand-tuned run of the tool introduces more [configuration drift](configuration-drift.md), which further erodes confidence, which further discourages running the tool consistently.

The way out is to deliberately break the cycle: pick one set of servers, get to the point where the code can be applied and reapplied to them without surprises, then schedule it to run automatically (for example, hourly), and only then move on to the next set of servers. Good monitoring and automated testing build the confidence needed to let [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md) run unattended, because drift is caught and surfaced as soon as it happens rather than accumulating unnoticed.
