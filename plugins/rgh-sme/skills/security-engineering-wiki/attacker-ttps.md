---
type: concept
title: Attacker TTPs
description: >
  Tactics, techniques, and procedures — formal catalogues like MITRE
  ATT&CK that describe concretely how attackers carry out each stage of an
  attack, so defenses can be built per method.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 2"
---

# Attacker TTPs

Tactics, techniques, and procedures (TTPs) categorize attacker methods at
a fine grain. MITRE's ATT&CK framework expands each stage of the
[cyber kill chain](cyber-kill-chain.md) into detailed, formally described
steps — hundreds to thousands of concrete methods. Example: under
Credential Access, ATT&CK notes that a user's `.bash_history` may contain
accidentally typed passwords an attacker can simply read.

Uses in design and defense:

- **Per-method defenses.** Because each technique is described concretely,
  a defender can check "do we have a control against this?" method by
  method, instead of hand-waving about attacker sophistication.
- **Focus on how, not who.** Attribution is hard — attackers disguise
  motive and identity (NotPetya masqueraded as financially motivated
  ransomware while functioning as targeted destruction delivered through a
  compromised software-update channel). Since identity and intent may
  never be clear, prioritize understanding and countering TTPs over
  identifying the actor (see
  [assessing attacker risk](assessing-attacker-risk.md)).
- **Cross-correlating attacks.** Shared TTPs and tool attributes let
  analysts connect otherwise unrelated incidents — the same lens
  [threat intelligence](threat-intelligence.md) reports use.

The tradition traced back to Stoll's "Stalking the Wily Hacker" (1986):
careful study of an adversary's specific procedures is what turns a
mysterious intrusion into a defensible pattern.

Many of the most reliable TTPs target the person holding a credential
rather than any technical control at all — the practical defense is
[out-of-band verification of credential requests](social-engineering-verification.md).
