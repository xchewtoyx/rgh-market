---
type: concept
title: Data Continuity Strategies
description: Four complementary techniques — lock, segregate, replicate, and reload — for preserving data across the destruction and rebuilding of the infrastructure that hosts it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

Practices that treat infrastructure as freely disposable and rebuildable — [reproducibility](reproducibility-principle.md), [immutable servers](immutable-server-pattern.md), [continuous disaster recovery](continuous-disaster-recovery.md) — run into a real limit at data: destroying and rebuilding the infrastructure that hosts stateful data risks losing or corrupting it, and many incremental-delivery techniques that rely on rollback don't straightforwardly apply to data schema changes. Four approaches, often combined, address this:

- **Lock** — mark specific resources so the stack tool refuses to destroy them, letting a human intervene manually instead. This is the weakest option: it can leave a stack partially modified if a change hits a locked resource mid-apply, and by design it invites manual intervention, which invites manual mistakes — better to find a way to automate the change safely than to lean on locking as a long-term strategy.
- **Segregate** — split data-holding resources into their own [stack](infrastructure-stack.md), per the [micro stack pattern](micro-stack-pattern.md), so compute can be destroyed and rebuilt freely (detaching and reattaching the data volume) without disturbing the data. Storing data in a managed database service can narrow the problem further, potentially offloading continuity to the platform entirely.
- **Replicate** — spread data across multiple instances (a distributed database cluster, for example) so a rebuilt node can resynchronize from its peers. This works as a first line of defense but fails if too many nodes are lost simultaneously — such as in a major hosting outage — so it needs a second mechanism as backstop.
- **Reload** — back up data to more durable storage and restore it after rebuilding, the best-known and most universal approach. Periodic backups lose whatever changed between the backup and the recovery, which can be minimized (or eliminated) by streaming changes continuously, such as a database transaction log, to durable storage. Snapshotting a disk volume before a risky change is a cheap, automatable form of this. "Untested backups are the same as no backups" — exercise the restore path itself in the pipeline or as a chaos experiment, the same discipline any other infrastructure code gets.

The strongest continuity design typically combines segregate, replicate, and reload: segregation creates room to manage the rest of the system flexibly, replication keeps data available most of the time, and reload is the backstop for the more extreme situations replication alone can't cover.
