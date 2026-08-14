---
type: concept
title: CPU Steal Time
description: The percentage of time a guest virtual machine's vCPU waits for physical CPU allocation from the hypervisor, indicating host overcommit or noisy neighbor activity.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 11"
---

In cloud and virtualized environments, **CPU Steal Time** (reported as `%steal` in `top`, `mpstat`, or Prometheus metrics) is the percentage of time a guest virtual machine (VM) wants to execute on a CPU but is prevented from doing so by the hypervisor because physical CPU resources are allocated to other VMs.

## The Hypervisor Scheduling Mechanism

In virtualized systems, guest virtual CPUs (vCPUs) are treated as standard user-space threads by the host operating system's CPU scheduler. 

```
+-------------------------------------------------+
| Physical Host (Hypervisor Scheduler)            |
|  [Physical Core 0]           [Physical Core 1]  |
+-------------------------------------------------+
         ^                              ^
         | (Scheduled)                  | (Blocked/Steal)
+-----------------+            +-----------------+
| Guest VM A      |            | Guest VM B      |
|  [vCPU 0]       |            |  [vCPU 0]       |
+-----------------+            +-----------------+
```

If the hypervisor overcommits host resources (subscribing more vCPUs across all tenant VMs than physical cores exist on the hardware) or if a neighboring VM on the same physical host runs a high-compute workload (a **noisy neighbor**), the host scheduler will fail to schedule the guest VM's vCPU threads immediately. 

The hypervisor tracks this waiting time and reports it back to the guest kernel, which exposes it as steal time.

## Interpretive Thresholds

*   **$0\%$ to $1\%$:** Normal operating conditions. Physical CPU resources are readily available.
*   **$1\%$ to $5\%$:** Moderate resource contention. The guest VM will experience minor performance degradation and latency jitter.
*   **$> 5\%$:** Severe CPU saturation on the physical host. Application throughput will drop sharply, and request latencies will spike unpredictably.

## Diagnostics

*   **`top` / `htop`:** Check the `%st` (steal) field.
*   **`mpstat -P ALL 1`:** Inspect steal time per vCPU core. If steal time is high on only one core, it might indicate a single-threaded noisy neighbor or specific core binding contention on the host.

## Mitigations

*   **Stop and Restart the VM:** In public clouds, stopping and starting a VM instance typically forces the orchestrator to reschedule the VM onto a different physical host, bypassing the current noisy neighbor.
*   **Avoid Burstable Instances:** Burstable instance families (e.g., AWS `t3`/`t4g`) allow CPU usage to burst above a baseline but throttle them once credits are exhausted, which can manifest as low baseline performance or appear as steal time depending on hypervisor configuration.
*   **Upgrade to Compute-Optimized or Dedicated Instances:** Sizing workloads onto instance types with dedicated physical hardware allocation (such as AWS compute-optimized `c` series or dedicated hosts) ensures a 1:1 mapping of vCPUs to physical threads, eliminating steal time.
