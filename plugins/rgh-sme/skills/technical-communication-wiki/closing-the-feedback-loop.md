---
type: concept
title: Closing the Documentation Feedback Loop
description: >
  Feedback closes the gap between what a writer assumed and what
  readers actually experience, but only if it's easy to give, properly
  triaged, and checked afterward against whether it actually reduced
  the friction it targeted.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 8"
---

Feedback exists to close the gap between an author's assumptions (see [the curse of knowledge and audience research](curse-of-knowledge-and-audience-research.md)) and what readers actually experience after publication. Collecting it well means making it easy, timely, and safe to give: page-level feedback mechanisms, a clear contact route, issue templates, and invitations to give feedback at moments when it's actually relevant. Ask about the task and its outcome specifically — did this help you do the thing you came to do — rather than a generic "was this page helpful?"

Qualitative feedback comes from usability sessions, interviews, support conversations, community posts, and friction logs (see [documentation research artifacts](documentation-research-artifacts.md)): observe users attempting a realistic task and record exactly where they hesitate, search, misread, or give up. Ask focused follow-up questions and look for themes that recur across multiple people rather than over-reacting to one strongly worded request. Quantitative signals — search queries, failed searches, page-behavior data, support ticket volume — are useful for identifying *where* to investigate, but on their own they don't explain *why*; they need the qualitative side to interpret them.

Triage incoming feedback by user impact, frequency, severity, how confident the evidence is, and the effort a fix would take. Classify each item as a documentation fix, a product defect being reported through the wrong channel, a feature request, or a misunderstanding whose real cause is somewhere else entirely — a request for a documentation change is still evidence of a real user need even when the specific fix requested isn't the right one. Document the triage decisions and close the loop with the people who reported an issue where that's feasible.

Integrate accepted changes through the normal review and publishing process (see [publishing is part of the user experience](publishing-as-part-of-user-experience.md)), and then re-test whether the change actually reduced the friction it targeted rather than assuming it did because it shipped. Feedback work should be continuous, not a one-time cleanup pass, and it should be shared outward with engineering, product, support, and developer relations — recurring documentation confusion is often the most visible symptom of a genuinely poor product workflow, naming choice, error message, or onboarding design, not just a writing gap.
