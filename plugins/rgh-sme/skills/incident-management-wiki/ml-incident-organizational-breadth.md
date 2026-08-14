---
type: concept
title: ML Incident Organizational Breadth
description: ML incident resolution routinely pulls in finance, vendor management, PR, legal, and business leadership rather than staying an engineering-only activity, because ML systems span more of the organization than non-ML services.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

ML systems have a strong connection to real-world situations and user
behavior, so troubleshooting an ML incident can involve far more of the
organization than a standard production incident does — finance, supplier
and vendor management, PR, and legal are all plausible participants, not
just engineering. This isn't a claim that ML outages are necessarily more
costly or important than non-ML ones — only that understanding and fixing
them usually has broader organizational scope, because ML systems are built
on and feed into more technical, product, and business systems at once.

The practical implication is a wider stakeholder set than the [incident
command system](incident-command-system.md)'s standard roles anticipate:
resolving the incident may need someone who understands a data vendor's
contract, or legal input before a model output can be publicly discussed,
or product/business input to judge whether an effect is even a regression
(see [ML outage boundary ambiguity](ml-outage-boundary-ambiguity.md)).
Recognizing this in advance — rather than discovering it mid-incident —
matters for who gets added to the [escalation](escalation-as-resource-request.md)
path and how quickly.

This breadth also shows up in *choosing* a mitigation, not just in
diagnosing the problem: in a documented case, whether to roll back to an
older model was ultimately a business call, not an engineering one, once
engineering had shown the old model was itself no longer clearly correct
(see [ML rollback limits in a changing
world](ml-rollback-limits-in-a-changing-world.md)) — the deciding factor
was how much revenue risk the business was willing to accept, which no
amount of additional engineering analysis could resolve on its own. This
kind of engineering-can't-decide-alone escalation is described as far more
common for ML incidents than for non-ML ones, which is an argument for
having both technical leaders who understand the business and business
leaders who understand the technology, rather than routing every
mitigation decision through a purely technical incident commander.

See also [ML outage visibility gap](ml-outage-visibility-gap.md).
