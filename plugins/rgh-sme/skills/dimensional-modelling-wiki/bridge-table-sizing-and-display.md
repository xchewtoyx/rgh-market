---
type: concept
title: Bridge Table Sizing and Display
description: How to estimate a ragged hierarchy bridge table's row count before building it, and how to sort and indent its output into natural tree order.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 7"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 10"
  - title: "Agile Data Warehouse Design"
    resource: "Agile Data Warehouse Design (Lawrence Corr with Jim Stagnitto), ch. 6"
---

Because a full [ragged hierarchy bridge table](ragged-hierarchy-bridge-table.md)'s row count is what drives its cost, it's worth estimating before building it: sum, level by level, the number of members at that level times the level's own number counting from the top (a 9-member, 4-level tree with 1/3/3/2 members per level costs 1×1 + 3×2 + 3×3 + 2×4 = 24 rows before accounting for any [type 2](slowly-changing-dimension-type-2.md) history). A quick, always-safe overestimate is `dimension members × (max levels − 1)`, useful for a rough sizing check without needing the level-by-level breakdown. In practice the row count only occasionally reaches an order of magnitude above the base dimension's own row count, since real hierarchies are rarely both very deep and very wide at once.

Displaying a tree in its natural hierarchical order (parents immediately followed by their own subtree, indented) needs an explicit **sequence number** column on the bridge, sorted "top to bottom before left to right" — plain name or level-number sorting alone doesn't work, since sorting only by level groups every same-depth node together regardless of which parent it belongs to, destroying the parent-child grouping a report reader needs. A report then sorts by sequence number and indents each row by its level number (e.g., `LPAD(' ', 3*(level-1)) || name` for level-based indentation). Leaving gaps between initial sequence numbers (multiples of 10 or 100, rather than consecutive integers) allows new nodes to be inserted later without renumbering every row that follows them — renumbering is otherwise required whenever a node is inserted mid-sequence, since sequence numbers must stay in strict hierarchical order for the sort to remain correct.
