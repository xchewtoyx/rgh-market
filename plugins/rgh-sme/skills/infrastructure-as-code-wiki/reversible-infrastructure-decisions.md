---
type: concept
title: Reversible Infrastructure Decisions
description: Deliberately favoring infrastructure and tooling choices that can be undone cheaply over ones that lock the organization in, so more decisions can be made and iterated on quickly.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3, ch. 4"
---

Not all infrastructure decisions carry the same cost if they turn out wrong. Amazon's "one-way door / two-way door" framing draws the line explicitly: a one-way door is a decision that's nearly impossible to reverse once made (retiring a platform an entire org depends on); a two-way door is one you can walk back through cheaply if it doesn't work out (adopting a new managed database for a single new service). Because a two-way door carries low downside, an organization can afford to make more of that kind of decision, and make it faster, rather than stalling on analysis paralysis — a large infrastructure change is safer and faster overall when broken into a sequence of small, individually reversible steps than committed to as one big irreversible leap.

This reframes the point of good infrastructure architecture: not to pick the single best tool up front, but to design so that today's choice stays a two-way door for as long as possible — favoring loosely coupled components behind stable interfaces, [evaluating third-party modules](evaluating-third-party-infrastructure-modules.md) for how hard they'd be to leave as much as for what they offer today, and treating [multicloud and platform choices](multicloud-strategies.md) as provisional rather than permanent. A choice that looked reversible at adoption time can still calcify into a one-way door in practice — once a system is core to production, migrating away from it costs real team time, retraining, and rebuilt tooling even when nothing contractually locks you in — so it's worth periodically asking, before a technology becomes load-bearing, how it would actually be undone and how expensive that would be, rather than discovering the answer only when a real need to leave arises. A [premortem](premortem-for-infrastructure-changes.md) run before a specific change ships is one way to surface a would-be one-way door before it's actually walked through.
