---
type: concept
title: ML Incident Whistleblower Considerations
description: An on-call engineer investigating an ML incident may discover something worthy of disclosure beyond the incident itself, and needs a commonly understood framework for that situation established in advance rather than improvised alone.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

An on-call engineer's unmediated access to systems, configuration, and data
during ML incident response — access that's genuinely hard to remove while
still fixing problems promptly — creates a distinct possibility: the
investigation surfaces something that isn't just an incident to mitigate,
but a finding worthy of disclosure beyond the incident channel itself (an
[ML fairness incident](ml-fairness-incident-recognition.md) uncovered
mid-investigation, a deliberate design decision the responder wasn't aware
was deliberate, or evidence of an unethical use of the system). The authors
argue the ML field needs an explicit, industry-understood whistleblower
framework for this situation specifically, without claiming the authority
to define one unilaterally themselves.

The incident-readiness point this raises, independent of how any specific
framework ends up defined: an on-call engineer under the stress and time
pressure of an active incident is a bad position from which to improvise a
first-principles answer to "what do I do with this." Whatever the
organization's answer is — an ethics escalation contact, a formal
disclosure process, legal involvement — it needs to already exist and be
known to responders before an incident puts someone in the position of
needing it, the same preparation logic behind [ML pre-negotiated outage
thresholds](ml-pre-negotiated-outage-thresholds.md) applied to an ethical
rather than a technical decision.
