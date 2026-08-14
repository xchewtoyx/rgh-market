---
type: concept
title: Phoenix Server
description: >
  A server managed so fully through automated configuration scripts that it can
  be destroyed and rebuilt from scratch at any moment, eliminating undocumented
  environment state.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 2"
---

# Phoenix Server

The deliberate opposite of a [snowflake server](snowflake-server.md): every
aspect of the machine's configuration — OS, middleware, application settings —
is captured in version-controlled automation (via
[idempotent provisioning](idempotent-provisioning.md) scripts), so the server
can be torn down and recreated identically at will rather than nursed forward
through manual patches.

Practically this is achieved through automated OS installation (PXE, Kickstart,
Preseed, or pre-baked images) plus configuration-management tooling (Puppet,
Chef, CFEngine, Ansible) applied on every rebuild. A team's ability to rebuild
a production environment from bare metal or a VM template to a running
application, entirely through automated scripts, is a direct measure of how
close its environments are to this model — and a precondition for
[ephemeral test environments](ephemeral-test-environments.md) and for treating
[environment drift](environment-drift.md) as structurally impossible rather
than merely policed.

Being *able* to rebuild on demand is necessary but not sufficient to close
off drift entirely — a manual patch path left available still gets used under
pressure. See [immutable infrastructure](immutable-infrastructure.md) for the
stricter practice of disallowing manual changes altogether.
