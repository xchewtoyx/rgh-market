---
type: concept
title: Just-in-Time Documentation Triggers
description: Writing operational documentation only when a real knowledge gap is demonstrated, using disposable notes and a backlog rather than trying to document everything upfront.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 10"
---

Continuous informal knowledge sharing (hallway conversations, ad hoc explanations) reduces the risk of knowledge being concentrated in one person who might leave — the "truck factor" risk a handover is meant to eliminate. But not every piece of shared knowledge needs to become a permanently maintained document. A disposable sketch or an on-demand explanation is sometimes better than a maintained artifact, because it doesn't create an ongoing maintenance burden for knowledge that turns out not to be reused.

## Triggers for Writing Something Down

Rather than trying to anticipate everything a future maintainer might need, write documentation reactively, triggered by evidence that a specific gap is real:

- **Astonishment reports**: When someone is surprised by how the system actually behaves — an assumption they held turned out to be wrong — that surprise is a signal that a piece of tacit knowledge just became visible. Capture it while it's fresh; a documented surprise is exactly the kind of gotcha a future unfamiliar operator would otherwise rediscover the hard way.
- **Knowledge backlog**: Maintain a running list of documentation gaps that have actually been hit in practice (a question someone had to ask, a piece of context someone was missing), and write them up when the backlog reveals the same gap recurring — rather than speculatively documenting everything that might conceivably be asked.

## Why This Beats Upfront Comprehensive Documentation

Documentation written speculatively, before any real gap has been demonstrated, tends to document what the author assumes will matter rather than what actually does — and it still needs maintaining even if no one ever needed it. Documentation triggered by an actual astonishment or a recurring backlog item is targeted at proven need, which both makes better use of documentation effort and keeps the resulting notes closer to what a real future reader will actually search for.
