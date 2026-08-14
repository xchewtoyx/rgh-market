---
type: concept
title: Autoscaling Safety Practices
description: >
  Autoscaling is automation deciding how much of a service to run, so it
  inherits every general safeguard automation needs, plus failure modes
  specific to using load or utilization as the signal that drives it.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 11"
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 17"
---

# Autoscaling Safety Practices

Autoscaling is [intent-based automation](intent-based-automation.md)
applied to capacity: instead of an operator deciding how many instances to
run, the system computes it from an observed signal. That makes it subject
to the same [safeguards against runaway
automation](safeguards-against-runaway-automation.md) as any other
automation acting at scale, plus a set of pitfalls specific to using load
as the input:

- **Unhealthy instances can defeat it silently.** An instance that's
  failing but still counted in utilization averages makes the fleet look
  less loaded than it is, suppressing scale-up exactly when it's needed.
  Scaling from a load-balancer-observed capacity signal (which already
  discounts unhealthy instances) and pairing autoscaling with autohealing —
  restarting unhealthy instances, with enough grace time to actually come
  back up — closes this gap.
- **Scale up fast, scale down cautiously.** The cost of under-provisioning
  during a traffic spike is immediate and visible; the cost of
  over-provisioning during a lull is just wasted spend. Configuring the two
  directions asymmetrically — and keeping the system away from hard
  bottlenecks like CPU saturation, since the autoscaler needs lead time to
  react — reflects that asymmetry instead of treating scale-up and
  scale-down as mirror images.
- **Drain before destroying.** Removing an instance isn't just deleting
  it — the autoscaler first has to tell the load balancer to stop routing
  *new* requests to it, then give the instance itself a chance to finish
  whatever it's already handling before it's torn down. Skipping this and
  destroying an instance outright turns every routine scale-down into a
  small burst of failed in-flight requests. Implementing the drain signal
  is the service's own responsibility, not something the autoscaler can
  do for it — an autoscaling design that assumes instances can always be
  killed instantly is implicitly assuming every service behind it already
  handles shutdown gracefully, which is rarely true unless it was built in
  deliberately.
- **Bound it with explicit min/max limits.** Without a ceiling, a signal
  that stops correlating with real load — a buggy release burning CPU
  without doing useful work, or a downstream dependency that's hanging
  rather than failing outright — can drive the autoscaler into a spiral of
  runaway upsizing that exhausts quota and never resolves the underlying
  problem, because more capacity doesn't fix a bug or an unresponsive
  dependency.
- **Give on-call a kill switch.** A fast, obvious, well-documented way to
  disable or override the autoscaler is what lets a human step in when its
  automatic decisions are making an incident worse, without having to
  understand or fight the autoscaling logic itself under pressure.
- **Account for what scaling up costs downstream.** Adding frontend
  capacity increases load on every dependency behind it — databases, other
  microservices, shared quota. Autoscaling one tier without analyzing its
  effect on the tiers it depends on just moves the bottleneck instead of
  removing it.

Autoscaling is also rarely the only automated control loop touching
traffic — see [interacting automated control
loops](interacting-automated-control-loops.md) for what happens when it's
combined with load balancing and load shedding without a shared view of
how they affect each other.
