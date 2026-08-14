---
type: concept
title: Product Leader Incident Boundaries
description: A business or product leader's legitimate role during an ML incident is to be informed and to supply business-impact context, not to lead — their instinct to take charge is the main risk to manage.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

Business and product leaders often assume incident response isn't their
concern, but once ML matters to the organization beyond the narrowest uses,
their awareness becomes important — they can report real-world impact and
suggest likely causes or the least-costly mitigation from a business
standpoint. That said, this role rarely sits in a formal on-call rotation;
the default alternative, "everyone is mostly on call all the time," is
worth replacing with an actual rotation if only to let leaders take real
vacations.

During an active incident, a product or business leader's main risk is the
urge to lead when they aren't the most knowledgeable person present. Their
legitimate rights are narrower than that: to be informed, and to provide
context on business impact. They generally shouldn't participate directly
in the technical handling — proxying questions through someone else and
staying off the direct incident channels (chat, phone, the [incident
state document](incident-state-document.md)'s live thread) helps avoid
inadvertently taking over the [incident commander's](incident-command-system.md)
role, which is the same failure mode [SME conduct during
incidents](sme-conduct-during-incidents.md) warns technical experts against
for a different reason (undermining [command
presence](command-presence.md) rather than business overreach).

Post-incident, this role should own prioritizing follow-up work and setting
completion standards, without needing an opinion on implementation
specifics — a simple priority-tier system (Highest, High, ... Nice to Have)
with a review trigger if Highest-priority items stall is enough. Product
teams, led by product management, are also the natural owners of specifying
and evolving the SLOs that determine what actually satisfies customer needs
going forward.
