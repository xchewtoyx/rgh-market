---
type: concept
title: Attacker Motivations
description: >
  Security adversaries are humans with purposes — fun, fame, activism,
  money, coercion, manipulation, espionage, destruction — and knowing why
  someone would attack a system shapes how to design and defend it.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 2"
---

# Attacker Motivations

Unlike reliability adversaries (hardware failure, success disasters, errant
config, a cat chewing a power cable), security adversaries are human, and
their actions are calculated. Reasoning about the people behind attacks —
why they would target *this* system — equips both proactive design and
incident response. Common motivations:

- **Fun** — undermining security for the joy of knowing it can be done.
- **Fame** — notoriety for technical skill.
- **Activism** — broadcasting a message, typically political.
- **Financial gain** — theft, ransom, fraud.
- **Coercion** — forcing a victim to knowingly do something they don't
  want to do.
- **Manipulation** — creating an outcome or changing behaviour, e.g.
  publishing false data.
- **Espionage** — gaining valuable information (state or industrial).
- **Destruction** — sabotage, data destruction, or taking systems offline.

Motivations combine in one actor: the same indicted operator was linked to
WannaCry ransomware (financial), the Sony Pictures compromise (coercion and
destruction), and utility intrusions (espionage). Avoid stereotypes —
anyone with time, knowledge, or money can undermine a system, from
governments buying exploitation software to a hobbyist with a $20 tool.

Design use: for each asset and workflow, ask which motivations it could
serve. A money-transfer processor should expect financially motivated
state-level actors (the SWIFT bank thefts are the template), not just
opportunistic fraudsters. Feed the answers into
[attacker profiles](attacker-profiles.md) to identify *who*, and into
[risk-assessment considerations](assessing-attacker-risk.md) to calibrate
how much defense is proportionate. For the adversaries already inside the
trust boundary, see [insider risk](insider-risk.md).
