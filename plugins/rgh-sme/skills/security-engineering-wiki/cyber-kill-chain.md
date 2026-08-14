---
type: concept
title: Cyber Kill Chain
description: >
  Laying out the sequential stages of an attack — reconnaissance, entry,
  lateral movement, persistence, goals — so a defensive control can be
  placed at each stage.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 2"
---

# Cyber Kill Chain

A kill-chain framework plots the steps an attacker must take to achieve
their goal, so defenses can be mapped stage by stage. Lockheed Martin's
trademarked version has seven stages; a simplified five-stage form works
well:

| Stage | Attack example | Example defenses |
| --- | --- | --- |
| **Reconnaissance** — surveilling the target's weak points | Search engine reveals employee email addresses | Educate employees about online safety |
| **Entry** — gaining network/system/account access | Phishing yields credentials; attacker signs in to the VPN | Two-factor auth (security keys) on the VPN; VPN only from managed devices |
| **Lateral movement** — hopping between systems/accounts for more access | Remote login to other systems with the stolen credentials | Employees can log in only to their own systems; 2FA on multiuser systems |
| **Persistence** — ensuring ongoing access | Backdoor installed for remote access | Application allowlisting |
| **Goals** — acting on the objective | Documents exfiltrated via the backdoor | [Least-privilege](least-privilege.md) access to sensitive data; account monitoring |

Two design payoffs:

- **Every stage is a detection and prevention opportunity.** A multistep
  methodology gives the defender multiple contact points; breaking any
  link stops the chain. This is the attack-side rationale for
  [defense in depth](defense-in-depth.md).
- **The chain structures review.** For a given asset, walk the stages and
  ask what control exists at each — gaps cluster visibly.

For finer-grained cataloguing of *how* each stage is carried out, expand
into [attacker TTPs](attacker-ttps.md); for evidence of which chains real
attackers are running against organizations like yours, use
[threat intelligence](threat-intelligence.md).
