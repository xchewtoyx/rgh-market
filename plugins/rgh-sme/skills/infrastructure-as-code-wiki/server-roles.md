---
type: concept
title: Server Roles
description: A named grouping of server configuration modules and default parameters, applied to a server to define its purpose, often organized with a base role that others inherit from.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 11"
---

A server role marks a group of [server configuration modules](server-configuration-code.md) — and possibly default parameter values — to apply together to a server, defining what that server is for. An `application-server` role, for instance, might bundle Tomcat, a monitoring agent, a logging agent, and network hardening, plus a default inbound port.

Roles can be composed two ways: assigning several narrow, single-purpose roles to one server (`ApplicationServer`, `MonitoredServer`, `PublicFacingServer`), or defining fewer, broader roles each server gets exactly one of. A common middle ground is role inheritance — a `base-role` with software and configuration every server needs (hardening, monitoring, logging agents), with more specific roles (`application-server`, and in turn `shopping-service-server`) including the base role and layering their own modules and parameters on top.

Poorly managed roles become as messy as any other unstructured code, so the same design discipline that applies to [server configuration modules](server-configuration-code.md) generally — cohesion, avoiding duplication, clear single responsibility — applies to how roles are composed. Roles are also the natural boundary for baking configuration into a [server image](server-image-as-code.md) ahead of time, versus applying it when [creating a new server instance](baking-vs-frying-server-configuration.md).
