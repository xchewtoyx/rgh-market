---
type: concept
title: Segregation of Duties as a Control Barrier
description: >
  Letting one actor control both the execution of a risky action and the
  verification that reports on it removes the independent feedback a
  control loop depends on, so the single point of control can distort or
  suppress the very data that would reveal its own drift.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 15"
---

A control loop is only as trustworthy as its sensor. Segregation of duties
— structurally separating the people who execute a risky action from the
people who verify and report on it — exists because a single actor who
holds both roles can quietly corrupt the sensor data upward, and nothing in
the loop above them will know.

**Barings plc (1995)** is the canonical demonstration. A single trader in
the Singapore derivatives office controlled both front-office trading
(taking positions) and back-office reconciliation and settlement
(verifying and reporting them) — a direct violation of a basic control
policy that exists specifically to prevent this. When a trading strategy's
losses mounted under market volatility, the trader concealed them by
routing them through an unreported error account, excluding that account
from the daily position, price, and trading reports sent to London.
London management, lacking derivatives expertise themselves, received
reports of extraordinary, mathematically implausible profits and — treating
the trader as an untouchable star performer — approved escalating margin
calls without ever verifying the underlying trading data. The firm's
reporting architecture had exactly one sensor for the state of the
Singapore book, and that sensor was controlled by the person with every
incentive to falsify it once losses began.

**Why the general design principle generalises past finance**: segregation
of duties is a structural instance of [proactive monitoring's insight that
a control loop is only as good as where its sensor
sits](proactive-monitoring-control-model.md) — here applied to *who*
controls the sensor rather than *when* in the process it reports. A single
point of control over both action and its own verification is a standing
vulnerability regardless of domain, because it converts what should be an
independent check into a self-report the checked party can simply edit.
The Basel II operational-risk framework's three pillars name the general
remedy this specific case instantiates: **people** (mandatory supervision
of every operational agent, including "star performers," and closing gaps
in executive domain expertise so oversight is not merely nominal),
**process** (structural separation between execution and verification
functions, enforced rather than merely documented), and **systems**
(reporting architecture that prevents any single point of control from
altering, filtering, or suppressing the data feeding it).

**The deeper lesson is about feedback versus feedforward control.** Barings'
management ran in a purely reactive, feedback-driven mode — approving
margin requests as they arrived rather than questioning their structural
cause — the same brittle, always-behind-events posture [the law of
stretched systems](law-of-stretched-systems.md) and [lack of
time](resilience-as-control.md) describe generally. A **feedforward**
alternative would have set explicit risk limits and hard verification
bounds *before* releasing capital, and tracked a leading indicator that
could not be manipulated by the party being measured — a simple continuous
reconciliation of cumulative trading losses against available capital
reserves would have exposed the insolvency early, precisely because that
comparison does not depend on the compromised party's own reporting.
