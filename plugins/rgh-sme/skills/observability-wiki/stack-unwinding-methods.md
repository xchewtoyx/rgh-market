---
type: concept
title: Stack Unwinding Methods for Profiling
description: Capturing a call stack for a profile or flame graph requires walking the stack via frame pointers, a kernel-maintained unwind table, or DWARF debug info, and each method trades off overhead, accuracy, and binary compatibility differently.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 3"
---

Every stack sample behind a [CPU flame graph](cpu-flame-graphs.md) or profiling trace has to be reconstructed by walking a thread's call stack at the sample point, and how that walk happens materially affects whether the resulting profile is trustworthy:

- **Frame pointers** — the compiler reserves a register (`%rbp` on x86-64) to maintain a linked list of stack frames, which a sampler can walk cheaply and in real time. This is the cheapest and most tracing-friendly option, but it costs a general-purpose register per function call, so many toolchains compile with `-fomit-frame-pointer` by default — silently breaking stack walks for any profiler that depends on this method unless the target binary was built with `-fno-omit-frame-pointer`.
- **ORC (Oops Rewind Capability)** — a compact, kernel-specific unwind metadata format that lets the Linux kernel unwind its own stack accurately without needing frame pointers reserved in kernel code.
- **DWARF debug info** — full call-frame information emitted by `-g`. This is the most accurate method, including through heavily optimized code, but parsing it is comparatively expensive, which makes it a poor fit for high-frequency, low-overhead production sampling.

The practical consequence: before trusting a flame graph or [continuous-profiling](continuous-profiling.md) stack trace, check which unwind method produced it and whether the target binary is compatible with that method — a profile silently missing frame pointers can look like a shallow, misleading call stack rather than visibly failing.
