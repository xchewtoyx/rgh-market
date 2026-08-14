---
type: concept
title: Service Decommissioning Checklist
description: Retiring a service safely requires an ordered, cumulative checklist covering user removal, resource deallocation, and resource disposal, because skipped or misordered steps leave orphaned resources or break still-dependent systems.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

Decommissioning a service is the mirror image of launching one, and shares the same underlying risk: it happens rarely enough for any given team that institutional memory of "everything that needs to happen" fades between occurrences, so steps get missed. The consequence of a missed step here is different from a missed launch step, though — it's not a customer-visible failure but a silent, lingering cost: orphaned resources that nobody notices are still allocated, still billed, or still a security exposure.

## Three Ordered Phases

- **User removal**: migrate or notify remaining users, and archive or hand off their data. This is often a product-management task rather than a purely technical one.
- **Resource deallocation**: turn off DNS entries, power down machines, tear down database connections, and so on. Order matters here — DNS entries typically shouldn't be pulled until the machine they point to is truly unused, and shared network connectivity can't be removed while some other, unrelated service still depends on it. Deallocating out of order can cause an outage in a system that was never meant to be affected by this decommissioning at all.
- **Resource disposal**: securely erase data and repurpose, sell, or scrap the underlying hardware.

## The Cumulative Checklist Countermeasure

The same countermeasure used for infrequent [service launches](launch-vs-handoff-readiness-reviews.md) applies here: maintain one decommissioning checklist that grows every time a decommission surfaces a new gotcha (a dependency nobody remembered, a resource type nobody thought to reclaim), rather than relying on whoever happens to run the next decommission to remember or rediscover it. Because both launch and decommissioning checklists exist to fight the same "this happens too rarely for anyone to just remember" problem, they benefit from the same organizational-memory discipline and, ideally, the same visible, easy-to-find home.
