---
type: concept
title: Late-Arriving Data
description: >
  Data that reaches the pipeline well after the event it describes occurred,
  and why handling it is a policy decision engineers must set and enforce,
  not just a technical filter.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Late-arriving data is a completeness/timeliness problem, not purely a
technical one: a source can be fully correct and still deliver a record long
after the event it represents happened — for example, a mobile app that
buffers ad-view events locally and only uploads once network connectivity
returns, so an "ad watched" event can land in the pipeline hours or days after
the actual view.

Because this can't be eliminated at the source, the pipeline has to decide,
explicitly and consistently, how to treat records arriving after their
expected window: reprocess the affected period, accept a bounded amount of
lateness with a watermark, route very-late records to a separate handling
path, or something else. Whatever the choice, it needs to be a uniformly
enforced standard rather than an ad hoc, per-job judgment call — an
inconsistent policy quietly produces different answers depending on which job
happened to run when the late record showed up.

This is also where the load mechanics meet dimensional design: a late-arriving
fact or dimension row has to be reconciled against whatever surrogate keys and
history the target model already has (grain and SCD design are the
downstream `dimensional-modelling` bundle's concern; getting the row into the
model correctly despite its late arrival is the pipeline's). When a fact
arrives before its dimensional context does, see the
[inferred member pattern](inferred-member-pattern.md) for the concrete
load-time technique.
