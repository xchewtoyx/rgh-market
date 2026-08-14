---
type: concept
title: eBPF as an Instrumentation Accelerator
description: eBPF lets you attach safe, sandboxed programs to kernel and user-space events without recompiling or modifying the target, making it a good gap-filler for instrumenting code you can't or won't change directly — but it complements rather than replaces deliberate application instrumentation.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 15 & app. C"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 7"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §7"
---

Extended BPF (eBPF) is an in-kernel virtual machine that runs sandboxed bytecode: a kernel verifier statically checks the program before load (bounded execution, safe memory access, no possibility of a kernel panic), and a JIT compiler then translates it to native machine code for near-zero-overhead execution. Programs can attach to [kprobes/kretprobes, tracepoints, uprobes/uretprobes, and USDT points](stable-vs-dynamic-instrumentation-points.md), as well as network layers (socket filters, traffic control, XDP) and security hooks (LSM) — all without recompiling or modifying the target binary. Results are typically computed via [in-kernel aggregation](in-kernel-aggregation-over-event-streaming.md) rather than streamed raw.

This makes eBPF-based instrumentation (e.g. OpenTelemetry's eBPF Instrumentation / OBI) a good **accelerator and gap-filler**: it requires no code changes, incurs no in-process runtime overhead, and can bridge or propagate [trace context](context-propagation.md) through legacy or otherwise-uninstrumented services.

Tying kernel-visible detail to an active application-level [span](trace-anatomy-and-spans.md) in a fully general way is still hard — the two live in different worlds (kernel event stream vs. user-level trace context), and continuously correlating every kernel event to the right span is intrusive and expensive. A pragmatic middle ground used at scale: rather than trying to merge the two event streams generally, take periodic snapshots of a handful of kernel-level activity parameters from user space (e.g. via eBPF probes) and attach them as annotations on whichever span is active at snapshot time — cheaper than full correlation, and still enough to notice when kernel-level activity (not just userspace application behavior) explains an otherwise-unexplained slow span. It is not a replacement for deliberate application-level instrumentation, though — it can observe that a call happened and how long it took, but it can't capture domain-specific business context (which only the application itself knows) the way [custom instrumentation](automatic-vs-custom-instrumentation.md) can. Two tooling frameworks build on this: BCC (a Python/C framework with ~70 standard tools like `execsnoop`, `biolatency`, `runqlat`) for complex multi-probe tools, and `bpftrace` (an AWK/DTrace-inspired high-level language) for rapid, ad hoc one-liners during an investigation.

## bpftrace One-Liner Reference

During production incidents, `bpftrace` enables responders to dynamically instrument the system to gather high-fidelity data on-CPU and off-CPU. Common diagnostic one-liners include:

### CPU and Scheduler
* **Sample CPU stack traces at 99 Hz (Flame Graph input)**:
  `bpftrace -e 'profile:hz:99 { @[kstack] = count(); }'`
* **Count context switches by process name**:
  `bpftrace -e 'tracepoint:sched:sched_switch { @[args.prev_comm] = count(); }'`
* **Summarize CPU run queue latency (wait time histogram)**:
  `bpftrace -e 'tracepoint:sched:sched_wakeup { @qtime[args.pid] = nsecs; } tracepoint:sched:sched_switch /@qtime[args.next_pid]/ { @usecs = hist((nsecs - @qtime[args.next_pid]) / 1000); delete(@qtime[args.next_pid]); }'`

### Memory
* **Count page faults by process name**:
  `bpftrace -e 'tracepoint:exceptions:page_fault_user { @[comm] = count(); }'`
* **Trace heap allocation sizes (`brk` system call)**:
  `bpftrace -e 'tracepoint:syscalls:sys_enter_brk { @[comm] = count(); }'`

### File System and Block I/O
* **Measure VFS read latency histogram**:
  `bpftrace -e 'kprobe:vfs_read { @start[tid] = nsecs; } kretprobe:vfs_read /@start[tid]/ { @us = hist((nsecs - @start[tid]) / 1000); delete(@start[tid]); }'`
* **Trace open file paths with process name**:
  `bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s opened %s\n", comm, str(args.filename)); }'`
* **Block device I/O latency histogram**:
  `bpftrace -e 'tracepoint:block:block_rq_issue { @start[args.dev, args.sector] = nsecs; } tracepoint:block:block_rq_complete /@start[args.dev, args.sector]/ { @usecs = hist((nsecs - @start[args.dev, args.sector]) / 1000); delete(@start[args.dev, args.sector]); }'`

### Network
* **Trace TCP retransmissions**:
  `bpftrace -e 'tracepoint:tcpretrans:tcpretrans { printf("Retransmit: %s -> %s\n", args.saddr, args.daddr); }'`
* **Count outbound TCP connections by process**:
  `bpftrace -e 'kprobe:tcp_connect { @[comm] = count(); }'`
