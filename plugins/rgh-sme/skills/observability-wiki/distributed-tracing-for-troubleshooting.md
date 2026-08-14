---
type: concept
title: Distributed Tracing for Troubleshooting
description: Distributed tracing systems propagate an ID across service calls so a single request's full path can be reconstructed, making it possible to pinpoint which specific slow or failing RPC in a call chain is responsible for a symptom.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 12"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §1"
---

Tools like Google's Dapper and its open-source descendants (e.g. Zipkin) trace a request's propagation across microservice dependencies, letting an investigator pinpoint the specific slow or failing RPC responsible for an observed symptom rather than guessing which service in the call chain is at fault.

A debugging session investigating latency often starts with a question as simple as "can you find a slow trace?" — see [trace anatomy and spans](trace-anatomy-and-spans.md) for how a trace is structured, and [context propagation](context-propagation.md) for how the ID that ties a request's spans together moves across process and service boundaries. Tracing is complementary to, not a substitute for, function-level [profiling](fixed-counters-vs-profiling-vs-tracing.md) — see [profiling and tracing are complementary](profiling-vs-tracing-complementary.md). See [black-box vs. annotation-based tracing](black-box-vs-annotation-based-tracing.md) for the underlying design choice that makes this kind of correlation possible at all.

Two deployment properties determine whether a tracing system is actually useful for troubleshooting rather than just for the requests someone happened to think to instrument: **ubiquity** (even small unmonitored parts of the system can hide the real culprit, especially in shared infrastructure where a symptom in one service is actually caused by another tenant's load on a resource they both depend on) and **always-on collection** (the specific unusual behavior an investigation needs is often difficult or impossible to reproduce on demand, so it has to already have been captured when it happened). A further practical target worth designing for: trace data should reach queryable storage within roughly a minute of being generated — data that's hours old is still useful, but fast turnaround is what lets an investigator react to an anomaly while it's still happening rather than only reconstruct it after the fact.
