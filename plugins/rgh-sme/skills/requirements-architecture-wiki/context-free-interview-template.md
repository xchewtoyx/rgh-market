---
type: concept
title: Context-Free Interview Template
description: >
  A fixed sequence of interview question categories — user profile,
  environment, problems, proposed-solution reaction, other requirements,
  wrap-up — keeps a requirements interview from being shaped by whatever
  the interviewer happened to think to ask.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), Appendix A"
---

A "context-free" interview is structured so its question categories work
regardless of the specific domain being investigated, reducing the risk
that [interviewer bias](requirements-elicitation-techniques.md) — the
interviewer's own preconceptions leaking into which questions get asked —
shapes what gets discovered. The recurring structure:

- **Customer/user profile** — who the interviewee is and what standing
  they have to answer for the group they represent.
- **User environment** — how many people are involved in the task and
  whether that's changing, how long a task cycle takes and how time is
  spent within it, any unusual environmental constraints, what platforms
  and other applications are already in use and need to be integrated
  with, and expectations around usability and training time.
- **Problem exploration** — for each candidate problem: is this a real
  problem, why does it happen, how is it currently solved, how would the
  interviewee prefer to solve it, and how does it rank against the other
  problems raised?
- **Reaction to a proposed solution** (if one exists yet) — summarize
  candidate capabilities and prompt with "what if you could...?" rather
  than only asking about the problem in the abstract.
- **Other requirements** — a deliberate catch-all for legal, regulatory,
  environmental, or standards-driven requirements that don't fit the
  categories above, plus an open "anything else we should know?" prompt.
- **Wrap-up** — anything the interviewer should have asked but didn't,
  permission for follow-up contact, and willingness to participate in a
  later requirements review.

The categories are deliberately ordered from broad context toward specific
requirements, so a requirement surfaced late in the interview is already
anchored to a profiled user and a described environment, rather than
floating free of the context needed to judge whether it generalizes to
other users or is one interviewee's idiosyncratic need. See [story-based
elicitation questions](story-based-elicitation-questions.md) for a
technique that sharpens how the problem-exploration questions themselves
get asked.
