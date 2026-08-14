---
type: concept
title: Least Privilege
description: >
  Grant every human, service, and machine only the minimum access needed for
  the task at hand, because mistakes, compromise, and malice must all be
  assumed possible.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 11"
---

# Least Privilege

Users — human or automated — should have the minimum access needed to
accomplish a task. The justification is not distrust of colleagues but the
refusal to rely on human perfection: engineers make mistakes, fat-finger
commands during incidents, fall for phishing, and occasionally act
maliciously. Design the system so that any of these bad actions has minimal
or no impact, rather than hoping they never happen.

A useful thought exercise when reviewing a design: if you *wanted* to do
something evil with your current access, what could you do? Would you be
detected? Could you cover your tracks? And even with good intent, what is
the worst mistake someone with equivalent access could make one typo away
from causing?

Least privilege is most effective (and cheapest) when applied at design
time; retrofitting it onto a running system is expensive. It should extend
through every authentication and authorization layer, and it rejects two
common shortcuts:

- **Implicit authority in tooling** — automation that connects over a broad
  API (e.g. full SSH/POSIX access) implicitly holds far more power than its
  task requires, so a bug or credential compromise in the tool becomes a
  fleet-wide compromise. The structural fix is
  [small functional APIs](small-functional-apis.md) and
  [trust segmentation](trust-segmentation.md).
- **Ambient authority** — standing broad access such as the ability to log
  in as root. Prefer scoped, [temporary access](temporary-access.md) so that
  when a destructive command is issued by accident, the fewer permissions
  held, the better. Where access can't be usefully time-bounded upfront,
  [unused permission revocation](unused-permission-revocation.md) prunes
  it after the fact instead. The same logic applies to a running process,
  not just a human session: a container or service that runs as root, with
  a writable root filesystem and unrestricted network egress, holds far
  more standing authority than its job requires — running as a dedicated
  non-root user, mounting the filesystem read-only, and restricting egress
  to only the downstream services actually called are the process-level
  instance of removing ambient authority, so that compromising the
  application's code doesn't hand the attacker the whole host.

Applying least privilege proportionately starts with
[classifying access by risk](access-classification-by-risk.md) — not all
data or actions deserve the same controls. Enforcement rests on a clear
[authentication/authorization split](authorization-policy-framework.md),
with escape valves for legitimate exceptional need
([breakglass](breakglass.md),
[multi-party authorization](multi-party-authorization.md)) and detection of
misuse via [audit logs](audit-log-design.md).

The model has real costs: granular policy is complex to manage (you must
always be able to answer "who has access to X?" and "what does user Y have
access to?"), authorization steps can slow users down, and security
decisions become only as good as the data (group membership, client
attributes) feeding them. A strict model suits sensitive data and admin
actions; deliberately relaxed access elsewhere (e.g. broad internal
source-code visibility) can pay for itself in collaboration and in making
inappropriate changes harder to hide. Verify the posture with
[testing of and with least privilege](testing-least-privilege.md).
