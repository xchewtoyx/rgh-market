---
type: concept
title: Attacker Profiles
description: >
  Illustrative classes of attacker — hobbyists, vulnerability researchers,
  nation-states, hacktivists, criminals, automated systems — each implying
  different targeting logic and proportionate defenses.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 2"
---

# Attacker Profiles

Profiles are illustrative, not definitive — no two attackers are alike —
but they help a designer ask "who would target this system, and what
would defending against them cost?"

**Hobbyists** hack for curiosity and fun, usually within personal ethics
that stop short of harm. They find flaws designers missed and can be
allies; their thinking is worth borrowing.

**Vulnerability researchers and red teams** use security expertise
professionally, within disclosure norms (or with explicit permission), to
make systems better. Treat them as allies: their findings are evidence
about your real posture.

**Governments and law enforcement** gather intelligence, support military
operations (Stuxnet destroying enrichment centrifuges), and police domestic
activity (commercial spyware turned on journalists). Signals: you build
technology other states want (chip designs), or you hold data an agency
can't easily get elsewhere — personal communications, location data
(Operation Aurora targeting Gmail accounts; Strava heatmaps revealing
secret bases). You can be a target without realizing it — Aurora hit 20+
victims across sectors, many of whom never considered themselves at
nation-state risk. Defending outright may exceed your resources; take the
long view — protect the most sensitive assets first, layer protections
over time, and aim to make the adversary spend enough to raise their risk
of exposure (see [assessing attacker risk](assessing-attacker-risk.md)).

**Hacktivists** attack to broadcast a message: defacement via a
compromised CDN, or purchased-botnet DDoS. They are vocal, take credit
publicly, and need little skill, which makes them hard to predict. If your
product hosts user content, touches politically charged issues, or is used
by activists, invest in layered controls: patching,
[DoS resilience](dos-defense-in-depth.md), and backups that restore
quickly.

**Criminal actors** range from tool-writers to buyers of click-to-attack
kits; social engineering is the cheapest and among the most effective
techniques. Examples span M&A-data theft for insider trading, ransomware,
$20 stalkerware exploiting domestic trust, and hired attacks (a telecom
employee paying to degrade a rival's network). They gravitate to the
easiest, cheapest path to their goal — so raising attack cost (the
CAPTCHA arms race is the canonical example) genuinely redirects them to
other victims.

**Automation and AI**: self-learning systems can already find, exploit,
and patch flaws without a human at the controls (DARPA Cyber Grand
Challenge). Expect some future attacks to be fully automated; the defense
is resilient design by default and the ability to iterate your security
posture automatically —
[design for a changing landscape](design-for-changing-landscape.md).

**Insiders** get their own treatment — see
[insider risk](insider-risk.md) — because their privileged access makes
them the profile where security and reliability intersect most.

Whoever the attacker, study *how* they work before worrying about who they
are: see [attacker TTPs](attacker-ttps.md) and the
[cyber kill chain](cyber-kill-chain.md).
