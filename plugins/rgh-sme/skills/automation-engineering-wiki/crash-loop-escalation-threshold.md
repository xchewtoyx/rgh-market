---
type: concept
title: Crash-Loop Escalation Threshold
description: >
  An automated process watcher that blindly restarts a crashing process
  forever can waste resources or mask a real problem, so it needs its own
  rate limit that converts repeated restarts into a human escalation.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
---

# Crash-Loop Escalation Threshold

Auto-restarting a crashed process is a basic, valuable form of
[self-healing](self-healing-overload-response.md) — nobody should have to
watch thousands of processes by hand to notice one died. Left unbounded,
though, the same mechanism becomes its own failure mode: a process that
crashes immediately on every start (a bad config push, a corrupted data
file, a bug triggered by every input) gets restarted in an infinite crash
loop, burning CPU and I/O without ever making progress, indistinguishable
from healthy operation unless someone is watching restart counts
specifically.

The fix is a [governor](governor-pattern.md)-style rate limit on the
restart action itself: a process watcher tracks its own restart frequency
and, once it crosses a threshold (e.g. more than five restarts in a
minute), stops restarting automatically and escalates to a human instead
of continuing to loop. This is the same design principle as any other
[safeguard against runaway automation](safeguards-against-runaway-automation.md)
— bound how much a single automated action can repeat before something
external has to approve continuing — applied to the narrowest possible
scope: one process's own recovery loop. A slower, less frequent crash
pattern (say, once an hour) doesn't need the watcher to intervene at all;
it's better caught by ordinary monitoring and still worth investigating,
just not urgently enough to halt the restart behavior itself.
