---
type: concept
title: Pathstring Hierarchy Attribute
description: An alternative to a hierarchy bridge table that encodes each node's full ancestry path as a wildcard-searchable string attribute on the dimension row.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 2-3, 7"
---

A pathstring is an alternative to a [ragged hierarchy bridge table](ragged-hierarchy-bridge-table.md) for representing a [ragged hierarchy](ragged-hierarchy.md) without SQL language extensions. Each node's pathstring is its parent's pathstring plus the next sequential letter (A, B, C, ...) under that parent; a trailing "+" marks a node with children, and a trailing "." marks a leaf. The tree is navigated via wildcard pattern matching: `A*` (asterisk = variable-length wildcard) retrieves the whole tree, `*.` retrieves only leaf nodes, and `?+` (question mark = single-character wildcard) retrieves the topmost node.

A related alternative, **modified preordered tree traversal**, assigns every node a (Left, Right) number pair identifying all of its descendants; the whole tree is enumerable from the topmost node's pair (e.g., `Left BETWEEN 1 AND 26`), and leaf nodes are exactly where Left and Right differ by 1.

Both alternatives embed the hierarchy definition directly in the [dimension-table](dimension-table.md) row rather than in a separate [bridge table](bridge-table.md), and share two disadvantages compared to a [ragged hierarchy bridge table](ragged-hierarchy-bridge-table.md): the hierarchy definition is locked into the dimension, making it hard to swap in an alternative rollup structure at query time, and both are vulnerable to a "relabeling disaster" where a small tree change forces relabeling a large part of the tree — fine in a small textbook example, but dangerous with thousands of real nodes. Pathstrings are sensitive to relabeling because inserting a new node forces relabeling every node to its right under the same parent; modified preordered tree traversal is even more fragile, since any tree change forces renumbering the entire rest of the tree to the right of the change.
