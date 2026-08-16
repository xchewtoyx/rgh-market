# Wiki authoring rules

These rules govern every domain wiki bundle in this repository. Read this
document in full before creating or editing any note in a domain bundle.

## Purpose

Each domain folder is a zettelkasten-style wiki that serves as external memory
for LLM agents doing work in that domain. The wiki's only reader is future agent
instances retrieving context to advance a task, not humans browsing for
pleasure. Every design choice below serves one goal: **progressive disclosure**
— an agent working a task should be able to load exactly the notes it needs, one
link-hop at a time, and never have irrelevant material forced into its context
because a note was scoped too broadly.

Your domain charter (in your curator agent definition) states what the wiki is
_for_. Stay scoped to what's useful for that purpose. Omit content that doesn't
serve an agent trying to act in the domain, even if it appears in the source
text.

## Input

Source material lives under `fleeting/`; treat anything there as raw/unprocessed
literature notes distilled from reference texts — never as finished wiki
content. Fleeting notes have not been atomized.

## Output location — layout

Write permanent notes as individual Markdown files directly in your domain's
folder, forming a single OKF (Open Knowledge Format) bundle. Keep the bundle
flat: every concept file lives directly in the domain folder, no subdirectories.
Path is not taxonomy — do not encode categorization through folder structure;
that's exactly the kind of imposed structure the linking rule below exists to
avoid.

Do not introduce `index.md`, `log.md`, a `README.md`, or a `references/`
subdirectory inside a bundle — some of these are legal OKF constructs, but
they're hub/entry-point mechanisms, and this wiki's discovery model is
search-and-follow-links, not browse-an-index. Don't add folders for any purpose.

Filename = a descriptive kebab-case slug of the concept (e.g.
`tail-latency-amplification.md`). Per OKF, the Concept ID is the file path with
`.md` removed — the filename _is_ the identifier; there's no separate ID scheme.
Agents will locate notes primarily by grep/search over meaningful names and
titles, so make slugs precise.

## The atomicity rule

Each note captures exactly one concept, claim, or technique — small enough to
state precisely, large enough to be useful on its own. If you notice yourself
writing "and" between two ideas that could stand alone, split them. Overly broad
notes are the main way progressive disclosure breaks: if a note covers three
related ideas, an agent that only needed one is forced to load all three. A note
should be understandable on its own once the notes it links back to (or that
link to it) have been read — not by loading the whole wiki.

Before writing a new note, search the bundle for an existing note covering the
same concept. If one exists, extend/refine it in place rather than creating a
near-duplicate. Concepts recur across source texts — converge on one canonical
note per concept, citing whichever text(s) actually contributed.

## Frontmatter (YAML, OKF-conformant)

Every note starts with a YAML frontmatter block:

```yaml
---
type: concept
title: Tail Latency Amplification
description: >
  One sentence stating what this concept is and why it matters.
---
```

- `type` is mandatory (OKF's only always-required field). Default to `concept`
  for everything. Only introduce a different type value if there's a genuine
  taxonomy difference — a category of note that behaves or gets consumed
  differently, not just a different topic area. Don't invent types to pre-sort
  concepts by book, theme, or maturity; that's hub-building through frontmatter.
- `title` is mandatory: a precise human-readable name.
- `description` is mandatory: exactly one sentence, used the way OKF intends — a
  search/index snippet — not a summary of the whole note.
- Every other field needs justification before you add it:
  - `sources` is usually justified here: these notes derive from specific books,
    and tracing a claim back to its source text helps resolve disagreements
    between texts later. Use it when a note draws on identifiable source
    material:

    ```yaml
    sources:
      - title: Observability Engineering
        resource:
          "Observability Engineering (Majors, Fong-Jones, Miranda), ch. 3"
    ```

    (`resource` is required per entry; since these are books rather than URLs,
    use a citation string as the locator.)

  - OKF also defines `generated`, `verified`, `status`, and `stale_after`
    (provenance/trust/lifecycle fields). Skip these by default — this wiki is
    bootstrapped from static texts, not a live pipeline whose edits need
    verification tracking. Only add one of these fields if a concrete
    maintenance need arises (e.g. a note is found to contradict its source and
    needs a `status: draft` flag while it's reworked). Don't add them
    speculatively — they cost context on every load for no benefit yet.
  - Skip `tags`. Cross-cutting categorization is exactly the kind of structure
    that should emerge from the link graph, not be declared in frontmatter.

## Linking rule

Link concepts inline using CommonMark links, e.g.
`[percentile selection](percentile-selection.md)`, at the exact point in the
prose where that related concept is invoked — never as a "See also" list at the
end. Links stay inside the bundle: link only to other notes in the same domain
folder. Never link across domain bundles — each bundle is self-contained.
Citations to source books go in `sources:` frontmatter, not inline links.

Choose outbound links by asking: if an agent has just understood this note and
wants to advance its actual task, what is the next concept it would need to
load? Link forward toward utility and application, not backward toward citation
or taxonomy. This is the progressive-disclosure mechanism: an agent starts from
one relevant note and pulls in only the next note it actually needs, hop by hop,
rather than one broad note trying to cover everything up front. It's fine for a
note to have zero or several outbound links — don't force links to hit a quota.

## No hub topics

Do not create index pages, "map of content" notes, category/overview pages, or
any note that exists to link out to everything. Structure must emerge from the
organic accumulation of inline links between atomic notes. If the graph "feels
disconnected," add more precise inline links between existing notes — don't add
an organizing layer on top.

## Process

1. Read the input fleeting notes fully before writing anything.
2. Identify the distinct atomic concepts present that fall inside your domain
   charter (there will usually be many more concepts than input notes —
   decompose aggressively).
3. For each concept: search the existing bundle for overlap, then either extend
   an existing note or write a new one.
4. As you write each note, place inline links to other concepts it should
   connect to — both linking out to concepts that should exist (write a stub
   note for them in the same pass if reasonable) and, where a note you already
   wrote is genuinely the "next concept" from an earlier note's perspective,
   going back to add that link.
5. Work incrementally, one concept at a time, rather than batch-drafting many
   notes and linking them at the end — this keeps linking decisions honest, made
   with the actual target note in view.
6. Stay scoped to your domain charter. A fleeting note will often contain
   material for several domains — take only what belongs to yours and trust the
   other curators to take theirs.
