---
type: concept
title: Deployment Script Design Principles
description: >
  Deployment scripts should be parameterized, environment-abstracted, fail
  loudly on any error, log every action, and share common logic through
  reusable libraries rather than duplicating it per environment.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 6"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 9"
---

# Deployment Script Design Principles

Design rules that keep deployment automation reliable enough to trust with
production, in support of a [repeatable deployment process](repeatable-deployment-process.md):

- **Parameterization**: the script accepts environment-specific values (target
  host, port, DB credentials, environment name) as parameters rather than
  hardcoding them — the mechanism this feeds is
  [configuration injection](configuration-injection.md).
- **Environment abstraction**: OS-specific commands are isolated behind
  standard abstraction layers or functions, so the same script logic works
  across platforms without branching everywhere on OS.
- **Strict error handling**: the script must detect and fail explicitly on any
  error (e.g. `set -e` in shell, explicit return-code checks). Never swallow
  an error or let a failed step proceed silently — a deployment script that
  reports success despite a partial failure is worse than one that has no
  error handling at all, because it hides the problem.
- **Deployment log audit**: every execution logs all actions taken, target
  hosts, executed commands, timestamps, and return codes, to both stdout and a
  durable audit log — this is what makes a failed deployment diagnosable after
  the fact instead of a mystery.
- **DRY**: extract common build/deployment logic into reusable libraries or
  plugins rather than duplicating near-identical scripts per project or
  environment; duplicated deployment logic drifts out of sync the same way
  manually managed environments do — see [environment drift](environment-drift.md).

## Separate provisioning from deployment

Split environment provisioning (installing OS packages, runtimes, and
middleware dependencies) into its own script or playbook, distinct from the
one that deploys application code. The two change at very different
frequencies — provisioning rarely changes once an environment's shape is
settled, while deployment happens on every release — and running only the
deployment script on routine releases (rather than the full provisioning
sequence every time) is both much faster and lower-risk, since it touches far
fewer moving parts per run. This mirrors
[build once, deploy everywhere](build-once-deploy-everywhere.md)'s separation
of concerns: provisioning establishes the environment an artifact runs in;
deployment places the artifact into it. Conflating the two into one script
makes routine deploys pay the cost of full re-provisioning every time.
