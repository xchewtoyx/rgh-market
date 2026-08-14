---
type: concept
title: Step Dimension
description: A dimension recording where a transaction row sits within a sequential process, used to analyze session-like or multi-step behavior.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2, 8"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 9"
---

Most DW/BI measurements are point-in-time snapshots rather than sequences, but some processes — a web session built from page-view events across multiple servers, tied together by a cookie — need a way to understand where a given [transaction fact table](transaction-fact-table.md) row sits within an overall sequence. A step dimension records the current step number and how many further steps remain to complete the sequence; the first row is used only for one-step sessions, and subsequent rows are prebuilt for sessions of increasing length (typically prebuilt to accommodate sessions of at least 100 steps). A step dimension also implicitly carries "why" and "how" information about the wider sequence: its first-step row stands in for whatever triggered the sequence (e.g., the referring source of a web visit), and its last-step row stands in for how the sequence concluded (e.g., "just browsing" versus "completed purchase") — so labeling first/last rows explicitly lets a query find these pivotal cause-and-effect events (a "session killer" page, or the page immediately before one) with simple single-pass SQL, without any special sequence-analysis logic.

A step dimension can be given multiple [role-playing dimension](role-playing-dimension.md) references against the same fact table at page-event grain — for example, an overall-session role, a successful-purchase-subsession role, and an abandoned-cart-subsession role simultaneously — enabling queries like "first page of successful purchases" (the attractant page) or "last page of abandoned carts" (where the customer decided to leave).

## Growth and overflow handling

Because a step dimension must prebuild one row for every step position within every supported sequence length, its row count grows quadratically with the maximum sequence length supported: for a maximum of *n* steps, the dimension needs *n*(*n*+1)/2 rows (200 steps needs about 20,100 rows; 1,000 steps needs over half a million). Pre-populate only for a practical maximum that covers the large majority of real sequences (200 steps might cover 99% of sessions, for example), and handle sequences that exceed it with a small number of special, negative-keyed rows that record just the step number without the full row set the rest of the dimension carries — an unusually long sequence is itself often worth investigating as a symptom of an ETL error or a poorly defined sequence-termination rule, rather than something to size the dimension around by default.

Attaching step numbers to facts during ETL needs two passes rather than one: a first pass groups raw events into sequences using a business rule (the same cookie or IP address, with no gap longer than some threshold, for example) and counts each sequence's total length, and a second pass then assigns the correct step key to each event now that the sequence's final length is known — meaningfully more ETL work than an ordinary insert-only load.

An alternative technique for sequential behavior avoids a step dimension altogether: encode each possible step or product as a fixed code and concatenate a customer's whole sequence into one wide, delimited text column (e.g., `"11254|45882|53340|..."`). Wildcard searches on this string support queries like specific products bought in sequence, bought with intervening products, or one product bought while another was never bought — modern RDBMSs handle wide text fields (64,000+ characters) with wildcard search adequately for this purpose.
