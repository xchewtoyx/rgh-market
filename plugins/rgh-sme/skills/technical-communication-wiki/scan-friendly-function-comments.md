---
type: concept
title: Scan-Friendly Function Comments
description: >
  Function-level reference comments should open with an indicative verb
  so a seeker scanning a file can judge relevance quickly, and a single
  clear prose sentence often beats artificially separated boilerplate
  sections.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Reference documentation at function granularity has a scanning job: a reader already knows roughly what they're looking for and needs to decide, line by line, whether this declaration is the one. **Start the comment with an indicative verb** — "Merges," "Deletes," "Creates" — naming what the function does and, where relevant, what it returns, so verbs line up visually down the file and a seeker can assess relevance without reading full paragraphs.

Boilerplate section labels ("Returns:", "Throws:", "Parameters:") are not inherently clearer than good prose. One sentence that naturally covers postconditions, parameters, return value, and exceptional cases is often easier to read than the same facts chopped into mandatory headings — especially when most functions don't need every section filled. The same scanability discipline applies one level up: **file comments** should outline what's in the file, its main use cases, and its intended audience in the opening paragraph or two; **class comments** should describe the type, its important methods, and its purpose in nouned form ("The `Foo` class contains… and allows you to…"). If an API cannot be described succinctly at file scope, that is often a signal the API itself is doing too many jobs and should be split — see [choosing documentation types](choosing-documentation-types.md) for the parallel rule that a page, like an API, should have one clear purpose.
