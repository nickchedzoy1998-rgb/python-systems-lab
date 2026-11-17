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
- progressive hints
- code review
- debugging guidance
- design discussion
- test ideas

The objective is understanding and engineering fluency rather than
maximising implementation speed.

## Lessons and projects are different modes

The curriculum uses this sequence:

1. learn one mechanism;
2. practise it in a small task;
3. consolidate related skills;
4. pass a bounded readiness check;
5. build a complete program from a specification;
6. review the project critically.

Guided exercises and integration builds can produce useful application
code, but they do not count as project progress. A project begins only
after its required concepts have already been introduced and practised.
During a project, the learner chooses the structure, responsibilities and
tests instead of receiving a function-by-function tutorial.

## Repository structure

- `src/python_systems_lab/exercises/` contains focused concept practice.
- `src/python_systems_lab/guided_integrations/` contains instructor-supported
  combinations of previously introduced mechanisms.
- `examples/` contains manual inputs used to exercise guided programs.
- `tests/` mirrors the learning mode and package structure.
- `docs/practice/` contains supporting practice policies.

Independent project packages will be introduced only when their readiness
gate has been passed and the project is deliberately activated. The repository
does not create placeholder project code in advance.

## Curriculum practice rules

[SQL practice: capability with minimal overhead](docs/practice/SQL_PRACTICE.md)
adds diagnostic-led SQL practice within existing ten-minute sessions.
Project work and delayed reviews count; familiar material is not retaught
without evidence of a gap.

## Current focus

The `guided_integrations/csv_cli` package is a **guided integration build**
for professional Python, testing and process boundaries. It is not the first
major project.

After the remaining CLI/process-testing lessons and a short mixed readiness
check, **P01 · Reliable Data Pipeline** begins as a fresh bounded program
from a written specification. Later checkpoints add PostgreSQL and safe
historical replay only after those concepts have been taught and practised.

The [Engineering Lab tracker](https://engineering-lab-nick.nickchedzoypt797242.chatgpt.site/#Projects)
shows the learning blocks, readiness gates and independent project checkpoints.

See `NEXT.md` for the single current task.
