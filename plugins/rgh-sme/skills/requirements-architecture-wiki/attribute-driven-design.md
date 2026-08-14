---
type: concept
title: Attribute-Driven Design (ADD)
description: >
  A repeatable seven-step design loop that turns prioritized
  architectural drivers into structures, one iteration at a time, with
  the design's rationale recorded as it is produced rather than
  reconstructed afterward.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 20"
---

Attribute-Driven Design (ADD) is a systematic method for turning
**architectural drivers** — [architecturally significant
requirements](architecturally-significant-requirement.md), functionality,
constraints, and design purpose — into concrete structures. Its value is
the same as any engineering method's: it is repeatable and teachable,
which is what lets architectural design be practiced as a discipline
rather than as one person's unrepeatable intuition. It explicitly does not
eliminate the creative part of design (selecting and adapting a solution);
it structures everything around that creative act so the rest of the work
— tracking what's been addressed, capturing why a choice was made — isn't
left to chance.

Design proceeds in **rounds** made of **iterations**, each iteration
running the same seven steps:

1. **Review inputs** — confirm this round's drivers (already prioritized
   by the techniques in [architecturally significant
   requirement](architecturally-significant-requirement.md)) are still
   correct and complete; a design method cannot compensate for bad
   inputs. For existing (brownfield) systems, this includes understanding
   the as-built architecture, which may require real reverse-engineering
   effort.
2. **Select a driver subset** to target for this iteration.
3. **Choose the element(s) to refine** — architectural decisions manifest
   as structures of elements, usually obtained by decomposing,
   combining, or improving elements already identified in an earlier
   iteration (or, in greenfield work, by refining the whole system as
   the only element that exists yet).
4. **Choose design concepts** — tactics, patterns, reference
   architectures, or externally developed components — that satisfy the
   selected drivers for the chosen elements. This is usually the hardest
   step; see [design concept selection](design-concept-selection.md).
5. **Instantiate elements, allocate responsibilities, and define
   interfaces** — turn the chosen concept(s) into concrete elements,
   assign each one's responsibilities, and connect them with
   [interfaces](interface-documentation.md), since a pattern or tactic on
   its own never fully specifies these.
6. **Sketch views and record decisions** — capture the resulting
   structures, even informally, as they're produced, together with the
   significant decisions and their rationale — see [architectural
   decision capture](architectural-decision-capture.md). This preliminary
   sketch is deliberately lighter-weight than the full [architecture
   documentation package](architecture-documentation-package.md) that may
   follow later; document with a specific purpose in mind (analysis,
   construction, or onboarding) rather than exhaustively.
7. **Analyze and review** — check, ideally through someone other than the
   designing architect, whether the iteration actually achieved its
   goal, then assess whether the round's design purpose has been met or
   more iterations are needed.

Iteration continues, resources permitting, until the highest-priority
drivers are addressed with enough confidence — the stopping point is a
risk judgment, not a fixed exit criterion. A lightweight **architectural
design backlog** (drivers plus supporting activities like prototypes or
reverse-engineering tasks, expandable as decisions surface new concerns)
and a three-column **design Kanban board** (Not Yet Addressed / Partially
Addressed / Completely Addressed) are enough to track this without
heavier project machinery.

ADD is one instance of the general pattern of iterating concrete designs
against explicit, stated requirements rather than starting from a
favored architecture and justifying it afterward; see [iterative design
against explicit requirements
(NALSD)](nalsd-iterative-design-against-requirements.md) for a
differently-shaped method built on the same discipline.
