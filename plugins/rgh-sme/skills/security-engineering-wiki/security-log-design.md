---
type: concept
title: Security Log Design
description: >
  Logs for future investigations must be immutable, centrally collected,
  privacy-aware, selectively retained, and budgeted — because attackers
  erase traces and compromises take months to discover.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 15"
---

# Security Log Design

Before launching a service, assume any action leading to data or system
access may be in scope for a future investigation and will need auditing.
Both [debugging and security investigations](debugging-vs-security-investigation.md)
live or die on logs — structured, timestamped records (treat core/memory
dumps and stack traces the same way).

**Immutability.** Attackers erase their traces as soon as they gain a
foothold. Write logs remotely to a hardened, centralized, distributed log
server so the attacker must compromise that too (the modern line-printer
whose paper trail a remote attacker can't burn). Alteration should be
hard, and itself leave an immutable audit trail.

**Privacy shapes the design** (consult privacy/legal): *depth* —
investigations want every action, host, and timestamp, while
privacy-preserving practice discourages retaining sensitive data; agree
on policy. *Retention* — compromises take ~200 days on average to
discover, and insider-threat investigations have needed OS logs going
back years; a week of access logs may mean an intrusion simply cannot be
investigated. *Access controls* — protect logs and their metadata like
the data they describe ([least privilege](least-privilege.md)); logs are
themselves attractive targets and shouldn't contain credentials or PII
([security-reliability intersection](security-reliability-intersection.md)).
*Anonymization/pseudonymization* — can let investigators build a
session timeline without identifying the user; hard to get right.
*Asymmetric encryption* — anyone can write with the public key, only the
private key reads; daily key pairs let debuggers get small recent
subsets while preventing bulk decryption.

**What to retain**: OS logs (Windows Event, syslog, auditd — nearly free
to enable; auditd's performance cost is usually worth it); host agents /
HIDS (kernel agents see more but break more; classic antivirus has
declining value; evaluate before deploying); application logs (have
security specialists work with developers so custom apps log data
writes, ownership/state changes, account activity); cloud logs (cheap
central collection and query, but provider-predetermined coverage,
sprawling unknown assets — inventory tooling helps, e.g. mining the
billing system for cloud spend; CASBs intermediate user-to-cloud access
for control and logging); network logging (NIDS/IPS — high value, few
downsides beyond cost and alert triage; DNS query logs answer "did any
host resolve this malicious domain," support sinkholes; web-proxy logs
scan for phishing/vulnerability patterns — tailor detection narrowly to
minimize employee-privacy exposure).

**Budget for logging in advance** — an unbudgeted system quietly
accumulates 100 TB of never-used logs or, worse, keeps too little:

- Prefer high signal-to-noise sources (firewall-blocked packet logs are
  mostly worthless volume).
- Compress (log metadata is highly redundant); split warm storage
  (recent/incident-related, indexed, expensive) from cold (old,
  compressed, cheap).
- Rotate intelligently — oldest first, but keep the most important types
  longer.
- **Degrade log collection gracefully** rather than halting at capacity:
  write full-fidelity and summarized streams at collection time (e.g.
  full packet captures deleted after N days, netflow kept a year), so
  budget pressure costs fidelity, not coverage.

Iterate: after each investigation, ask what information would have
helped, and add those sources. Chance favors the prepared.
