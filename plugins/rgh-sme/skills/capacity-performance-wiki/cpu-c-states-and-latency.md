---
type: concept
title: CPU C-States and Latency Jitter
description: How hardware-managed CPU power-saving states (C-states) introduce exit/wakeup latencies, causing tail latency jitter in low-latency systems.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 3"
---

In modern computer architectures, **CPU C-states** are hardware power-saving idle states. While highly effective at reducing energy consumption and heat dissipation, entering deep C-states introduces significant wakeup latencies that degrade tail latency in high-performance, real-time, or low-latency systems.

## C-State Hierarchy and Latency Trade-Off

CPU states are categorized into operational states (P-states, governing clock frequency and voltage) and idle states (C-states).

*   **C0:** The active state. The CPU core is actively executing instructions.
*   **C1 (Halt):** The basic idle state. The CPU clock is stopped, but the core can return to C0 almost instantaneously (typically $<1$ microsecond).
*   **C2, C3, C6, C7... (Deeper Idle States):** Deeper power-saving modes. The CPU progressively shuts down internal components (L1/L2 caches, clock generators, voltage regulators).
    *   **Trade-Off:** Deeper C-states save significantly more power, but they require a longer duration to transition back to C0 (exit/wakeup latency). Waking up from a deep state like C6 can take anywhere from $10 \text{ to } 200 \mu\text{s}$.

## Impact on Tail Latency

In [fan-out microservice architectures, even brief delays can amplify into significant tail latencies](tail-latency-amplification.md) at the system boundary. When a request or packet arrives on an idle machine:

1.  The network interface card (NIC) generates a hardware interrupt to signal packet arrival.
2.  The CPU scheduler attempts to wake up the worker thread and place it on an idle CPU core.
3.  If that core is in a deep C-state (e.g., C6), it must physically power back on, incurring a $100 \mu\text{s}$ delay before it can process the packet.
4.  This wakeup latency introduces unpredictable latency spikes (jitter) that directly inflate the [99th and 99.9th percentile latencies](latency-percentiles-vs-mean.md) (tail latency).

## Mitigation and Tuning

For systems demanding consistent, sub-millisecond latencies, deep C-states should be restricted or disabled:

1.  **Kernel Parameters:** Restrict the maximum idle state at boot time by adding parameters to the kernel command line:
    *   `intel_idle.max_cstate=1` (forces the Intel-specific idle driver to restrict cores to C1).
    *   `processor.max_cstate=1` (restricts ACPI processor idle states).
2.  **Power Management Quality of Service (PM QoS):** Applications can programmatically restrict C-states in real time by opening `/dev/cpu_dma_latency` and writing a 32-bit integer representing the maximum allowable latency (in microseconds). Writing `0` to this file disables all deep C-states, forcing CPU cores to remain in C0/C1. The restriction is active only while the file descriptor remains open.
3.  **CPU Governor:** Configure the Linux scaling governor to `performance` (e.g., `cpupower frequency-set -g performance`) to prevent CPU cores from downclocking (P-states), which further reduces latency overhead.
