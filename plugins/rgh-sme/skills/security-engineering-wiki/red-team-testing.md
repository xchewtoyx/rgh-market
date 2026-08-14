---
type: concept
title: Red Team, Blue Team, Purple Team
description: >
  Unannounced offensive testing against your own production systems finds
  the gaps announced audits and reviews miss, but only pays off if a
  tracked follow-up loop turns findings into fixed vulnerabilities.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 16, 20"
---

# Red Team, Blue Team, Purple Team

A **Red Team** simulates a real attacker against production, typically
with no advance notice to responders (senior leadership excepted). Because
an internal Red Team already knows the organization's infrastructure, its
exercises are far more productive than an external penetration test — it
can chain realistic pivot points the way an actual adversary would,
including human-layer attacks like phishing and social engineering, not
just technical exploitation. This is distinct from planned, cooperative
[continuous validation](continuous-validation.md): Red Team exercises are
adversarial and unannounced by design, which is what makes them measure
detection and response rather than just correctness.

**Red Team engagements are not the same thing as vulnerability scanning or
penetration testing**, and conflating them misleads you about what a clean
result means:

- *Vulnerability scanning* looks for predictable, automatable weaknesses
  in software and configuration — hours to days, narrow and mechanical.
- *Penetration testing* targets a specific product, component, or process,
  trying to find and exploit as many vulnerabilities in it as possible —
  days, narrow scope, prevention-focused with some detection coverage.
- *Red Team* engagements are goal-oriented (exfiltrate this class of data,
  test whether reconnaissance gets noticed, prove a "theoretical" issue is
  actually exploitable), broadly scoped across product/infrastructure/
  organizational boundaries, and typically run for weeks using any means
  within agreed safety limits.

None of these substitutes for the others; a clean penetration test result
says nothing about whether your detection pipeline would notice a
determined attacker crossing trust boundaries the test never touched.

**Running a Red Team program safely** requires groundwork most
organizations underestimate: get buy-in from legal and executives before
starting, and define hard boundaries up front — no access to real customer
data, no disrupting production, approximate goals with test accounts
instead. Agree in advance on a de-escalation protocol for when the Blue
Team detects the exercise, so a successful Red Team breach doesn't trigger
a real breach response (executive notifications, regulators) by mistake.
Because engagements are infrequent and often run by engineers who already
know the systems, treat results as revealing rare edge cases and validating
trust-boundary assumptions — not as a statistically representative measure
of your exposure to a real external attacker.

The **Blue Team** is whoever defends and responds — the people a Red Team
exercise is actually testing, whether or not they carry that label
day to day.

A **Purple Team** function closes the loop between the two: it tracks that
findings a Red Team surfaced actually get fixed by the Blue Team, rather
than each exercise rediscovering the same gaps. Without it, red-teaming
degenerates into a demonstration with no lasting effect — think of it as
regression testing for vulnerabilities, verifying a hole stays closed
rather than just that it was once found. Sharing the attack plan with the
Blue Team up front is one way to formalize this: it trades surprise for
faster, more comprehensive feedback on detection coverage, and can extend
to distributing Red Team-style thinking out to the product engineers who
know a system's actual weak points.

**Complementary, lower-cost formats** for organizations not ready for full
unannounced Red Team exercises:

- **Tabletop exercises** — a facilitator walks a mixed group (engineers,
  leadership, communications, legal) through a believable incident
  scenario with branching decision points, asking what they'd actually do.
  Nonintrusive (nothing goes offline) and useful even for scenarios too
  costly or dangerous to run for real.
- **Targeted fault injection**, such as deliberately testing whether a
  breakglass credential mechanism still works when standard access
  services are down, with the detection team watching in parallel to
  confirm the resulting alert fires correctly — validating the security
  control and the response pipeline in the same exercise.

Every finding — from a full Red Team engagement or a tabletop — is only as
valuable as what happens next: write it up with the same rigor as a
[security postmortem](security-postmortem.md), assign an owner, and track
it to closure. [Vulnerability Reward Programs](vulnerability-reward-programs.md)
extend the same assurance goal to continuous, unscoped external scrutiny
rather than a periodic internal exercise.
