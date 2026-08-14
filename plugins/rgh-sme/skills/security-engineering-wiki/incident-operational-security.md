---
type: concept
title: Incident Operational Security
description: >
  Keeping response activity secret from a watching adversary — clean
  communication channels, no logins to compromised hosts, no touching
  attacker infrastructure — until you choose to trade secrecy for safety.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 17"
---

# Incident Operational Security

Operational security (OpSec) during a
[security crisis](security-crisis-management.md) means keeping your
response secret from an adversary who may be watching and working against
you. An attacker who learns they're discovered either goes quiet —
costing you visibility into their footholds — or torches what they can on
the way out. Establish the OpSec plan *before* any incident; once a
secret is lost you can't get it back. The IC owns setting, communicating,
and enforcing confidentiality rules; brief every responder explicitly and
have them acknowledge — people can't keep secret what they don't know is
secret.

**Common mistakes**:

- Discussing or documenting the incident in a medium the attacker may
  monitor (your own email server, in scope of the breach).
- Logging into compromised servers — donating admin credentials to an
  attacker scraping passwords from memory.
- Touching attacker infrastructure: downloading their malware from an
  investigation machine, port-scanning or DNS-resolving their hosts —
  novice moves that stand out in the attacker's logs.
- Locking accounts or changing passwords of affected users before the
  investigation is complete; taking systems offline before the attack's
  scope is understood.
- Letting analysis workstations accept the same credentials the attacker
  may have stolen.
- **Helpful tools that betray you**: chat clients, spreadsheets, and doc
  editors auto-fetch and cache URLs — an attacker's log showing
  `"GET /malware_c2.gif ... Chatbot-LinkExpanding 1.0"` announces your
  discovery. Habitually write indicators defanged (`example[dot]com`),
  even outside incidents.

**Good practices**: meet in person where possible; if you need
chat/email, stand up a *clean environment* — e.g. a fresh cloud tenant
unassociated with the organization, accessed from freshly built machines
unlike your regular fleet ([emergency access](emergency-access.md)
overlaps). Pre-deploy remote forensic agents or key-based access so
evidence collection never exposes login secrets
([digital forensics](digital-forensics.md)). For each investigative step,
ask what a shrewd attacker would conclude from observing it (a sudden
rush of group-policy tightening on a compromised Windows server reads as
"they found me").

**The exception — trading OpSec for the greater good**: with imminent,
clearly identifiable risk (vital data, systems, or lives; or a trivially
exploitable, widely known bug), loudly disabling the system may be the
right call even though it reveals the response. That decision belongs to
executives with the IC as resident expert.
