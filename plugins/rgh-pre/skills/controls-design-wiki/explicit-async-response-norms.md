---
type: concept
title: Explicit Async Response Norms
description: >
  Establish and communicate an explicit expected response-time norm for an
  asynchronous channel (e.g. "email doesn't mean respond within the hour"),
  so its asynchronous nature isn't silently overridden by an unstated
  expectation of instant response.
sources:
  - title: "The Canary Code: A Guide to Neurodiversity, Dignity, and Intersectional Belonging at Work"
    resource: "The Canary Code (Ludmila N. Praslova, PhD), Chapter 7: Work Organization — Productivity and Purpose"
---

A channel designed to be asynchronous (email, a message queue) still
behaves synchronously in practice if everyone using it implicitly expects
near-instant replies — the tool's async design doesn't do anything if the
surrounding norm contradicts it. Left unstated, this default gets set by
whoever responds fastest or complains loudest, not by deliberate choice.
Stating the expected response window explicitly (and having whoever sets
the norm actually model it, e.g. not replying in real time themselves)
makes the channel's asynchronous nature real rather than nominal, and
removes the standing low-grade pressure to monitor it continuously.
