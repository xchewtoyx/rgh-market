---
type: concept
title: Proactive Requirements Analysis
description: >
  Gathering data-warehouse requirements concurrently with, rather than
  after, the operational system that will feed it lets BI stakeholders
  shape the source schema while it is still cheap to change, at the cost
  of having neither real data nor existing reports to analyze against.
sources:
  - title: Agile Data Warehouse Design
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 1, pp. 13-16"
---

Data warehouses historically lagged behind the operational (OLTP) systems
they reported on — built only once an operational system had already
proven inadequate for reporting and a backlog of unmet BI needs had built
up. **Proactive** analysis inverts this: the warehouse is designed and
built concurrently with a new operational system, rather than after it.
This has become more common as the line between operational and analytical
reporting has blurred (near-real-time BI feeding operational decisions) and
as organizations with prior warehouse success come to expect every new
operational system to arrive with its BI integration already planned,
rather than tolerating an interim gap.

**Why it pays off**: preempting detailed operational data modeling lets BI
stakeholders set the data agenda while the source system is still cheap to
change. This matters most for *mandatory data* — attributes that look
optional or insignificant from a purely operational point of view can be
specified `not null` and captured from day one, before operational users
develop workarounds that later resist correction. It also benefits ETL: an
agile ETL team can define its ideal extraction interface against the
proactive data-warehouse model and hand it to the still-in-development
OLTP team as a spec — a natural opportunity to build in proper
change-data-capture support (consistently maintained timestamps, update
reason codes) so ETL can later tell *when* data changed and *why* (a
genuine business change requiring history, versus a correction requiring
none). See [mandated constraint](mandated-constraint.md) for the general
category "specify this while it's still cheap to change" belongs to, and
[requirement vs. design decision](requirement-vs-design-decision.md) for
why capturing the *what* (mandatory, auditable data) doesn't require the
OLTP team's implementation to be finalized first.

**The "data then requirements" conundrum**: proactive analysis has to run
before real data or real reports exist, which strips out the two
icebreakers both traditional strategies rely on — see [data-driven vs.
reporting-driven requirements
analysis](data-driven-vs-reporting-driven-requirements-analysis.md).
Reporting-driven analysis loses its usual opening questions ("how could
your favorite reports be improved?", "how do you use this data to
decide?") because there are no existing reports to reference, and even
open-ended prompts land poorly when stakeholders have no experience of the
new process yet to reason from. Data-driven analysis loses its source to
profile: there is no populated schema to remodel when the source database
doesn't exist yet, is still under development, or holds only test data —
and even a fully documented package-application schema can be too complex
to profile usefully when little of it is populated or understood yet.
Neither IT nor business stakeholders can state genuine BI requirements in
full detail before there is data and people have lived with it, even
imperfectly — yet without early, detailed requirements a proactive design
routinely fails to deliver the right information on time, and a BI backlog
starts building the moment data does become available. This chicken-and-
egg problem is what motivates treating [requirements discovery as
iterative rather than a single up-front collection
exercise](requirements-discovery-vs-gathering.md): a proactive
requirements approach has to be paired with a design and analysis
technique that can keep discovering requirements as real data starts to
flow, not one that assumes discovery finishes before build begins.
