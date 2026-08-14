---
type: concept
title: Snowflake Server
description: >
  A server whose configuration has drifted through manual tweaks and unrecorded
  patches until it is unique and impossible to recreate predictably, making it
  a liability for repeatable deployment.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, 2"
---

# Snowflake Server

A snowflake server results from manually configuring operating systems,
middleware, and application settings directly on target machines instead of
through version-controlled automation. Because each manual change is
unrecorded, no two snowflake servers end up identical, and none can be audited
or rebuilt from scratch — the environment itself becomes an undocumented,
unreproducible artifact.

## Consequences

- **Environment drift**: see [environment drift](environment-drift.md) — the
  silent divergence between environments over time.
- Builds pass in one environment (e.g. QA) and fail in another (e.g.
  production) for reasons nobody can trace, because the difference lives only
  in each machine's undocumented history.
- Deployments cannot be repeated reliably, since the deployment process depends
  on assumptions about machine state that were never written down.

## Remedy

Replace snowflake servers with automated, version-controlled provisioning — see
[idempotent provisioning](idempotent-provisioning.md) — so that any environment
can be destroyed and rebuilt from scratch on demand. A server managed this way
is sometimes called a **phoenix server**; see
[phoenix server](phoenix-server.md).
