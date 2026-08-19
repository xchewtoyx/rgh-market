---
name: progress
description: Show per-domain curation progress (pending fleeting notes).
argument-hint: "[--pending-only]"
---

# Curation progress overview

Print how far each domain ledger is through the fleeting backlog so the next
useful `/curate` target is obvious. When a domain has ratings-cache entries for
still-pending notes, also show the highest cached confidence (`MAX_P`) and how
many pending scored notes are at or above `0.7` (`P>=0.7`) — useful for picking
a `/curate --focused` target without opening note bodies.

## Procedure

1. From the repo root, run the path-only helper (do not open fleeting note
   bodies):

   ```sh
   sh scripts/curation-progress.sh
   ```

   Optional: `sh scripts/curation-progress.sh --pending-only` (or pass
   `--pending-only` / `-p` to this skill) to list only domains that still have
   unreviewed notes.

2. Show the command output to the user unchanged. Domains with pending work are
   marked `*`. `MAX_P` is the highest cached confidence among pending notes for
   that domain (`-` when none are scored yet). `P>=0.7` counts pending notes
   with cached confidence at or above `0.7`.

3. Do not read fleeting note contents, do not open ledger bodies beyond what the
   script already summarizes, and do not start curation unless the user asks.
   Suggest `/curate <slug> --limit N` when they want a next slice, or
   `/curate --focused <slug>` when `P>=0.7` is non-zero.

## Rules

- Path-and-ledger bookkeeping only — never open fleeting note bodies.
- Do not invent progress numbers; always run the script.
