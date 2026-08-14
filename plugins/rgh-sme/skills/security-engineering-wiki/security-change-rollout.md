---
type: concept
title: Security Change Rollout
description: >
  Rolling out posture improvements group by group with dry-run modes,
  self-service enrollment, fast noncompliance feedback, and long-tail
  tracking — scaling up to multi-year ecosystem changes driven by
  incentives.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 7"
---

# Security Change Rollout

Proactive posture improvements rarely need sudden rollout — phase them
deliberately, with success criteria gating each phase. Affected teams
often can't be expressed as "X% of traffic"; phase by *who* (team,
system, user group) and by *what* (progressively stricter requirements;
opt-in before mandatory; **dry-run/audit mode before enforcement** so
misidentified scope and hard cases surface while the change is still
harmless). Choosing the first group: easiest-first proves value when
you're still seeking buy-in; hardest-first finds the real bugs when
leadership is already committed. Either way the team making the change
should live under it themselves.

**Lessons from Google's FIDO security-key rollout** (replacing phishable
OTP 2FA company-wide, 2013–2015):

- Define security *and usability* requirements up front — 2FA had to be
  fast and brainless, especially for on-call SREs mid-outage — and
  validate candidates with real users.
- Make the solution work for **all** users (accessibility included) and
  easier than what it replaces; friction on frequent actions compounds.
- **Self-service everything** — enrollment, multiple backup keys,
  firmware updates — to keep central IT out of the critical path.
- Give users tangible proof the change serves them; keep a feedback
  channel.
- **Fast noncompliance feedback**: reminders (then blocks) within
  minutes/hours when someone uses the deprecated path.
- **Track the long tail from the choke point**: since all OTPs were
  centrally generated, request logs identified which application to
  convert next; a web-based OTP generator (gated on security-key
  verification) served the final exceptional cases.

**Long-term/ecosystem changes** (multi-year, often externally driven,
e.g. Chrome's HTTPS push): documentation sustains continuity across staff
turnover and leadership support; measure progress with automated,
self-serve compliance checks (aim for compliance-check coverage like test
coverage) feeding one transparent source of truth; and expect a long
tail — for non-mandatory changes, 80–90% adoption is success. The
HTTPS-specific lessons: understand the ecosystem with data before
committing to strategy; overcommunicate through every channel (regionally
tailored); **tie the security change to business incentives** (HTTPS-only
web features gave organizations bottom-line reasons to migrate); and
build industry consensus so the change reads as an inevitable trend.

Sequencing under pressure belongs to
[design for a changing landscape](design-for-changing-landscape.md);
urgent timelines to
[zero-day response](zero-day-vulnerability-response.md).
