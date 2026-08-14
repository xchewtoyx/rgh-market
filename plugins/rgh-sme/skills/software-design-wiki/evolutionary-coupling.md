---
type: concept
title: "Evolutionary Coupling: Files That Change Together"
description: >
  Mining version-control history for files that are repeatedly committed
  together reveals coupling invisible to static structural analysis — two
  files with zero call or inheritance relationship can still be as tightly
  coupled as if they shared code.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman, with Yuanfang Cai), ch. 23"
---

[Coupling](coupling.md) is usually inferred from **structural**
dependencies — one file calling, inheriting from, or importing another,
visible to static analysis. But version-control history exposes a second,
independent signal: **evolutionary coupling**, the frequency with which
two files are committed together. The two signals can disagree sharply. A
worked case (Apache Camel) found a structural dependency graph that looked
sparse and healthy, while the same files' co-change history was dense —
pairs of files with *zero* structural relationship nonetheless changed
together repeatedly. The architects independently confirmed the diagnosis:
despite the clean-looking structural picture, nearly every change was
costly and delivery timing was hard to predict. Structural analysis alone
had badly understated the real coupling.

**Modularity violation** is the sharpest instance of this: two files with
no structural dependency relationship at all that nonetheless change
together frequently. That combination is the fingerprint of a hidden,
unencapsulated shared "secret" — some assumption or piece of knowledge both
files depend on without either one owning it explicitly, exactly the
failure mode [information hiding](information-hiding.md) is meant to
prevent. Structural analysis can't see this kind of coupling because there
*is* no call or inheritance edge to find; only the co-change history
reveals it. The fix is the same as any other information-hiding failure:
find the shared secret and give it an explicit, owned home — an
abstraction neither file has to independently know about anymore.

The practical implication: judging a design's coupling from source code
alone, however careful the review, can miss real coupling that only shows
up as a pattern across many commits over time. Where the history is
available, checking co-change frequency between suspected-independent
files is a concrete, cheap way to catch modularity violations that a
structural read-through would never surface.
