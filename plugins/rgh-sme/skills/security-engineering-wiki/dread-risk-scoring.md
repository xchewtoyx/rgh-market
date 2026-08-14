---
type: concept
title: DREAD Risk Scoring
description: >
  Score each identified threat 0–10 across five categories — Damage,
  Reproducibility, Exploitability, Affected users, Discoverability — and
  average them into one comparable number so mitigation effort can be
  ranked instead of argued about.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 9"
---

# DREAD Risk Scoring

A structured enumeration like [STRIDE](stride-threat-classification.md)
routinely produces more threats than can be fixed at once, and the
threats are rarely comparable on their face — a rare-but-catastrophic
issue and a common-but-minor one don't rank themselves. DREAD gives each
threat a score, 0–10, in five categories, then averages them into a
single number:

- **Damage** — how severe is the impact if the threat is realized?
- **Reproducibility** — how reliably can the attack be repeated?
- **Exploitability** — how much skill or resource does exploitation take?
- **Affected users** — what fraction of users or systems are exposed?
- **Discoverability** — how easily would an attacker find this threat?

The average gives a rough, comparable priority ranking across otherwise
unlike threats, which is the point: it's a triage tool for ordering
mitigation work, not a precise risk measurement, and categories like
discoverability are judgment calls that will vary between reviewers. Use
it to make the ranking explicit and arguable rather than to produce a
number precise enough to defend past one decimal place.

This operates one level down from [assessing attacker risk](assessing-attacker-risk.md):
that note calibrates how much to trust your read of the adversary in
general (don't assume low sophistication, don't assume attribution);
DREAD takes a specific, already-identified threat and scores it for
relative urgency once the adversary calibration is in place.
