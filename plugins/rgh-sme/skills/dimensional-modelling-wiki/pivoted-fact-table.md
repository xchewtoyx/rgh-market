---
type: concept
title: Pivoted Fact Table
description: A derived fact table that transposes another star's data between row-wise and column-wise orientation to simplify report development.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 14"
---

A pivoted fact table is a [derived schema](derived-schema.md) that transposes another star's data from row-wise to column-wise orientation, or vice versa. For example, a general ledger fact table recording one `amount` fact per `transaction_type` (Credit or Debit) produces two rows per account when grouped by type; many reports instead want one row per account with separate `debit_amount` and `credit_amount` columns. A pivoted fact table precomputes exactly that shape — one column per former dimension value instead of one fact plus a type dimension — implementable either as a view or as a physically loaded ETL table.

Pivoting is chosen for report simplification, not performance — the performance gain from precomputing a transposition is generally marginal, so it's worth building only for report-heavy applications where it saves significant development time. Its value scales with how many things are being transposed: with only two transaction types, doing the transposition inline in SQL or a report variable may be trivial and not worth a whole extra table to load and maintain; the case gets much stronger as the number of transposed values grows into the dozens.

**Reversibility isn't guaranteed.** Whether the pivoted table can be derived back into its original shape depends on the source grain: if the original star sits at a fine (e.g. transaction) grain, a pivoted table built by summarizing across many transactions loses that detail permanently and the original can't be reconstructed from it. Because of the potential for confusion over which of two representations of the same data to query, pivoted schemas — like other [derived schema](derived-schema.md)s — are sometimes restricted to trained developers rather than exposed generally.
