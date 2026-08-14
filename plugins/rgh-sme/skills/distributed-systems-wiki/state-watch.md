---
type: concept
title: State Watch
description: >
  Pushing change notifications to subscribed clients over an existing
  connection instead of making them poll, and the harder problem of not
  losing events across a disconnect.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 27, State Watch"
---

# State Watch

Polling for changes is awkward for client logic and wasteful at any scale;
opening a dedicated connection per watched value doesn't scale on the
server side either. The fix: a client registers interest in a key (or a
whole prefix, for hierarchical stores) once, over a connection it already
maintains — typically the same [single socket channel](single-socket-channel.md)
used for other traffic — and the server pushes a notification down that
connection whenever the watched state changes, fanning out to every
watching connection from a lookup keyed by the changed key. This is a core
building block of a [coordination service](coordination-services.md): peers
learn about a new leader, an expired [lease](distributed-locks.md), or a
membership change this way instead of polling for it.

## The hard part: not losing events across a disconnect

A client that reconnects — say, to a newly elected leader — needs to know
whether it missed anything while disconnected. The client resends its watch
registrations along with the last event index it actually received, and the
server is expected to backfill everything since. This only works if the
server assigns a strict, monotonic index to every state change, which comes
for free if the server is backed by a [write-ahead
log](write-ahead-log.md), since every entry already carries a log index.
Three backfill strategies, in increasing sophistication and cost:

1. **Derive events from current state.** Compare the client's last-seen
   change number against each current value's stored version and replay
   anything newer as a synthetic update. Cheap, but can miss transient
   events entirely — a key created and deleted entirely within the
   disconnect window leaves no create event to derive, because the key is
   simply gone by the time anything looks. ZooKeeper uses this approach, and
   compounds the risk by making watches one-shot by default: once fired, a
   watch must be explicitly re-registered, so a client must independently
   re-check current state around every watch reset to avoid a gap.
2. **Bounded event history.** Keep a fixed-size eviction queue of recent
   events and replay from it on reconnect. Simple, but a client disconnected
   longer than the window loses events anyway.
3. **Multi-version storage.** Keep every version of every key (see
   [versioned value](versioned-value.md)), so "give me everything since
   version N" is always answerable in full, no matter how long the client
   was gone. This is what etcd v3+ does.

A contrasting design avoids the problem altogether: Kafka's newer
architecture has brokers **pull** the metadata log from a controller quorum
by offset, exactly like an ordinary consumer, rather than having the server
push events — resuming is just "ask from the last offset you have," with no
separate push/notify machinery and therefore nothing to lose track of. This
replaced Kafka's original design, which used exactly the push-and-reconnect
pattern above: consumers watched broker and consumer registries and
recomputed [partition assignment](consumer-group-rebalancing.md) whenever a
watch fired. See [push vs. pull consumption](push-vs-pull-consumption.md) for
the general trade-off this switch is an instance of.

## Backpressure

Pushing events onto a connection with no flow control can overwhelm a slow
consumer — a real production issue in etcd's watch implementation. Reactive-
streams-style frameworks (and protocols such as RSocket) are the structured
way to build backpressure into an event-push path rather than bolting it on
after the fact, echoing the same [singular update
queue](singular-update-queue.md) backpressure concerns on the sending side.
