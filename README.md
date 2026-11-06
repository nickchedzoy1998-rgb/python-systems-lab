# Python Systems Lab

A deliberate-practice repository for developing professional Python,
backend engineering, and systems skills.

## Long-term direction

This repository will evolve from small Python engineering exercises into
a durable asynchronous job-processing service using:

- Python
- FastAPI
- PostgreSQL
- asynchronous/concurrent workers
- testing
- Docker
- observability
- load and failure testing

## Learning approach

Core implementation is written manually.

AI is used primarily for:
- teaching
- hints
- code review
- debugging guidance
- design discussion
- test ideas

The objective is understanding and engineering fluency rather than
maximising implementation speed.

## Curriculum practice rules

[SQL practice: capability with minimal overhead](docs/SQL_PRACTICE.md)
adds diagnostic-led SQL practice within existing ten-minute sessions.
Project work and delayed reviews count; familiar material is not retaught
without evidence of a gap. This supplements the broader curriculum and
does not replace the current task.

## Current focus

The first major project is the Reliable Data Pipeline. Start with a tested local ingestion command, then add atomic PostgreSQL batches and safe replay. A separate job API can reuse the database setup while owning its own job and attempt state. The [Engineering Lab project roadmap](https://engineering-lab-nick.nickchedzoypt797242.chatgpt.site/#Projects) shows how analytics and operations build on these components.

See `NEXT.md`.
