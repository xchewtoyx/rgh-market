---
type: concept
title: Put Explanations Where Future Readers Will Actually Look
description: >
  An explanation recorded only in a change log, chat thread, or meeting
  note is effectively lost the moment the person who needs it doesn't
  know to go searching there — durable rationale belongs in the artifact
  itself.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 16"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Martin Fowler), ch. 10, Introduce Assertion"
---

It's tempting to record the reasoning behind a change only where the change itself is being discussed — a commit message, a pull-request comment, a chat thread, a meeting note — on the assumption that the record exists and can be found later if anyone needs it. That assumption fails in practice for a simple reason: a future reader working from the artifact itself has no cue that a relevant explanation lives somewhere else, and even someone who suspects one exists still has to search a change history or a chat archive to find it, which is a real cost most readers won't pay before they act. An explanation that isn't visible from where the work actually happens is, functionally, not available to the person who needs it — a hard-won fix can be silently undone by someone who never saw why it was needed in the first place, because nothing in the artifact itself flagged that the current form was deliberate.

The self-check is simple: before writing an explanation somewhere transient, ask whether someone will plausibly need this information again later while looking at the artifact, not at its history. If yes, the explanation belongs in the artifact — attached to the thing it explains — not only in the record of the change that produced it. A transient location can still carry a copy for convenience or narrative color, but it should never be the only copy of anything a future reader would actually need. This is the same underlying discipline as [maintaining and deprecating documentation](maintaining-and-deprecating-documentation.md): documentation that exists but isn't where a reader will encounter it fails just as completely as documentation that was never written.

The same placement discipline applies to stating an assumption, not just a rationale: an unstated assumption a reader needs ("this only works for positive input," "this field is always populated by the time this code runs") should be written down explicitly at the point where the assumption is *established* or *enforced*, not only at each of the possibly many points that later rely on it. A reader troubleshooting a violated assumption starts at the point of failure and needs to trace backward to its origin; recording the assumption there, once, gives them exactly the anchor that scattering the same note across every dependent site would not.
