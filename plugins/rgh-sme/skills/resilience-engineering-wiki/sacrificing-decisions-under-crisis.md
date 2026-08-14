---
type: concept
title: Sacrificing Decisions Under Crisis
description: >
  Under extreme time and information pressure, decision-making shifts from
  Simon's ordinary satisficing to deliberately abandoning the highest-payoff
  option in order to cap the worst-case downside — not the same thing as a
  proactive sacrifice judgement made before a crisis exists.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

Simon's satisficing describes ordinary bounded-rational decision-making:
under normal constraints on time and information, people choose the first
option that is good enough rather than exhaustively searching for the
optimum. A genuine crisis compresses time, information, and control far
enough that satisficing itself changes shape into something Pariès names a
**sacrificing decision**: deliberately abandoning a high-potential,
high-payoff option specifically because its downside is intolerable, in
favour of a lower-tier option whose worst case is capped and survivable.

US Airways Flight 1549 is the clean case. Post-accident simulation showed
the aircraft technically had enough energy to glide back to LaGuardia — the
higher-payoff option, an undamaged aircraft landing normally. Determining
that in real time, under the actual conditions the crew faced, was not
possible; more importantly, a failed attempt carried an intolerable
downside — a crash short of the runway over a dense urban area. Ditching in
the Hudson gave up the high-payoff outcome deliberately, in exchange for
capping the worst case at something survivable. The same logic recurred
inside the same event at a smaller scale: the standard procedure called for
attempting to relight the one engine still delivering idle thrust, but doing
so required shutting it down first, which risked total power loss and a
drop from the flight-control system's protected "normal law" to unprotected
"direct law" — trading a chance at thrust recovery against degrading the
controllability the crew would need for the *ditching itself* if the
relight failed. Both are the same shape of decision: give up the better
expected outcome to keep the worst outcome bounded.

**This is not the same concept as a [sacrifice
judgement](sacrifice-judgements.md), despite the shared word.** A sacrifice
judgement is a *proactive* choice, made with time to spare, to relax
production goals before any crisis exists, in order to stay clear of a
safety boundary — converting to open surgery, breaking off an approach. A
sacrificing decision is *reactive*, made inside an already-unfolding crisis
with no time left, choosing between bad options none of which is safe,
purely to bound how bad the outcome can get. The two sit at opposite ends of
[the boundary of potential variability](boundary-of-potential-variability.md):
a sacrifice judgement is how a well-functioning system avoids crossing the
boundary at all; a sacrificing decision is what happens once the crossing
has already occurred and only the recovery is left to manage — the decision
logic operating inside [preserving margin for future
response](preserving-margin-for-future-response.md) once margin is nearly
gone rather than while it is still being protected.
