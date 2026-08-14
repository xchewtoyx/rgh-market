---
type: concept
title: Threat Intelligence
description: >
  Reports, indicators of compromise, and malware analyses from security
  firms that show how real attackers currently operate, giving defenders
  early warning and machine-consumable detection inputs.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 2"
---

# Threat Intelligence

Threat intelligence describes attacks observed in the wild, in three forms
serving different purposes:

- **Written reports** narrate how attacks progressed and what the attacker
  intended — best for understanding adversary behaviour; quality varies
  with the researchers' hands-on expertise.
- **Indicators of compromise (IOCs)** are finite attack attributes — the
  IP hosting a phishing site, the SHA256 of a malicious binary — usually
  structured (e.g. STIX, exchanged via TAXII) and delivered by automated
  feed so detection systems can consume them programmatically.
- **Malware reports** reverse-engineer attacker tools (IDA Pro, Ghidra),
  yielding capability insight, IOCs, and attributes for cross-correlating
  unrelated attacks.

Value to a defender: knowing what attacks peer organizations in your
industry face is early warning of what you may face — feed it into
[risk assessment](assessing-attacker-risk.md) and map observed
[TTPs](attacker-ttps.md) against your controls. Buy from a reputable firm
with customer references; many firms also publish free annual trend
reports (e.g. Verizon DBIR).
