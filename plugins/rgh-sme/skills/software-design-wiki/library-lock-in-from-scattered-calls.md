---
type: concept
title: Library Lock-In From Scattered Direct Calls
description: >
  Every hard-coded call to a library class is a place a seam could have
  been, and skipping that isolation risks real vendor lock-in, not just a
  testing inconvenience.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 14"
---

Buying or reusing a library saves time, but scattering direct calls to it
"promiscuously throughout your code" creates real lock-in, not just a
testability problem. A vendor raising royalties to unprofitable levels can
leave a team with no realistic exit, because switching vendors would amount
to a full rewrite when calls to the original library were never isolated in
the first place. **"Avoid littering direct calls to library classes in your
code. You might think that you'll never change them, but that can become a
self-fulfilling prophecy."**

This reframes [the seam concept](seam.md) onto third-party code directly:
**"Every hard-coded use of a library class is a place where you could have
had a seam."** Some libraries define interfaces for their concrete classes
(seam-friendly out of the box); others make classes `final`/`sealed` or
methods non-virtual, closing off fakeability entirely — see
[library design constraints vs. testability](library-design-constraints-vs-testability.md)
for why that closing-off happens and how to work around it, and
[skin and wrap the API](skin-and-wrap-the-api.md) for the default response
when a library's own surface can't be made into a seam directly.
