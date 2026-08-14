---
type: concept
title: Write Buffering With a Durability Escape Valve
description: Buffering writes in memory and flushing them asynchronously cuts tail write latency sharply, and the durability risk that buffering introduces can be bounded — without paying the buffer's latency cost on every write — by routing just one replica's copy of each write around the buffer.
sources:
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §6.1"
---

Write latency in a replicated store is often dominated by disk access on the replicas involved, and — because the operation only returns once enough replicas have responded — by the *slowest* of those replicas, not the average. An in-memory **write buffer** in front of the storage engine (each write lands in the buffer immediately, is periodically flushed to disk by a background thread, and reads first check the buffer before falling through to storage) removes disk latency from the request path entirely for the common case.

## Measured Effect

One production deployment (Amazon's Dynamo) measured a **5x reduction in 99.9th-percentile write latency** at peak traffic from adding this buffer — and the effect held even with a buffer sized for only about a thousand objects, meaning the benefit comes from decoupling request-path latency from disk-flush latency, not from buffering a large fraction of the working set. Buffering also **smooths tail variance**, not just the tail's absolute value, since the request path no longer inherits whatever variability the underlying disk's queue depth or seek pattern happens to be exhibiting at that moment.

## The Durability Risk This Introduces

A write acknowledged from the buffer is not yet on disk; a crash before the background flush runs loses it. This is the same trade a page-cache write-back introduces at the OS level (contrast with [dirty page write throttling](dirty-page-write-throttling.md), where the kernel instead blocks writers once too much unflushed data accumulates, trading latency back for safety once a threshold is crossed) — here the trade is made deliberately and asymmetrically per-write instead of throttling uniformly.

## The Escape Valve: One Durable Replica Per Write

Rather than accepting the buffer's durability risk uniformly across every replica of every write, or giving it up entirely by disabling the buffer, a coordinator handling a replicated write can designate **exactly one of the N replicas** to perform a synchronous "durable write" — bypassing the buffer entirely and going straight to disk — while every other replica involved in that same write still uses its buffer. Because the coordinator only needs **W** replicas to respond to consider the write successful (see [tunable per-request quorum](tunable-per-request-quorum-nrw.md)), and the durable-write replica is only one contributor among several, the overall write's latency is still governed by the fastest W responses, not held hostage by the one replica doing the slower synchronous disk write. This converts an all-or-nothing durability/latency trade into a per-write guarantee — at least one durable copy exists — purchased at a cost that doesn't show up in the operation's observed latency at all, as long as enough of the other, buffered replicas respond quickly.

## The General Pattern

This is a specific instance of a broader move: when only a *subset* of parallel participants in an operation needs a stronger property (here, synchronous durability) for the operation as a whole to have that property, paying the stronger property's cost on only that subset — while the rest of the participants take the cheap path — captures most of the benefit of the strong guarantee everywhere without paying its latency cost everywhere. It works here specifically because the operation's completion criterion (W acks, not N acks) already tolerates some participants being slower than others.
