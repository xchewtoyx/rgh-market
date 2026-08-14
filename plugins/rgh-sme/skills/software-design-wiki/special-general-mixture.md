---
type: concept
title: Special-General Mixture
description: >
  Special-general mixture is the red flag where a general-purpose mechanism
  also contains code specialized for one particular use of it, complicating
  the mechanism and creating information leakage between it and that use
  case.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 9"
---

**Red flag: special-general mixture** — "occurs when a general-purpose
mechanism also contains code specialized for a particular use of that
mechanism. This makes the mechanism more complicated and creates
[information leakage](information-leakage.md) between the mechanism and the
particular use case: future modifications to the use case are likely to
require changes to the underlying mechanism as well."

Worked example: a text editor needing multi-level undo/redo across text
edits, selection changes, cursor moves, and scroll position. The flawed
initial design put the entire undo mechanism inside the text class: it
tracked a list of undoable entries, auto-adding text-change entries while
accepting UI-added entries (selection, cursor, view changes) through extra
methods, and called back into UI code on undo/redo for the non-text entries.
The text class ended up mixing a general-purpose "track and step through a
list of actions" mechanism with special-purpose knowledge of things (like
selection) it had no other reason to know about — leakage between the text
and UI modules, extra cross-module methods just to shuttle undo data, and any
future undoable entity type would require new text-class methods.

The fix extracts the general mechanism into a standalone class:

```java
public class History {
    public interface Action {
        public void redo();
        public void undo();
    }
    History() {...}
    void addAction(Action action) {...}
    void addFence() {...}
    void undo() {...}
    void redo() {...}
}
```

`History` knows nothing about what an `Action` actually represents or how it
implements undo/redo — it just walks a list. Concrete `Action`
implementations (`UndoableInsert`, `UndoableDelete` in the text class;
`UndoableSelection`, `UndoableCursor` in the UI module) live wherever their
domain knowledge naturally belongs — see
[separating general- and special-purpose code](separate-general-and-special-purpose-code.md).
**Fences**, markers placed via `addFence()`, group related actions so one
user-facing undo request can span several underlying actions (restore text,
reselect it, rescroll to it); `undo`/`redo` walk the action list until hitting
the next fence. Fence placement policy is decided by higher-level UI code, not
by `History` itself.

The result is a three-way split, each independently understandable: the
general action-list mechanism, the specific action implementations (scattered
across whichever modules understand each action type), and the grouping
policy. Once the general-purpose core is separated out and given its own
class, the rest of the design tends to fall out naturally.
