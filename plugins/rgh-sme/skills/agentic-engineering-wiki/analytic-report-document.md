---
type: concept
title: Analytic Report Document
description: >
  Frame a prompt as an analytical report — introduction through conclusion —
  when the task is objective analysis rather than conversation.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

Models are trained on vast numbers of human-written analytical reports
(business, literature, science, law — though legal defense is best left to
professionals), which makes the report document archetype easy to leverage
per the [Little Red Riding Hood principle](little-red-riding-hood-principle.md).
Reports follow a familiar structure — introduction, leading to a conclusion,
often with a recap — into which gathered information slots naturally as
discussion or background sections. Reports favor objective analysis, which
lightens the model's cognitive load by not requiring it to simulate social
interaction the way an
[advice conversation document](advice-conversation-document.md) does; this
format also suits [chain-of-thought prompting](chain-of-thought-prompting.md)
well, since analysis-then-conclusion is exactly a report's native shape.

Two techniques specific to this archetype:

- **A Scope section** stating boundaries up front (e.g. "This report focuses
  solely on novels, excluding self-help books") rather than negotiating
  exclusions dialogically — models respect such boundaries more consistently
  when stated in report form than when negotiated turn by turn in
  conversation.
- **A clear transition** into decision-making mode where analysis ends and
  conclusion begins, since analysis typically precedes conclusion in this
  format; without one, the response risks meandering and needing extra
  parsing to extract the actual verdict. See
  [prompt transition](prompt-transition.md) for the general technique.

**Write report prompts consistently in Markdown.** It's near-universal in
training data, so models know it well; it's simple and lightweight to write
and interpret; headings define a hierarchy that lets you organize, rearrange,
or omit sections while preserving structure; indentation generally doesn't
matter outside triple-backtick code blocks, which handle
indentation-sensitive content like source code; it renders directly for
users; and hyperlinks let the model include easily-parsed, verifiable links.

A **table of contents** at the start of a long Markdown report prompt helps
the model orient, the same way it helps a human reader, and controls the
completion in two ways:

1. **Scratchpad sections** — adding `# Ideas` or `# Analysis` sections before
   `# Conclusion` in the table of contents guides the model toward a more
   informed conclusion, while letting the application ignore or discard the
   earlier sections when parsing the output.
2. **Signaling the response's end** — adding a `# Appendix` or `# Further
   Reading` section after the conclusion, then setting that heading as a
   [stop sequence](completion-stop-condition-design.md), ensures the model
   finishes without wasting compute generating content past the conclusion.
