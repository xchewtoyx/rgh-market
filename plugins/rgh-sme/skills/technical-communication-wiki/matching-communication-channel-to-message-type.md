---
type: concept
title: Matching Communication Channel to Message Type
description: >
  Which channel a message goes out on should follow from how long it
  needs to persist and how much emotional nuance it carries, not from
  whichever channel happens to be open — real-time chat, persistent
  email, and a lasting document each fit a different kind of message.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 7"
---

A team that coordinates primarily through chat tends to default every message to chat, regardless of whether the message actually belongs there — but chat, persistent messaging, and a standing document each suit a genuinely different communication need, and picking the wrong one loses information or wastes a reader's attention. A workable default: **chat** for real-time, ephemeral discussion that nobody needs to find again later; **a persistent channel like email** for anything that needs to survive a shift change or a day boundary, including a decision that was actually reached in chat and now needs to be broadcast somewhere durable; **a wiki or shared document** for anything with lasting effect — a policy, a design decision, a process everyone will need to reference going forward — with its creation itself announced through the persistent channel so people know to go look. The underlying test for picking a channel is not "where is the conversation happening right now" but "how long does this message need to remain findable, and by whom."

A second axis, independent of durability, is how much emotional or interpersonal nuance the message carries. Plain text strips out tone, so a message that's neutral in the writer's head can read as curt, sarcastic, or hostile to a reader who has no vocal inflection or facial expression to calibrate against — a bigger risk in a distributed or remote team, which lacks the incidental in-person cues that catch a misunderstanding early. The fix is to deliberately escalate to a higher-bandwidth channel — voice, video, or an in-person conversation — specifically once conveying emotion starts to matter, and especially once a text exchange is visibly turning heated: continuing to argue a sensitive point over chat because that's where it started usually makes the misunderstanding worse, not better. This is the same instinct behind [phrasing disagreement to stay collaborative](phrasing-disagreement-to-stay-collaborative.md) — extended from the words themselves to the channel those words travel over — and it argues for having an explicit, agreed convention for which channel a given message type uses, rather than leaving the choice to habit or whatever tool happens to be open.
