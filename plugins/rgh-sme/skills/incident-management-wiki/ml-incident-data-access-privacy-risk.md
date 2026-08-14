---
type: concept
title: Privacy Risk in Ad Hoc Incident Data Access
description: Pulling raw customer query or log data for incident troubleshooting can expose PII and correlated-query re-identification risk that a responder focused on diagnosis is unlikely to weigh on their own.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

In a documented case, a responder diagnosing a recommendation-quality
incident pulled a repeatable test set of roughly 100,000 real customer
queries and page views to replay against the model — a reasonable
diagnostic move under time pressure, and one an on-call engineer could
make unilaterally with existing access. The authors flag this as a privacy
risk that should not have been made unilaterally: raw queries can contain
protected information directly (an IP address is PII in many
jurisdictions), and *correlated* queries — the same user's queries
considered together — can reveal materially more private information than
any single query does in isolation, the failure mode behind the AOL search
log release incident. The responder should have consulted
privacy/data-protection professionals before extracting the data, or,
better, never have had unmonitored direct access to raw customer queries
available to reach for in the first place.

The general incident-readiness implication is that "whatever gets the
diagnosis done fastest" is not a safe default when the fastest path
touches raw user data — the pressure of an active incident is exactly the
condition under which a responder is least likely to pause and weigh a
privacy tradeoff on their own. Preparation has to close this gap in
advance, by making the privacy-safe path also the easy path (tooling that
doesn't expose raw queries un-aggregated) and by making a
privacy/data-protection contact a normal part of the incident escalation
list rather than an afterthought reached for only if someone happens to
think of it.

Three concrete governance mechanisms address this directly: restrict
sensitive data access by default rather than granting it broadly ahead of
time; require a logged justification for any access granted during an
incident, so what was accessed and why is reviewable afterward; and
require multiple people jointly overseeing sensitive data access as a
mutual check, rather than trusting any one responder's judgment alone
under pressure. [Model developers](ml-model-developer-incident-role.md)
should treat pushback on a request that would violate one of these
constraints as a legitimate part of the role, not an obstruction of the
response. See also [ML fairness incident
recognition](ml-fairness-incident-recognition.md) and [ML incident
whistleblower considerations](ml-incident-whistleblower-considerations.md)
for the other two areas where an ML incident can raise stakes beyond the
immediate technical problem.
