---
type: concept
title: Write the Comments First
description: >
  Writing interface comments at the start of implementing something, before
  the method body, produces better documentation and better designs than
  writing comments at the end — and eliminates the backlog of undocumented
  code that delay always produces.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 15"
---

Developers habitually delay documentation with "the code is still changing,
so I'd have to rewrite the comments" — but the deeper reason is usually that
documentation is viewed as drudge work to put off as long as possible. The
delay compounds ("it'll be more stable in a few weeks") until the
undocumented codebase has grown so large that backfilling comments looks even
less appealing, worsening the backlog further. Even if a developer eventually
goes back, the result tends to be poor: by then they've mentally checked out
of that code and rush through it, and because they're looking at finished
code while writing, the comments tend to just
[restate the code](comment-repeats-code-red-flag.md). Design rationale and
other information that never made it into the code will also have faded from
memory, so the resulting comments are missing exactly what they should most
be capturing.

The workflow that avoids this, applied to building a new class:

1. Write the class's interface comment first.
2. Write interface comments and method signatures for the most important
   public methods, leaving method bodies empty at this stage.
3. Iterate on these comments until the overall structure feels right.
4. Write declarations and comments for the most important instance
   variables.
5. Only then fill in method bodies, adding
   [implementation comments](implementation-comments.md) as needed.
6. New methods or variables discovered mid-implementation get the same
   treatment retroactively: interface comment before the method body,
   variable comment at the moment of declaration.

The end state: when the code is done, the comments are also done — there is
never a backlog of unwritten comments. Writing a method's interface comment
*before* its body specifically helps by forcing focus on the abstraction in
isolation, undistracted by implementation details, and the comments continue
to improve iteratively as coding and testing surface problems with the
initial wording.

On cost: total time spent typing code and comments combined, including
revisions, is unlikely to exceed roughly 10% of total development time — see
[comment-writing time investment](comment-writing-time-investment.md).
Writing comments first also tends to *stabilize* abstractions earlier, which
plausibly reduces how much code (not just comment) gets rewritten later,
since an abstraction that's never been pinned down in words tends to keep
shifting as implementation proceeds. See
[comments as a design diagnostic](comments-as-a-design-diagnostic.md) for why
this workflow's biggest benefit isn't documentation quality at all, but
design quality.
