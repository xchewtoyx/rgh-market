---
type: concept
title: Virtual Waiting Room
description: An edge-level admission queue that holds excess arriving users outside the transactional system and releases them at a rate the backend can sustain, instead of either rejecting them outright or letting them all through at once.
sources:
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Michael T. Nygard), ch. 15"
---

A **virtual waiting room** is a queue placed in front of a system, at the edge (a CDN or reverse proxy), that admits users into the real transactional path at a controlled rate during a known or detected demand spike — a product launch, a ticket sale, a marketing campaign landing page — rather than letting every arrival reach the backend immediately or [shedding](adaptive-throttling.md) the excess outright.

## Why Not Just Shed Load Instead

[Load shedding](adaptive-throttling.md) protects a system by rejecting excess requests, which is the right response when the excess is unwanted or abusive traffic. A demand spike from a legitimate, anticipated event is different: every one of those users is a customer the business wants to serve, just not all in the same second. A waiting room reframes the problem from "how much traffic can we reject" to "how do we spread wanted traffic out over time without any individual user simply failing" — users wait in a low-cost holding queue instead of being turned away or hitting an error page.

## Mechanism

*   Requests arriving above the sustainable rate are intercepted before reaching the application or database tier — typically at a CDN or edge proxy layer, which is far cheaper to scale than the transactional backend itself.
*   Held users are shown a lightweight status page (position in queue, estimated wait) rather than consuming any backend resources while waiting.
*   The system admits waiting users into the real backend at a rate matched to measured backend capacity — the same discipline as [capacity headroom](capacity-headroom-safety-margin.md), but applied as a live release valve instead of a static provisioning target.

## Relationship to the Failure It Prevents

This directly addresses a **self-denial spike**: a company's own marketing or business action (a synchronized email blast, a launch announcement) produces an instantaneous demand impulse against [capacity headroom](capacity-headroom-safety-margin.md) sized from steady, averaged request rates — the same [load testing](capacity-test-types.md) blind spot as any other under-modeled demand spike, except this one is self-inflicted and, in principle, schedulable in advance. Where static edge caching absorbs a spike for content that's the same for every user, a waiting room is the complementary technique for the part of the spike that genuinely requires individual, transactional backend work that can't be cached away.
