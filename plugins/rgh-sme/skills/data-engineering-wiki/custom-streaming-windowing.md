---
type: concept
title: Custom Streaming Windowing
description: >
  Window assignment and optional merging as the two building blocks for
  windowing strategies beyond fixed, sliding, and stock session windows.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 5"
---

Most engines ship fixed, sliding, and session windowing. Real workloads often
need custom strategies. In Beam, custom windowing consists of:

1. **Window assignment** — places each element into an initial window; at the
   limit, every element gets a unique window.
2. **(Optional) window merging** — allows windows to combine at grouping time
   (as with [session windows](streaming-window-types.md)).

Stock `FixedWindows`: assignment by timestamp, size, and offset; no merging.
Stock `Sessions`: assignment to proto-session windows at each record's
timestamp spanning the gap duration; merging combines overlapping sessions.

Three common custom variants:

**Unaligned fixed windows** — default fixed windows align across all keys,
causing synchronized completion bursts at scale (millions of windows firing
simultaneously). Fix: add a hash-based per-key time shift to window start
calculation so windows align within a key but spread across keys over time.
Trade-off: reduced peak provisioning vs. lost cross-key temporal alignment.
Generally requires custom windowing support.

**Per-element/per-key fixed windows** — when each customer configures its own
window size (carried as record metadata), assignment reads per-element size
instead of a global constant. Different keys run different window lengths
through the same pipeline. Too use-case-specific to standardize in a general
API but trivial as custom assignment logic.

**Bounded sessions** — plain sessions can grow without limit; some use cases
need caps (semantic limits, spam protection). Extend session merge logic with
a `maxSize`: when merging would exceed the cap, flush the current merge
candidate and start a new session. Without custom windowing, bounded sessions
require post-hoc downstream decomposition — losing incremental aggregation
benefits and defeating spam protection that needs early truncation.

Apache Flink supports custom windowing to a comparable (even greater, via
custom window evictors) extent.
