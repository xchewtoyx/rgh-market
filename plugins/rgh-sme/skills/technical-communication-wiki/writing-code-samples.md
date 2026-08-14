---
type: concept
title: Writing Code Samples as Executable Explanations
description: >
  A code sample is documentation that a reader will copy and run, which
  makes it a promise about the product — it needs its own correctness,
  testing, and maintenance discipline beyond ordinary prose.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 5"
---

A code sample is an executable explanation: it shows how an interface is used and hands the reader a working starting point they can transplant directly into their own context. A small example built to support exactly one learning goal beats an extract of real production code, which usually carries irrelevant complexity the reader has to mentally filter out before they can use it. State explicitly, in the surrounding prose, what the example accomplishes, where it fits in the larger procedure, and what success actually looks like when it runs.

Because a reader will run this code, not just read it, it carries obligations ordinary prose doesn't: it has to be correct, complete enough to actually execute, and kept continuously tested — source for it belongs in version control near the product or in a dedicated runnable project, ideally checked automatically in CI rather than trusted to stay correct by inspection. State dependencies, supported language or runtime versions, required setup, and any deliberate omissions explicitly, and never include secrets, private data, inaccessible dependencies, or unexplained "magic" values a reader can't account for.

**Write for copying.** A reader has to know exactly which values are placeholders to replace, with what, and when — distinguish literal commands the reader should type verbatim from variables they need to substitute. Use realistic, safe example values instead of abstract stand-ins like `foo` wherever the domain context actually helps comprehension. Keep the surrounding prose short and annotate only the specific lines that genuinely need explanation, rather than narrating every line. Never turn a code block into a screenshot — it has to stay selectable and searchable, or its usefulness as something to copy is gone (see [using visuals effectively](using-visuals-effectively.md) for the broader version of this rule).

Use progressive complexity: start from the smallest possible success, then layer in error handling, configuration, alternatives, and production concerns afterward rather than presenting all of it in one example a beginner can't parse. Because examples are effectively a promise to the reader, code and prose drifting apart from the real API is a direct defect — samples need to be updated or explicitly deprecated in step with the product, not left to quietly rot. The highest-value review for a sample is having a developer genuinely unfamiliar with it try to run it — their failures are exactly the documentation defects a familiar reviewer would never hit.
