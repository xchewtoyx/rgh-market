---
type: concept
title: Idempotent Infrastructure Code
description: The property that reapplying the same infrastructure code any number of times produces the same result, with no cumulative side effects — a prerequisite for safely applying code continuously.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 4"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 1"
---

Code is idempotent if running it once, or running it ten times, leaves the system in the same state. A non-idempotent shell command that appends a user entry to `/etc/passwd` creates ten duplicate entries if run ten times; a declarative statement that says "this user should exist with these properties" produces exactly one entry no matter how many times it runs, because the tool reconciles the declared state against the current state rather than blindly re-executing an action.

Idempotency is what makes it safe to reapply infrastructure code repeatedly and unattended, which is the basis of [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md) — a core defense against [configuration drift](configuration-drift.md). Non-idempotent code is exactly the kind of thing that makes teams afraid to run automation on a schedule, feeding the [automation fear spiral](automation-fear-spiral.md).

[Declarative infrastructure languages](declarative-vs-imperative-infrastructure-code.md) are typically idempotent by construction, since the tool computes the difference between declared and actual state on every run. Imperative infrastructure code has to be written carefully to achieve the same property, usually by checking current state before acting rather than executing actions unconditionally.

Idempotency isn't just a property to test for after the fact — it falls naturally out of how an operation's contract is phrased. An imperative "create this resource" or "delete this resource" has an inherent error case baked into its very definition: called a second time, "create" finds the resource already there and "delete" finds it already gone, and something has to decide whether that's success, failure, or an exception to catch. A declarative "ensure this resource exists" or "ensure this resource is absent" has no equivalent error case at all — the already-satisfied state simply *is* success, because the operation was never phrased in terms of a transition that could fail to apply twice. This is why reconciliation-based tools default to idempotence almost for free: declaring desired state, rather than the action that would produce it from one specific starting point, defines the "already done" case out of existence instead of leaving it as a special case for every caller (or every module author) to handle.

Ansible defines idempotence explicitly as "the ability to run an operation which produces the same result whether run once or multiple times," and treats it as a near-universal property of its built-in modules — a task installing a package or ensuring a service is running reports no change on a rerun if the declared state already holds. This idempotence is a property of each module's implementation, not of Ansible's task-execution model itself: Ansible cannot infer whether an arbitrary shell command changed anything, so tasks using its escape-hatch `command`/`shell` modules are always reported as changed unless the author explicitly tells Ansible otherwise (via `changed_when`, evaluated against the command's registered output) or gates the task's execution on a precondition (via `when`, checking a registered result before deciding whether to act at all). This is the concrete mechanism by which imperative, non-idempotent-by-default operations are made to behave idempotently within an otherwise declarative tool.
