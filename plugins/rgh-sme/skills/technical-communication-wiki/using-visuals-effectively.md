---
type: concept
title: Using Visuals Effectively in Documentation
description: >
  A visual belongs in documentation only if it passes three tests —
  comprehension, accessibility, performance — and each visual type
  (screenshot, diagram, video) has its own failure modes to check for.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 6"
---

Visuals supplement prose; they don't replace it. Every image should pass three tests before it's included: **comprehension** (does it directly help the reader understand or do something), **accessibility** (does it work for people with access needs — alt text, sufficient contrast, no meaning conveyed by color alone), and **performance** (does it load acceptably on constrained devices or connections). A relevant image draws useful attention; a decorative or overcrowded one competes with the content it's supposed to support.

**Screenshots** should be introduced in the surrounding prose and placed near the step they illustrate, cropped of surrounding clutter, and sized so their important details are actually legible — not so small the reader has to guess. Describe the image's meaningful content in the main text too, not only in alt text, and never put material a reader needs to copy — commands, IP addresses, code — only inside an image, where it can't be selected or searched.

**Diagrams** should each simplify one idea at one level of abstraction, not try to show everything about a system at once. A box-and-arrow diagram shows entities and the relationships or data flow between them; a flowchart shows a path and its decision points — though once the decision points themselves have enough interacting conditions, a flowchart stops being the right tool and an [exhaustive matrix](exhaustive-matrices-for-unambiguous-logic.md) is; a swimlane diagram shows responsibility distributed across actors. Sketch the entities, relationships, and process before choosing a diagram tool, then keep shapes, labels, and directionality consistent and add a legend if the notation isn't self-evident. Practical constraints worth checking explicitly: connectors shouldn't cross if it can be avoided, meaning shouldn't rely on color alone, and contrast should meet a real accessibility threshold (a 4.5:1 ratio is cited as a working bar). An overloaded diagram trying to show too much should split into a layered overview-plus-detail pair rather than staying as one dense image; place a diagram beside its explanation, and prefer a scalable format like SVG for anything published.

**Video** is expensive to produce and — more importantly — expensive to maintain, since a UI or workflow change can make a video obsolete faster than it can make prose obsolete; use it only where it's demonstrably better than text and images for the specific thing being shown, and budget for professional production, captions, a timestamped transcript, accessible hosting, and a concrete plan to reshoot after product changes, not just the initial recording. Whatever the visual type, review it in actual page context and across responsive layouts before publishing, and retain the editable source files — a diagram or screenshot without its source is effectively unmaintainable. See [diagrams as elicitation tools in stakeholder review](diagrams-as-elicitation-tools-in-review.md) for a related but distinct payoff a diagram can have in a live review setting, beyond helping a solo reader comprehend it.
