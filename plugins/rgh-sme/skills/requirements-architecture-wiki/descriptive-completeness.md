---
type: concept
title: Descriptive Completeness
description: >
  Architecture documentation is complete not when it covers everything,
  but when it states every intended element, relation, interface, and
  important property — plus what was deliberately left out.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 6"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 12"
---

Descriptive completeness means a piece of architecture documentation
states all the intended elements, relations, interfaces, and important
properties of what it covers — and, just as importantly, states what was
deliberately omitted. A view that is silent about something can mean
either "this doesn't exist" or "this exists but wasn't considered
important enough to show," and a reader cannot tell which without the
document saying so.

This matters most where a view establishes a boundary: a context diagram
that identifies external entities, external interfaces, and the system
boundary itself is only useful if its arrows have precise semantics — what
kind of interaction each one represents — rather than being decorative
lines. See [context diagram](context-diagram.md) for the specific
technique. Refinement — relating a coarse element to a more detailed
representation of the same thing — is different from decomposition
(breaking one element into parts), and the correspondence between the
coarse and detailed versions needs to be recorded explicitly so the two
views stay consistent with each other rather than silently drifting apart;
see [crosscutting structure documentation](crosscutting-structure-documentation.md).

Completeness, accuracy, and clarity are rarely all maximized in one
document — more completeness can hurt clarity; exhaustive edge-case
accuracy can obscure the main point. A "good" document is one doing its
intended single job per [documentation type by
purpose](documentation-type-by-purpose.md): reference favors completeness
(with some clarity cost), conceptual favors clarity (sacrificing some
completeness), landing favors organization over discussion. Focus on
audience needs rather than dumping every fact the author knows.
