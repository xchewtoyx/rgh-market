---
type: concept
title: Security Incident Recovery
description: >
  Planning and executing recovery from an attack — separate recovery
  teams, complete scoping, checklists, and hard questions about attacker
  reaction, compromised tooling, variants, and reintroduced vulnerabilities.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 18"
---

# Security Incident Recovery

Recovering from a security incident differs from outage recovery in one
way above all: a persistent attacker can leverage ongoing access or
reengage *during* your recovery. Recovery is usually executed not by
security specialists but by the people who build and run the systems
daily — SREs, developers, sysadmins — partnered bidirectionally with the
[investigation](digital-forensics.md) under the incident's remediation
lead ([crisis management](security-crisis-management.md)).

**Logistics**: staff recovery separately from investigation (investigators
are exhausted, phases overlap, skills differ). Use formal teams, frequent
syncs, shared checklists, peer review — Agile-style sprints work. Keep
recovery documentation accessible to the team but *not* the attacker
(clean infrastructure, air-gapped storage, even notecards until
responder machines are known-clean; see
[incident OpSec](incident-operational-security.md)), and keep an audit
trail of recovery actions so mistakes can be unwound — dedicated note
takers or technical writers help.

**Timeline**: mission-critical infrastructure (or a DoS) may demand
near-immediate recovery; a fully embedded attacker means planning starts
immediately but *execution* waits for understanding. Never start without
a plan and checklists; begin post-recovery work immediately after, before
details fade.

**Scoping** requires a complete list of affected systems/networks/data
plus enough attacker-[TTP](attacker-ttps.md) knowledge to find related
resources — a compromised config-distribution system pulls every system
it pushed to into scope. Classify actions as short-term mitigations vs.
long-term strategic changes, mapping each attacker behavior to a defense.

**Planning questions** (the deep-dive checklist):

- **How will the attacker respond?** See
  [ejecting the attacker](attacker-ejection.md) — the timing decision is
  its own concept.
- **Is your recovery tooling itself compromised?** A compromised config
  server must be remediated before rebuilding the laptops it manages; a
  backdoored backup-restore tool before restoring data. Recovering assets
  on attacker-controlled infrastructure invites immediate re-compromise —
  build a *clean*, isolated version of the asset (quarantined network,
  fresh OS, manual bootstrap) first.
- **What variants exist?** One exploited buffer overflow on one server
  implies 20 more servers running the same software, plus related
  vulnerability classes in custom code and shared libraries; fold broad
  upgrades into recovery.
- **Will recovery reintroduce attack vectors?** Golden images containing
  the vulnerable software, configs restored from a repository the
  attacker modified, or backups that captured the attacker's changes all
  regress the recovery. Know *when* the attacker started modifying
  things; if you can't, rebuild in parallel from scratch. Destroy or
  quarantine backups containing attacker artifacts (for later analysis) —
  see [backup and restore integrity](backup-and-restore-integrity.md).
- **What do mitigations cost?** Resilient design gives cheap options
  (in-place module fixes, container replacement). When forced into ugly
  short-term mitigations (a manual router deny rule bypassing review and
  version control), interrogate the technical debt: how long will it
  live, who owns paying it off, does it burn error budget, how is it
  *visibly marked* as temporary, how can a future engineer prove it
  removable, what happens if it accidentally persists (the "two-week"
  database quarantine that lasts six months), and has a domain expert
  poked holes in the answers?

**Checklists** turn the plan into execution: each item a task with
required skills, specific tools and commands, ordering, and
cleanup/rollback steps if the plan fails — enabling parallel claiming of
work and giving the IC confidence in what "done" means. Complex incidents
parallelize into per-problem teams (email, source code, SSL keys,
customer data, financial reconciliation), each with its own checklist,
all synced with the ongoing investigation.

Afterwards: the [security postmortem](security-postmortem.md).
