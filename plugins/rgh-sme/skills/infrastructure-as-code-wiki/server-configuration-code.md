---
type: concept
title: Server Configuration Code
description: Code that installs and configures the software, files, and accounts on a server instance, organized into modules and roles rather than sprawling ad hoc scripts.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 11"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 6"
---

Server configuration tools (Ansible, CFEngine, Chef, Puppet, Saltstack) manage what's installed and set up on a server: the operating system's packages, configuration files that control system and application behavior, and — treated as opaque data the tool doesn't try to manage — logs and other content the running system generates itself. This split matters because it tells a configuration tool what it should be enforcing consistency over versus what it should leave alone.

Most server configuration code is organized into modules focused on a single, cohesive concern (a module for Tomcat, a module for a monitoring agent), following the same [separation-of-concerns](infrastructure-component-coupling-and-cohesion.md) thinking that applies to any infrastructure component. Many teams split these further into *library modules* (reusable, parameterized building blocks) and *application* or *wrapper* modules (which import library modules and set their parameters for a specific purpose) — the same distinction as [facade modules](facade-module-pattern.md) at the stack level. [Server roles](server-roles.md) group modules together to define what a given server is *for*.

Ansible's concrete instance of this module unit is the **role**: a self-contained, conventionally-structured directory (tasks, handlers, default and fixed variables, files, templates, and a metadata file declaring which other roles it depends on) that a playbook composes by listing which roles to apply to which hosts, each role living "in its own isolated world" and reusable across any server or group that needs it. A role's default variables are its equivalent of a library module's parameters: a calling playbook can override them to customize behavior, while variables the role author intends to always hold means to change the role's own code, not override it, live separately with higher precedence than the overridable defaults. [Handlers](deferred-handler-notification-pattern.md) are first-class inside a role too, so a role can trigger its own deferred restart/reload actions without depending on the calling playbook to define them. Reusable roles are commonly published to a community or internal registry for others to install and pin by version — see [evaluating third-party infrastructure modules](evaluating-third-party-infrastructure-modules.md) for the trust and versioning discipline that applies once a role comes from outside the team. How a role's own task files get split and recombined internally is itself a [static-vs-dynamic code inclusion](static-vs-dynamic-code-inclusion.md) decision.

Server configuration code needs the same versioning and progressive-delivery discipline as any other infrastructure code — see [build-time, delivery-time, and apply-time project integration](build-time-project-integration-pattern.md) for how a server's constituent modules get combined into a working configuration, and [testing server code](progressive-testing-for-infrastructure.md) for how the general progressive-testing approach adapts to modules that tend to be small and declarative.
