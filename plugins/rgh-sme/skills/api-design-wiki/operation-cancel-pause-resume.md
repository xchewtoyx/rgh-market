---
type: concept
title: Operation Cancel, Pause, and Resume
description: >
  Custom methods that stop, pause, or resume tracked async work, with pause
  state carried in metadata rather than on the generic Operation type.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 10"
---

**Cancel** — `CancelOperation` (`POST .../:cancel`) blocks until cancellation
finishes and returns an Operation with `done: true` (cancellation completes
the operation, not necessarily successfully). Where possible, remove
intermediate artifacts so the system looks as if the work never ran; when
cleanup is impossible, metadata must point clients to manual cleanup (for
example files already written). Support cancel only where it helps users.

**Pause and resume** — `done` cannot mean "paused." Add `paused: boolean` on
the **metadata** type for operations that support pause, not on generic
`Operation` (which would imply every operation is pausable). `PauseOperation`
and `ResumeOperation` (`POST .../:pause`, `POST .../:resume`) mirror cancel:
block until the state change completes. Not all work is pausable (a rocket
launch after liftoff).

If a client is blocked on [wait](operation-polling-vs-wait.md) when cancel
runs, the wait should return the canceled Operation with `done: true` and an
appropriate result or error shape — not an HTTP error for retrieving status.
