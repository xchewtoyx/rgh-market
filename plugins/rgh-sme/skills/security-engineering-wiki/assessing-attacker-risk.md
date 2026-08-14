---
type: concept
title: Assessing Attacker Risk
description: >
  Five calibration rules for adversary risk: you may be a target without
  knowing it, sophistication is not required for success, don't
  underestimate resources, attribution is hard, and attackers may not fear
  being caught.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 2"
---

# Assessing Attacker Risk

When weighing the risk posed by [attacker profiles](attacker-profiles.md)
and [motivations](attacker-motivations.md), apply five considerations:

- **You may not realize you're a target.** Small organizations and those
  holding nothing "sensitive" can still be leveraged for a larger attack —
  Adobe was breached specifically so attackers could sign malware with its
  legitimate code-signing certificate. Ask what assets you hold that serve
  an attacker directly *or* as a stepping stone against someone else.
- **Sophistication is not a predictor of success.** Attackers choose the
  simplest, cheapest method that meets the goal; prominent intelligence
  operations run on plain phishing. Cover the basics (e.g. two-factor
  authentication) before worrying about exotic threats like firmware
  backdoors.
- **Don't underestimate your adversary.** Well-funded attackers will go to
  extraordinary lengths (intercepting hardware shipments to implant
  backdoors) — though such cases are the exception, consider what your
  adversary is willing to spend.
- **Attribution is hard.** Attackers disguise motive and identity
  (NotPetya posed as ransomware while acting as targeted destruction).
  Focus on countering [TTPs](attacker-ttps.md) before worrying about who
  the attacker is.
- **Attackers aren't always afraid of being caught.** International legal
  reality — especially for state-employed actors — means identification
  rarely equals accountability. Deterrence-by-prosecution is not a
  control.

The strategic aim against a stronger adversary is economic: make yourself
expensive enough to attack that the adversary must spend significant
resources — raising their risk of exposure — or lose the incentive
entirely. Even a small, inconspicuous adversary with anonymity and ample
time can do disproportionate damage, and every organization additionally
carries [insider risk](insider-risk.md).
