---
type: concept
title: CPU Flame Graphs
description: A flame graph visualizes a large collection of sampled stack traces as a stacked, width-proportional set of bars, making CPU hot spots instantly visible without reading through raw sample data.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 13"
---

A CPU flame graph turns a large set of sampled stack traces (from [statistical profiling](fixed-counters-vs-profiling-vs-tracing.md)) into a single visualization: each unique call stack becomes a stack of horizontal bars (one per frame), and the width of each bar is proportional to how often that frame appeared across all samples — not to time order. Wide plateaus, especially near the top of the graph, point directly at functions consuming a disproportionate share of CPU. The quality of those stacks depends on how they were captured — see [stack unwinding methods](stack-unwinding-methods.md) for the trade-offs between frame pointers, ORC, and DWARF, and why a profile can silently produce shallow, misleading stacks if the target binary is incompatible with the unwind method in use.

The generation pipeline is: sample stack traces at a target frequency → collapse identical stacks into folded, semicolon-delimited lines with a count → render the folded output as an SVG. This pipeline is tool-agnostic — any profiler that can emit or export stack samples (not just `perf`) can feed it.

Flame graphs are most useful for finding *functions called often with medium individual cost*, or functions near the graph's root with little time in their children — these are the shapes that indicate real optimization opportunity, as opposed to a single rare expensive call. See [profiling and tracing are complementary](profiling-vs-tracing-complementary.md) for how this fits alongside distributed tracing in a debugging workflow, and [heatmaps vs. percentiles for visualizing variance](heatmaps-vs-percentiles-for-variance.md) for another case where an aggregate visualization can hide the information the raw sample distribution provides.
