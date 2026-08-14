---
type: concept
title: Naked CRC
description: >
  Narrate a system's architecture in real time using blank index cards as
  physical stand-ins for object instances — motion and spatial position make
  involved interaction scenarios easier to grasp than a static diagram.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 17"
---

CRC (Class-Responsibility-Collaboration) cards — each listing a class's
name, responsibilities, and collaborators, with contested responsibilities
physically crossed out and moved to another card — were an early, tangible,
discussable stand-in for OO design, later largely supplanted in industry
practice by UML. That shift bred a misconception worth naming directly: UML
is a documentation notation, not itself a design method ("draw plenty of
diagrams, and then write code afterward" isn't design).

**Naked CRC** keeps CRC's spirit but uses **blank** index cards — no writing
at all. The presenter narrates a system's architecture while physically
laying cards on a table, moving, overlapping, and pointing at them to
represent objects and their interactions in real time. Two guidelines: cards
represent **instances**, not classes; overlapping cards represent a
**collection** of instances. The claimed effect: motion and spatial position
make involved interaction scenarios easier to grasp and more memorable than
a static diagram would be — closely related in spirit to
[sketching as a reading aid](sketching-and-markup-for-understanding-code.md),
but built for live narration of dynamic behavior rather than a static
structural picture.
