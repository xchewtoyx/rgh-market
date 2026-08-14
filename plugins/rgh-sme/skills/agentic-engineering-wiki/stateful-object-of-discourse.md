---
type: concept
title: Stateful Object of Discourse
description: >
  Give a conversation a persistent object that gets edited in place across
  turns, instead of having the model re-emit a fresh copy into the transcript
  every time.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 11"
---

A recurring UX problem in ordinary chat interfaces: ask the model to write,
then modify, a piece of content (a function, a document, a diagram), and the
default behavior is to rewrite it from scratch on every turn — producing N
separate objects scattered through the conversation instead of one object
whose state evolves. This makes it hard to say which version you mean, and
hard to do sustained collaborative work rather than just conversing. The
analogy is pair programming: the files under edit are the actual objects of
discourse, changed and discussed in place, not re-typed in full on every
exchange.

Anthropic's Artifacts feature is a step toward this pattern: a generated
object (code, an SVG, a document) persists statefully in its own pane outside
the conversation transcript, and an edit updates the object in place rather
than re-emitting it into the chat log. Turning [tool
use](tool-call-transparency-ui.md) into conversational agency was giving an
assistant the ability to act in the world; giving a conversation a stateful
object of discourse is the complementary move — letting a conversation be
*about* a persistent thing rather than only a sequence of exchanges.

This UX pattern still has real limitations worth knowing about when designing
one, because none of them are automatically solved by adopting the pattern
itself:

- **The persistence is a UI-level trick, not a prompt-engineering-level
  one**, if the underlying implementation still regenerates the entire object
  from scratch on every edit and the UI just happens to route the result into
  the same pane. This doesn't scale gracefully to long documents, where a full
  rewrite for a small edit is wasteful and risks introducing unrelated
  changes.
- **Supporting only one object at a time** is a common simplification, but it
  means a topic switch gets treated as a new version of the same object
  rather than a genuinely separate one, and there's no shorthand — in the UI
  or in the prompt itself — for referring to a specific one among several.
- **No direct user-editing of the object** means a user who spots a small,
  obviously-fixable problem has to ask the assistant to retype the whole
  thing rather than edit it directly and let the model pick up the diff on
  the next turn.

Leaning into a conversational interface is intuitive, but building something
"bare-bones" here easily ends up a gimmicky distraction rather than a
genuinely useful pattern — it takes real design investment to get right. A
tight conversational loop around a stateful object also helps counter the
model straying off course, the same problem [ReAct](react-loop.md) and other
tight observe-act loops address, by letting a user catch and correct a
problem as soon as it appears rather than after several more turns compound
it.
