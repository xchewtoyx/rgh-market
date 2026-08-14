---
type: concept
title: Find the Responsibilities Hidden Inside API-Saturated Code
description: >
  When an application reads as nothing but repeated calls to someone else's
  library, describe what the code actually does in plain English,
  independent of the API — that description surfaces the underlying,
  API-agnostic responsibilities worth extracting.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 15"
---

An application built mostly from vendor libraries, open source, or
platform-bundled code (J2EE, .NET) can end up reading as "nothing but
repeated calls to someone else's library." The seductive reasoning that
API-glue code is "too simple to need tests" is a trap — "many legacy
projects have started from those humble beginnings," and complexity creeps
in until you're maintaining code you didn't write with no real confidence in
your changes. API-saturated systems are harder than typical home-grown
legacy code for two specific reasons: the API calls crowd out any visible
hint of what the application's *own* design should look like, and you don't
own the API, so you can't rename, reshape, or add convenience methods to it
the way you could with your own classes.

**The technique**: write a one- or two-sentence plain-English description of
what the code actually does, independent of the specific API calls used to
do it. Worked example, a mail-forwarding server: this yields four
responsibilities — receive incoming messages, send a mail message, build a
new outgoing message per recipient from an incoming one, and periodically
wake up to check for new mail. Classify each by how API-bound it actually
is: some responsibilities are unavoidably tied to the API; some are merely
API-*adjacent* and independently testable using dummy objects standing in
for API types; some have nothing to do with the API at all (a sleep/wake
timing concern, say) and can be pulled out cleanly.

Even the cleanest resulting class often still touches the underlying API
directly somewhere — full independence isn't always achievable — but partial
layering still turns previously "buried and unapproachable" logic into
something directly testable. "It's nearly impossible to break up a system
into smaller pieces without ending up with some that are 'higher level' than
others."

A meta-technique for kickstarting this analysis on any API-soaked system:
mentally treat the whole mess as one oversized class and apply the same
responsibility-separation heuristics you'd use for
[a class that's grown too big](class-size-as-a-hiding-decision.md) — even
without immediately achieving the ideal design, simply naming the
responsibilities clarifies what to extract next. Once responsibilities are
named, [skin and wrap the API](skin-and-wrap-the-api.md) and
[responsibility-based extraction](responsibility-based-extraction.md) are
the two concrete techniques for actually separating them from the API calls.
