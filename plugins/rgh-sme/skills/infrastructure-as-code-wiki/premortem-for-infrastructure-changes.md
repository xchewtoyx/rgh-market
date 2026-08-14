---
type: concept
title: Premortem for Infrastructure Changes
description: A planning technique that counters overconfidence in a change plan by assuming it has already failed and asking participants to explain why, rather than asking them to critique it as written.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 5"
---

Once a team has built a plan for a risky infrastructure change — a major migration, a stateful cutover, a first production rollout of a new pattern — asking them to review their own plan for flaws typically gets only half-hearted scrutiny: having just built the plan, they're emotionally invested in it working, and mental simulation of a plan someone believes in tends to explain away rather than surface problems (the same bias behind [failure scenario mapping](failure-scenario-mapping.md)'s point that teams often don't know a failure mode's actual consequence until they deliberately investigate it).

A premortem reframes the exercise: imagine the change has already happened, months from now, and it failed. Participants must explain why — identifying the specific causes that would justify "of course it didn't work, because...". This turns plan review from a defensive task (find fault with something you're invested in) into a creative one (find smart, plausible failure modes), which reliably surfaces trouble spots a straight review misses. The exercise itself takes well under ten minutes to run; the discussion it triggers can run much longer, and is where the actual value shows up.

A premortem is a narrower, plan-specific instrument than [failure scenario mapping](failure-scenario-mapping.md)'s standing workshop — run it once, right before executing a specific high-stakes change, precisely because that is the moment overconfidence in "the plan we just spent weeks building" is highest. It pairs naturally with [reversible infrastructure decisions](reversible-infrastructure-decisions.md): a premortem that turns up a plausible failure mode with no cheap way back is itself evidence the change should be restructured into smaller, individually reversible steps before it ships.
