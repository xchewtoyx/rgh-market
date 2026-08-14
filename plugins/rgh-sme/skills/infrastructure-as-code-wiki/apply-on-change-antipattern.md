---
type: concept
title: "Antipattern: Apply on Change"
description: Only running server configuration code when there is a specific change to make, rather than reapplying it continuously, so it drifts silently between runs.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 12"
---

The apply on change antipattern (also called *ad hoc automation*) treats infrastructure automation tools as scripting tools for making one specific change, rather than as a way to continuously enforce a system's desired state. A team runs its Ansible playbook to build a new server, then leaves it alone until the next time a change is needed — at which point they may apply the updated code only to the specific server the change targets, not the whole fleet.

This is a natural habit for anyone used to managing servers by hand or with one-off scripts, but it leaves long gaps where code is never reapplied to a given instance, during which manual fixes, external patches, or other unmanaged changes can accumulate unnoticed — [configuration drift](configuration-drift.md) by another name. It also compounds unevenly: applying a change to only the servers that specifically need it, and not others, means the next unrelated change to "all application servers" will also silently propagate the earlier one-off change everywhere, often as a forgotten side effect that surprises whoever runs it.

The alternative is [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md) or adopting [immutable servers](immutable-server-pattern.md); this antipattern is usually paired with the [push configuration pattern](push-vs-pull-server-configuration.md), since pull-based tools tend to run on a schedule by design rather than only on demand.
