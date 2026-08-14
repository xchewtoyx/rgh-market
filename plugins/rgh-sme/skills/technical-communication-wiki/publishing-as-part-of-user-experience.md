---
type: concept
title: Publishing Is Part of the User Experience
description: >
  Where and how a document is published — the channel, the launch
  timing, the findability of the page — determines whether well-written
  content ever actually reaches its reader.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 7"
---

Publishing is not a mechanical step that happens after the real work of writing is done — it's part of the reader's experience, and getting it wrong can waste well-researched, well-edited content entirely. Choosing a channel means weighing where the target audience already looks, the content type (see [choosing documentation types](choosing-documentation-types.md)), discoverability, who owns the channel, its review workflow, its release cadence, its accessibility, and the team's actual ability to maintain content there long-term. A README meets contributors where they already are, right next to the code; a dedicated documentation site better supports product users who need navigation, search, and versioned reference material a README can't provide.

Publication should be planned alongside the product launch it documents, not bolted on afterward: establish the audience, the goal, the minimum content needed at launch, page owners, dependencies, the review and approval path, the publishing date, and how the release will be communicated — all before the launch date arrives. A clear, honest, deliberately scoped first release that ships when users need it beats "perfect" documentation that arrives after they've already had to work around its absence.

Treat documentation delivery like software delivery: keep source in version control, use pull requests and automated validation, preview changes before release, and assign explicit responsibility for keeping content current as the product changes (see [maintaining and deprecating documentation](maintaining-and-deprecating-documentation.md)). Before release, confirm links, rendering, code samples, images, navigation, metadata, and accessibility all actually work — not just that the prose reads well. Findability itself is a publishing responsibility: meaningful titles, headings, URLs, internal links, and search-oriented language (the terms a reader would actually type, not just the terms the writer would use) all determine whether a page can be found at all.

Publication is the start of a feedback and measurement loop, not its end — see [closing the feedback loop](closing-the-feedback-loop.md) and [measuring documentation quality](measuring-documentation-quality.md). Announce material documentation through the channels users actually follow (release notes, product messaging, community channels, support, direct outreach where appropriate), and don't assume a page that has been deployed has therefore reached or helped anyone.
