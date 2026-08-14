---
type: concept
title: Snowflake System
description: An infrastructure instance that has drifted or been hand-built to the point that nobody is confident they can safely rebuild, change, or fix it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 2"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 1"
---

A snowflake is an instance, or part of a system, that is difficult to rebuild — often an environment that should mirror others (such as a staging environment mirroring production) but has quietly become different in ways the team no longer fully understands.

Snowflakes are not usually created deliberately. They emerge from ordinary pressure: the first build of something with a new tool involves learning-by-mistake, but there's rarely time to go back and rebuild it once other things depend on it; or someone applies an urgent fix to one instance under pressure and never propagates it elsewhere. This is [configuration drift](configuration-drift.md) taken to its extreme.

The tell-tale sign of a snowflake is that the team avoids changing or upgrading it because they aren't confident they can do so safely — so it drifts further out of date, unpatched, and sometimes partly broken, and the avoidance becomes self-reinforcing. Snowflakes create ongoing risk and waste the time of the team that owns them; it is almost always worth the effort to replace one with a [reproducible](reproducibility-principle.md) system defined as code, built and tested in parallel with the snowflake until it can safely take over. If a snowflake system isn't worth that investment, it may not be worth keeping at all.

The configuration-management literature names the same failure mode from the server-administration angle: a "snowflake server" is one built and modified through ad hoc, undocumented, interactive changes (an admin SSHing in and running commands by hand), so that recreating its exact configuration from scratch — if it were ever lost — would be expensive or impossible. Shell scripts partially address this by at least recording *some* of what was done, but they rarely handle every edge case robustly when the same script must reconcile many servers' current, possibly-already-drifted state; this gap is exactly what pushed the adoption of dedicated [server configuration](server-configuration-code.md) tools.
