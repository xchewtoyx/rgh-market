---
type: concept
title: Image Authenticity Verification
description: Techniques for confirming a photo or video is genuine, correctly contextualized, and not AI-generated or miscontextualized.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 4"
---
# Image Authenticity Verification

An image can be false in two distinct ways: it can be a real photo miscontextualized (wrong event, wrong date, wrong location), or it can be synthetically generated. Each requires a different verification technique.

## Reverse Image Search
The primary technique for catching a real-but-miscontextualized photo is **reverse image search** (e.g., via a search engine's image-search feature or a dedicated reverse-search tool) to find where else the image has previously appeared online. For video, screen-grab individual frames and reverse-search those.

**Named case**: a photo claimed to show a specific wildfire event, shared widely by a public figure, was traced via reverse image search to a different fire years earlier in a different location — despite being a completely real, unaltered photograph.

## Detecting AI-Generated Images
A non-expert reviewer can evaluate two accessible signals:
- **Resolution and quality**: high resolution combined with a clean image (low noise, no compression artifacts) is reassuring, because degrading resolution and adding artifacts is the easiest way to mask traces of manipulation. Low resolution or low quality should raise suspicion.
- **File metadata**: consistent metadata (date/time/location) alongside high resolution and quality is a good sign, though not conclusive on its own.

Deeper forensic analysis (e.g., shadow geometry) and paid "photo analysis" services are not reliable tools for a non-expert reviewer to rely on — deceptively confident third-party analysis services are a known source of false certainty in this area.

## Synthetic Video and Audio (Deepfakes)
The same generative techniques that produce fake still images extend to fabricating video (face and motion synthesis onto a real actor's performance) and audio (cloning a specific person's voice from samples). A documented case used a live actor filmed in real settings combined with an AI model trained on a public figure's footage to synthesize a convincing likeness for fabricated scenarios. As of this note's source, convincing full fabricated scenes (e.g., an entire fake event, not just a person's face) were harder to achieve than closeups, but the technology moves quickly enough that this constraint should not be relied on for long. Treat synthetic video/audio as subject to the same [verification technology arms race](verification-technology-arms-race.md) as image detection: no detection technique should be assumed to keep working indefinitely as generation techniques improve. Also don't overestimate the sophistication needed to deceive — plenty of successful disinformation uses no synthetic media at all, because audiences believe what they are already inclined to believe.

## Verification Action
Nothing replaces old-fashioned reporting: contacting witnesses or the original photographer/videographer and establishing scene facts independently, in addition to the technical checks above. Where available, check for a [content provenance authentication](content-provenance-authentication.md) signature established at capture, but treat its absence as inconclusive rather than as evidence of fabrication.

## See Also
- [SIFT Framework](sift-framework.md)
- [Content Provenance Authentication](content-provenance-authentication.md)
- [Verification Technology Arms Race](verification-technology-arms-race.md)
