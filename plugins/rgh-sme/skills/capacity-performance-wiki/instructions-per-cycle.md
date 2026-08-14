---
type: concept
title: Instructions Per Cycle (IPC)
description: An architectural metric measuring the average number of instructions executed per CPU clock cycle, indicating whether CPU utilization is compute-bound or memory-stalled.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 6"
---

**Instructions Per Cycle (IPC)** is a critical microarchitectural metric that quantifies the efficiency of CPU execution. It is calculated by dividing the number of completed (retired) assembly instructions by the number of CPU clock cycles consumed:

$$\text{IPC} = \frac{\text{Instructions Retired}}{\text{CPU Clock Cycles}}$$

Its inverse is **Cycles Per Instruction (CPI)** ($\text{CPI} = 1/\text{IPC}$).

## The Pitfall of Raw CPU Utilization

Standard system monitoring tools (e.g., `top`, Prometheus `node_cpu_seconds_total`) report CPU utilization based on the percentage of time a logical processor is not running the OS idle loop (`cpuidle`). 

However, **high CPU utilization does not mean the CPU is actively executing code.** Modern processors spend a massive fraction of their clock cycles stalled, waiting for data. CPU cycles are split into two categories:

1.  **Instruction Execution:** The CPU is actively executing arithmetic, logical, or control flow instructions (e.g., IPC $> 1.0$).
2.  **Stall Cycles:** The CPU core is idle, waiting for resources. The most common cause is memory access (stalling on an L3 cache miss while fetching data from DRAM, which takes $\sim 60\text{--}100 \text{ ns}$ or $\sim 200\text{--}300$ CPU cycles).

## Interpreting IPC

Understanding a system's IPC profile changes how capacity and performance tuning are approached:

*   **High IPC (IPC $> 1.0$): Compute-Bound.** The CPU is executing instructions efficiently. 
    *   *Bottleneck:* CPU clock speed or instruction volume.
    *   *Remediation:* Optimize compiler flags, choose more efficient algorithms (reducing total instruction count), or upgrade to processors with faster clock speeds (GHz).
*   **Low IPC (IPC $< 0.5$): Memory-Bound / Stalled.** The CPU is spending most of its time waiting for RAM.
    *   *Bottleneck:* Memory latency, memory bandwidth, or cache size.
    *   *Remediation:* Improve data cache locality (e.g., contiguous array layouts instead of linked pointers), reduce memory allocation rates, or upgrade to hardware with larger L3 caches (e.g., AMD 3D V-Cache) or faster memory buses (DDR5 vs. DDR4). Upgrading CPU clock speed will have negligible impact.

## How to Measure IPC

IPC cannot be observed via standard kernel metrics. It requires accessing **Performance Monitoring Counters (PMCs)**, which are hardware registers built into the CPU silicon. 

On Linux, the `perf` tool is used to query these counters:
```bash
# Measure system-wide hardware counters for 5 seconds
perf stat -a -- sleep 5
```
Output includes:
*   `cycles` (CPU clock cycles elapsed)
*   `instructions` (instructions retired)
*   `insn per cycle` (the calculated IPC)

## Follow-Up: Isolating Why Instruction Counts Changed

A change in total retired instructions for an identical workload is a strong signal, but IPC and instruction counts alone don't say *why* the count changed. Pairing this with software event counters — such as `perf stat -e page-faults` — can isolate the mechanism; a dropped minor-fault rate, for instance, points toward [transparent huge pages](transparent-huge-pages.md) changing the memory allocation path. See [explain unexpected performance changes](explain-unexpected-performance-changes.md) for why this kind of drill-down is worth doing even when the instruction count change looks like a pure win.
