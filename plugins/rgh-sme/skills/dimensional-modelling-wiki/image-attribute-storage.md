---
type: concept
title: Image Attribute Storage
description: The trade-off between storing a filename reference to an image versus embedding the image as a database blob when a dimensional model needs to carry pictures.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), 3rd ed., ch. 14"
---

When a business process captures images or photographs alongside its usual numeric and text data — clinical images in an electronic medical record, for example — there are two ways to attach them to a dimensional model. Storing a filename or path reference (as a [dimension-table](dimension-table.md) attribute or degenerate value) lets other image-handling tools freely access the image directly, but requires maintaining a separate graphic-file store that stays in synchrony with the database as rows are added, changed, or deleted. Embedding the image as a blob directly in the database keeps everything in one place and avoids that synchronization burden, at the cost of database size and of losing easy access for tools that expect ordinary image files.

This is a narrower instance of the same underlying question as [text comments dimension](text-comments-dimension.md): bulky, largely unqueryable content doesn't belong cluttering the [fact-table](fact-table.md) itself, and the choice comes down to where to park it and how directly other systems need to reach it.
