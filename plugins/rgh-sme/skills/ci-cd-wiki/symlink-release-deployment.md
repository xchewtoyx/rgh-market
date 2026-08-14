---
type: concept
title: Symlink-Based Release Deployment
description: >
  Deploying each release into its own timestamped directory and atomically
  repointing a "current" symlink at it, so activating a new release — or
  rolling back to the previous one — is a single fast filesystem operation.
sources:
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 9"
---

# Symlink-Based Release Deployment

Popularized by Capistrano. Each deployment unpacks the new release into its
own directory (often timestamp- or version-named) alongside previous
releases, rather than overwriting the running application in place. A
"current" symlink points at whichever release directory is live; cutting
over to the new release is just repointing that symlink, and rolling back to
the previous release is repointing it back — both near-instant, atomic
filesystem operations rather than a re-deploy.

Persistent items that must survive across releases (logs, user uploads,
long-lived cache directories) live outside any single release directory and
are symlinked into each new release directory at deploy time, so they aren't
duplicated or lost on cutover.

## Where this fits among deployment patterns

Lighter-weight than [blue-green deployment](blue-green-deployment.md) — there
is only one running environment, not two full parallel ones — but it gives
much of the same benefit for a single server or a simple fleet: fast,
low-risk activation and near-instant [rollback](rollback-and-roll-forward.md)
without needing double the infrastructure. It doesn't address zero-downtime
across a *fleet* the way [rolling deployment](rolling-deployment.md) does; the
two combine naturally — each host in a rolling deploy can use symlink
activation locally to make its own per-host cutover atomic.
