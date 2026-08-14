---
type: concept
title: Circuit Breaker for Automated Retries
description: >
  Automation that retries a failing dependency needs a circuit breaker to
  stop retrying once failures pass a threshold, so a struggling downstream
  service gets relief instead of a retry storm that keeps it down.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 4"
---

# Circuit Breaker for Automated Retries

Retry is the default response automation reaches for when a call fails —
and it's usually right, since most failures are transient. But retry has
a blind spot: it assumes the target is momentarily unlucky, not actually
struggling. When a downstream service is genuinely overloaded or down,
every caller's automated retry logic firing at once is the opposite of
help — it's added load hitting a system that's already failing, which can
turn a brief blip into an extended outage purely because of how the
callers responded to it.

A **circuit breaker** sits in front of the retry logic and tracks recent
call outcomes to that specific dependency. Once failures (or timeouts)
cross a threshold, the breaker "trips": for a cooldown period, it fails
calls immediately without even attempting them, giving the struggling
dependency room to recover instead of more load to process. After the
cooldown it allows a small number of trial calls through; if those
succeed, it resets to normal; if not, it stays open and waits again. The
breaker's state is a piece of shared knowledge about "is this dependency
currently healthy" — centralizing it means every caller backs off
together, rather than each one independently deciding to keep hammering a
service that's already down.

This is a specific instance of [safeguards against runaway
automation](safeguards-against-runaway-automation.md): the danger being
bounded isn't automation acting too broadly on its own targets, it's
automation's own retry behavior becoming the runaway force against a
dependency it doesn't own. It's also why blind retry is not automatically
compatible with [idempotency](idempotency-in-automation.md) at scale —
making an action safe to repeat doesn't make repeating it at an
unconstrained rate harmless to whatever's on the receiving end.

The threshold and cooldown period are themselves a tuning tradeoff worth
naming explicitly: too sensitive (trips on ordinary blips) adds needless
latency and false alarms; too tolerant (trips only after sustained
failure) lets a genuine retry storm run for longer before the breaker
finally intervenes. As with any threshold-based safeguard, the right
values come from watching real failure patterns, not guessing once and
leaving it alone — see [confidence decay in unpracticed
safeguards](confidence-decay-in-unpracticed-safeguards.md) for why a
tripped-but-untested breaker is itself a risk.
