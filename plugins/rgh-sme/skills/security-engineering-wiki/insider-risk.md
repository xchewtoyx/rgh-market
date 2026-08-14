---
type: concept
title: Insider Risk
description: >
  The threat from people with trusted internal access — malicious,
  negligent, or accidental — and the design principles that limit what any
  insider (or an attacker wearing their account) can do.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 2"
  - title: The DevOps Handbook
    resource:
      "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 23"
---

# Insider Risk

Insiders are current or former people trusted with internal access or
proprietary knowledge. Insider risk spans malicious, negligent, and
accidental scenarios, across three categories:

- **First-party insiders**: employees, interns, executives, board
  directors. Classic cases: IP theft (a GE engineer exfiltrating turbine
  designs hidden in photos), voyeuristic or saleable access to personal
  data (hospital staff reading celebrity records), and disgruntled
  destruction (a fired employee deleting 23 virtual servers). Employment
  dynamics make this risk unavoidable.
- **Third-party insiders**: open source contributors, third-party app
  developers, partners, contractors, vendors, auditors. A contributor you
  have never met who lands a malicious or merely untested change *is* an
  insider; an API partner with privileged data access is one too. Controls:
  mandatory review and testing of all submitted code, and careful scoping
  of what API access actually confers. A cloud provider's own staff and
  hardware-disposal practices are the same category of risk, imported
  wholesale the moment you rent their infrastructure — see
  [cloud provider as a trust boundary](cloud-provider-trust-boundary.md).
- **Related insiders**: friends, family, roommates. The unlocked work
  laptop on the kitchen table, the on-call engineer's child installing
  malware that locks the machine during an outage. Define "workplace" to
  include the home.

**Why this is where security and reliability intersect most**: insiders
hold privileged access. Most reliability incidents are caused by an
insider who didn't realize their impact (faulty code, errant config); and
an attacker who takes over an employee account inherits every privilege
that employee holds. Design against both at once — the same
[least-privilege](least-privilege.md) controls that stop an attacker
wearing a hijacked account also stop the well-intentioned engineer from
accidentally deleting the customer database.

**Assume you can't determine intent.** If an insider takes a system down
and claims accident, you may never conclusively know (extreme negligence
cases need legal/HR/law-enforcement investigators). Plan for malicious and
unintended actions alike, and remember pure mistakes at scale: a stray "/"
accidentally added to a malware-site list once flagged every search result
on the planet — an automated config check would have prevented it.

**A simple threat-modeling frame**: enumerate *actor/role* (engineering,
operations, sales, legal, executives) x *motive* (accidental, negligent,
compromised, financial, ideological, retaliatory, vanity) x *action* (data
access, exfiltration, deletion, modification, injection, leak) x *target*
(user data, source code, logs, infrastructure, financials), and combine
into scenarios — "an engineer, retaliating over a review, injects a
backdoor that steals user data"; "an SRE is coerced into handing over SSL
keys". This works as a brainstorm or even a card game, and feeds the same
mitigation catalogue as external [attacker profiles](attacker-profiles.md).

Effective design concepts against insider risk:

- [Least privilege](least-privilege.md), in scope *and* duration
  ([temporary access](temporary-access.md))
- Zero-trust system management — automation and
  [safe proxies](safe-proxies.md) instead of broad direct access
- [Multi-party authorization](multi-party-authorization.md) for sensitive
  actions
- [Structured business justifications](structured-justification.md) for
  sensitive access
- [Auditing and detection](audit-log-design.md) of access and
  justifications
- Recoverability after destructive action — see
  [design for recovery](design-for-recovery.md)

**Detection has to carry weight that prevention structurally can't.** A
sufficiently motivated insider with genuine access can build a preventive
control blind spot on purpose: a documented case involved a developer who
planted a backdoor in ATM code, deployable via an undocumented
"maintenance mode," that let them withdraw cash without leaving a trace
code review or the standard change-approval process would catch —
review and approval both assume the reviewer can recognize malicious
intent in the code, which a competent insider can defeat by
construction. The fraud was caught not by either preventive control but
by [production telemetry](security-telemetry-visibility.md): someone
doing a routine operations review noticed ATMs entering maintenance mode
at unscheduled times. The lesson generalizes past insider fraud
specifically — preventive controls (review, approval, separation of
duty) and detective ones (telemetry, audit logs) catch different failure
classes, and an insider threat model that relies solely on the
preventive side is trusting the exact control a capable insider is best
positioned to defeat.
