---
type: concept
title: Place Documentation Where Maintainers Will Look
description: Documentation survives and gets updated only if it sits where the person changing the system will actually be looking, which is rarely the commit log and rarely a header file separated from the implementation.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (Ousterhout), ch. 16"
---

Two placement decisions determine whether a piece of documentation stays accurate or quietly rots, independent of how well it was written the day it was created:

- **Proximity to the code it describes.** The closer an explanation sits to the thing it explains, the more likely a maintainer editing that thing will notice the explanation and update it in the same pass. An explanation held at a distance — a note in a wiki, a comment in a header file separated from the implementation it documents — survives only as long as nobody forgets it exists while making the actual change. When a genuine audience conflict exists (e.g. a caller who "shouldn't need to see the implementation file"), solve it with tooling that surfaces the documentation to that audience, not by relocating the documentation away from the maintainer who has to keep it honest.
- **The artifact, not the commit log.** A commit message explaining why a subtle fix was necessary is nearly invisible to whoever touches that code next — nobody thinks to scan version-control history before making a change, so nothing in the code itself warns a future maintainer that a piece of logic exists for a specific, non-obvious reason. The concrete failure mode this causes: a later maintainer, seeing no reason not to, "simplifies" the logic and silently reintroduces a bug that was already fixed once. Anything a future maintainer might plausibly need again belongs in the code or artifact itself; a commit message can restate it for convenience, but the in-artifact copy is the one that actually protects anyone.

## Avoiding Duplication Without Losing Findability

When the same piece of context is relevant from multiple places, don't copy the explanation to each one — write it once at whichever site is the single most natural place a confused maintainer would look first (e.g. next to the declaration of the thing behaving unexpectedly), and have every other site carry only a short pointer back to it. This has a useful self-healing property that duplicated copies lack: if the anchor comment is ever moved or deleted, a pointer reference breaks visibly (nothing there, findable via history), whereas duplicated copies can drift apart silently with no signal that any of them has gone stale. This is the same underlying logic as [Central File for Cross-Module Design Notes](central-file-for-cross-module-design-notes.md) for the harder case where no single natural anchor point exists at all.

## Why This Matters for Handover

A handover package is only as good as the documentation's ability to survive the first few changes made after the handover — placement is what determines that, not just the quality of the writing at handover time. This is the practical, artifact-level complement to the higher-level discipline in [Documentation Maintenance Workflows](documentation-maintenance-workflows.md): that note covers the process (release-pipeline integration, audit triggers) that keeps documentation from decaying at the system level, while this is the individual-comment-level habit of putting each piece of knowledge exactly where the next person editing that spot will be looking.
