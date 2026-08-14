---
type: concept
title: "Pattern: Block/Rescue/Always Error Handling in Convergence Code"
description: Grouping a set of convergence tasks so a non-essential step's failure can be caught and handled without aborting the whole run, mirroring try/except/finally from general-purpose languages.
sources:
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 5"
---

By default, a failed task in a convergence run stops the whole run against that host — appropriate when every task is essential, but too blunt when a run includes steps that are genuinely optional, such as registering a newly-provisioned server with an external monitoring service. A block/rescue/always structure groups tasks into three phases, deliberately analogous to try/except/finally: tasks in the primary block run first; if any of them fails, control passes to a rescue phase instead of aborting the run (a rescue that just logs the failure, for instance, lets the rest of the run continue); and a final phase runs unconditionally regardless of whether the primary block succeeded or the rescue phase had to handle a failure.

Grouping tasks into a block also lets shared task-level parameters — a `when` condition, a privilege-escalation flag, a loop — be applied once to the whole group rather than repeated on every task inside it, which is a secondary but genuinely useful benefit distinct from the error-handling behavior itself.

The explicit caution that comes with this pattern: it's easy to over-use, the same way exception handling is easy to over-use in general-purpose code, turning a convergence run into a tangle of nested failure paths that's harder to reason about than the failure it was meant to handle gracefully. Before reaching for block/rescue/always, check whether a precise [task-level failure condition](idempotent-infrastructure-code.md) (asserting exactly what counts as a real failure, rather than trusting a step's default exit-code behavior) or a different task structure would solve the same problem more simply — reserve the block structure for genuinely optional steps whose failure shouldn't take down everything else.
