---
type: concept
title: Static vs Dynamic Code Inclusion
description: The choice between resolving an included file of infrastructure code before a run starts, so it can be fully inlined and analyzed ahead of time, versus resolving it during execution, so it can react to state established earlier in the same run.
sources:
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 6"
---

Splitting infrastructure code across files (see [server configuration code](server-configuration-code.md)) raises a question independent of *how* the split happens: *when* is the included file's content actually resolved? **Static inclusion** expands the included file into the calling code before the run begins — as if it had been pasted in place at parse/plan time. **Dynamic inclusion** instead resolves the included file during execution, after some of the calling code has already run.

Static inclusion is easier to reason about and to tool: because everything is known before execution starts, a linter, a `--syntax-check`-style validator, or a plan/preview step can see the whole expanded tree and analyze it as a single unit. Its limitation is exactly that up-front resolution: it cannot use a value that only becomes known once the run is under way — for example, a variable set by an earlier task in the same run — because at resolution time no run has happened yet. It also generally cannot use a variable inside the *name* of the file being included, since which file to include is itself part of what gets resolved statically.

Dynamic inclusion trades that analyzability away for the ability to react to runtime state: the file (or even its filename) to include can depend on a fact discovered earlier in the same run, on the result of a prior task, or on whether an optional file happens to exist on disk at that point — enabling patterns like "include this extra configuration only if this optional file is present," which static inclusion cannot express at all. The cost is that a full picture of what a run will actually do can only be known by running it (or by tracing the dynamic conditions by hand), which is a strictly weaker guarantee than static inclusion's up-front knowability.

Tools that offer both should default to static inclusion and reach for dynamic inclusion only where the reactive capability is genuinely needed — the same instinct behind preferring [declarative code](declarative-vs-imperative-infrastructure-code.md) and reserving imperative escape hatches, like the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md), for cases that actually require them. Ansible's own history illustrates the cost of blurring this line: it originally offered one include directive that was always resolved statically, later made resolution dynamic by default, then let a single flag toggle between the two behaviors on the same directive — before eventually splitting into two explicitly-named directives (one purely static, one purely dynamic) because overloading one keyword with two different resolution-time behaviors had become a recurring source of confusion.
