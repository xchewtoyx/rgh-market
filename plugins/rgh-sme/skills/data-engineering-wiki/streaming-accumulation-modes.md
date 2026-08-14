---
type: concept
title: Streaming Accumulation Modes
description: >
  How successive panes for the same window relate — discarding, accumulating,
  or accumulating with explicit retractions — and which downstream consumers
  each mode suits.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 7"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 9"
---

When [triggers](streaming-triggers-and-panes.md) ungroup a table back into a
stream, the **accumulation mode** determines what each emitted pane carries
when multiple panes fire for the same window over time. Three useful modes
(also called delta mode, value mode, and value-and-retractions mode):

**Discarding** — stored state is discarded after each pane fires; each pane is
independent. Downstream consumers that sum received deltas themselves suit
this mode. Summing all panes gives the correct total; the final pane alone
may not.

**Accumulating** — state is retained; each new pane builds on prior panes.
Suits consumers that simply overwrite previous values (key/value stores).
The final pane alone is correct; naively summing all panes double-counts
earlier contributions.

**Accumulating and retracting** — like accumulating, but each new pane also
emits an explicit **retraction** of the previous value ("remove X, replace
with Y"). Essential when:

- Downstream consumers regroup by a different dimension, so a corrected value
  may land in a different group than the old one — overwrite is insufficient.
- Dynamic windows (e.g.,
  [session windows](streaming-window-types.md)) merge, superseding multiple
  prior windows at once.

In [streaming SQL](streaming-sql-extensions.md), accumulating-and-retracting
should be the default under the covers (`Sys.Undo` column) because
accumulating alone breaks multi-stage grouped queries; omitting `Sys.Undo`
from SELECT yields accumulating-only semantics.

Example: panes with inputs [3] then [8,1] for the same window:

| Mode | Pane 1 | Pane 2 | Final value | Sum of panes |
| --- | --- | --- | --- | --- |
| Discarding | 3 | 9 | 9 | 12 ✓ |
| Accumulating | 3 | 12 | 12 ✓ | 15 ✗ |
| Accumulating & retracting | 3 | 12, −3 | 12 ✓ | 12 ✓ |

Cost/complexity ordering: discarding < accumulating < accumulating-and-
retracting. Accumulation mode is another axis — alongside triggers and
watermarks — for trading correctness, latency, and cost.
