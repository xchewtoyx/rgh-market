---
type: concept
title: The Curse of Knowledge and Audience Research
description: >
  Writers who know a system overestimate how much of it readers can
  infer, which is why documentation needs deliberate audience research
  rather than an author's own sense of what's obvious.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 1"
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 2"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

The curse of knowledge is the gap between what someone who knows a system assumes is obvious and what someone encountering it fresh can actually infer. A classic demonstration: people asked to tap out a well-known tune expected listeners to recognize it about half the time; listeners actually recognized it about one time in forty. A writer close to a system is in the tapper's position by default — the fix is empathy and research done before drafting, not a stronger effort to "explain clearly" from the writer's own vantage point.

Before writing, identify the audience(s) the document must satisfy and choose a **primary audience** to write to first — a design document persuades decision makers; a tutorial instructs someone utterly unfamiliar with the codebase; API reference must be complete for experts and novices who depend on the surface. You cannot optimize every axis at once; see [seekers versus stumblers](seekers-versus-stumblers.md) for how encounter mode differs from role, and [customer versus provider documentation](customer-versus-provider-documentation.md) for splitting end-user and maintainer material.

Good documentation does not require polished literary skill — treat writing like testing or any other required engineering process. The audience is standing where you once stood, minus your current domain knowledge; you do not need to be a great writer, just get someone like past-you as familiar with the domain as you are now, and improve the draft over time once something is on the page. Limited English fluency is less often the barrier than failure to step outside your own assumptions.

Useful audience axes to name explicitly: **experience level** (expert versus junior), **domain knowledge** (team insider versus API-only consumer), and **purpose** (quick task completion versus deep maintenance). Writing only for experts lets you cut corners but loses novices; explaining everything for novices annoys experts. There is no universal fix, but shorter documents often serve both better — which usually means drafting long, then editing down, because the cost of cutting is paid once and the savings are amortized across every reader.

Two goals need to be stated and checked against each other before writing starts: the organization's desired outcome for the reader (get them onboarded, get them using an API) and the reader's own actual goal (which may be a business problem the product is only one part of solving). A useful document set has to serve both, and conflating them — writing only to the organization's goal — produces documentation that's technically accurate but doesn't answer what the reader is actually there for. This is also where a writer should resist trying to serve everyone at once: prioritize one target audience, described concretely by role, experience level, working environment, and team context, since an application developer and an SRE reading the same product need genuinely different help. See [strong opening technique](strong-opening-technique.md) and [motivating the reader with a problem](motivating-the-reader-with-a-problem.md) for the parallel point that a document has to know what problem its specific reader is trying to solve.

The same asymmetry shows up whenever a writer judges their own clarity directly: if someone close to the material finds it simple but readers consistently report finding it confusing, the material is confusing — full stop, not "confusing to them but not really." The discrepancy is data about the audience gap, not a verdict on the readers, and it's worth investigating on its own terms rather than dismissing as the readers just not trying hard enough. A writer's job is to produce something the intended reader can use easily, not something the writer personally finds easy to follow, and those two things quietly diverge exactly where the curse of knowledge is strongest.

Concrete research methods, in rough order of cost: mine existing channels first — support tickets, developer-relations conversations, UX research, sales and marketing material, code, chat logs, and commit history — grouped by topic, process, and user type to find recurring patterns before running new research. Direct interviews favor quality over quantity: three to five well-matched participants can meaningfully guide a round of research, using specific open questions and, where possible, observing a participant actually attempt the real task rather than asking them to describe it from memory. Surveys should stay brief — one neutral, optional, closed question at a time, with a clear statement of how the data will be used — and consent, privacy, and applicable data-handling law govern all of the above.
