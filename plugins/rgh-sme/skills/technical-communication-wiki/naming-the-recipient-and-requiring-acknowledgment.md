---
type: concept
title: Naming the Recipient and Requiring Acknowledgment
description: >
  A spoken directive to a group is only reliably received if it names
  who it's for, states the objective and a timeframe, and asks for an
  explicit acknowledgment back — a request addressed to no one in
  particular is easy for everyone to assume someone else will handle.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Schnepp, Vidal, Hawley), ch. 3"
---

A request voiced to an open group — "can somebody look into this?" — diffuses responsibility exactly when it needs to be concentrated: each listener can reasonably assume someone else is already handling it, and if no one does, there's no single person whose job it was. A reliable directive has three parts instead: it **names a specific person or role** ("Database team, can you check the replication lag"), not a vague appeal to the room; it **states a clear objective and a timeframe** ("...and report back in five minutes"), not an open-ended ask; and it asks the receiver to **acknowledge and repeat back** what they heard, closing the loop so the speaker knows the request was actually received and understood as intended, rather than assuming it landed correctly.

This matters most exactly where a plain restatement wouldn't otherwise be worth the interruption: high-pressure, high-stakes, multi-person coordination where a missed or misunderstood instruction is expensive to discover later rather than immediately. In lower-stakes settings the repeat-back can feel like unnecessary ceremony, which is why it's worth reserving for moments where a silent assumption of receipt is itself the risk — a live incident bridge, a handoff between shifts, a request that several different people could plausibly think was meant for someone else.

This is a spoken-communication analog of [labeling systems for clarity](labeling-systems-for-clarity.md): a label only works if it unambiguously identifies its target, and a directive only works if it unambiguously identifies who's responsible for acting on it and confirms that the right person actually got the message.
