---
type: concept
title: Configuration Parameters as Incomplete Solutions
description: >
  A configuration parameter pushes a design decision up to users or
  administrators instead of resolving it internally, and represents an
  incomplete solution to the underlying problem — one to minimize, not
  reach for by default.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 8"
---

Configuration parameters are the inverse of
[pulling complexity down](pull-complexity-downwards.md): instead of the
module absorbing a decision (cache size, retry count), the decision gets
pushed upward for someone else to set. Some systems now export hundreds of
these. A parameter is also the archetypal [deferred-binding](binding-time.md)
mechanism — moving the moment a value gets fixed later in the life cycle,
from a developer's source edit to whoever sets the parameter, later and
possibly repeatedly.

There's a legitimate case: when the module genuinely cannot know the best
policy but the user's domain knowledge can supply it — a user knowing that
some requests are more time-critical than others and assigning them higher
priority, for instance. But parameters are often used as an easy excuse to
avoid dealing with an important issue, even when users or administrators are
poorly positioned to pick a good value, or when the system could derive a
good value automatically. Worked example: rather than a configurable
retry-interval parameter for a lossy network protocol, the protocol can
measure actual response times for successful requests and derive a retry
interval as a multiple of the observed value. This pulls the complexity down,
saves users from guessing, and adapts automatically to changing conditions —
a static configuration value, by contrast, drifts out of date as conditions
change.

Guidance: avoid configuration parameters as much as possible. Before adding
one, ask "will users, or the higher-level modules calling this one, actually
be able to determine a better value than I can determine here?" When a
parameter is genuinely unavoidable, compute a sensible default automatically
so most users never need to touch it — this is
[making the common case simple](interfaces-should-make-the-common-case-simple.md)
applied to configuration specifically. Every configuration parameter is, by
this framing, an admission that the module's solution is incomplete; the
ideal is for each module to solve its problem completely, internally.
