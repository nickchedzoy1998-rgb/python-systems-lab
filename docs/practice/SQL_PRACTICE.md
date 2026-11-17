# SQL practice: capability with minimal overhead

Approved: 5 November 2026

This addendum implements Nick's request for independent data-engineering SQL
capability with minimal unnecessary study time. It supplements the existing
curriculum, not another course or a replacement roadmap. The Python/backend/
infrastructure direction, prerequisites and current task remain intact.

## Operating rules

1. **One task, ten minutes, no extra homework.** Initially use roughly one SQL
   task per five completed sessions when SQL is not already being used. This is
   an adjustable starting point, not a fixed 20–25% quota or additional time.
2. **Count existing work.** SQL in a project, diagnostic or checkpoint counts.
   A delayed independent attempt can also fulfil an existing review slot. Do
   not add a drill when project work already provides equivalent practice.
   Preserve reviews of other subjects; new SQL teaching is not automatically
   a retrieval review.
3. **Diagnose before teaching.** Nick already uses SQL. Start with one unfamiliar
   question, without naming the solution technique. Ask for output grain and
   approach, a learner-written query, an output check and one edge-case
   explanation. Add a second diagnostic only when it changes the teaching plan.
   Do not infer mastery from work experience or repeat SELECT/JOIN instruction
   when the skill has been demonstrated.
4. **Teach only the gap.** Independent success skips introductory teaching for
   that skill, not a delayed check. A conceptual error gets a small explanation,
   a focused attempt and a different later test, not a repeated whole section.
   Syntax lookup is allowed after the intended operation is explained; concept
   hints are recorded. Typing speed and API spelling are not progression gates.
5. **Reuse context, vary the problem.** Reuse one small synthetic transactions,
   refunds and customer-history dataset, then the actual project's tables.
   Occasionally change the schema or question to check transfer. Prefer an old
   skill plus at most one new concept. Never use private client data.
6. **No new administration.** Use the existing practice record and review
   schedule. Missed sessions create no catch-up debt. Keep exactly one active
   NEXT.md task; do not replace the current Python task with this addendum.

A session can use roughly two minutes to reason, six to implement and two to
check. This is a budget, not a timed exam. Split larger work across sessions.
The instructor may supply schema, seed data and expected results; the learner
writes the core query and meaningful checks. Reuse an available SQL environment;
do not require new Docker/cloud/dbt/Spark setup for an initial query exercise.
Use PostgreSQL for engine-specific work at the appropriate project stage.
Code-only reasoning can be assessed, but execution remains unverified until run.

## What practice must eventually demonstrate

These are existing curriculum capabilities, not six additional lessons or exams.
Assess them in small slices and through projects; unassessed stays unassessed.

| Capability | Evidence | Placement |
| --- | --- | --- |
| Query correctness | Correct grain, joins, CTEs/subqueries, aggregates, null/date handling and existence checks; no lost or multiplied records. | Diagnose now; skip familiar introductory syntax. |
| Windows and deduplication | Appropriate ranking, LAG/LEAD and frames; latest-record selection with an explicit tie-breaker. | After grain and ordering concepts. |
| Relational design and safe writes | Suitable keys, constraints and types; parameterised application SQL; tested commit/rollback boundaries. | PostgreSQL/application-persistence stage. |
| Incremental transformations and history | Safe upserts/replay, late corrections, as-of joins and appropriate operational versus fact/dimension models. | After keys, transactions and modelling; extend the pipeline. |
| Verification and reconciliation | Checks for uniqueness, missing/excess rows, totals and edge cases; detect wrong answers even when queries execute. | Start with one meaningful check per relevant task. |
| Performance and concurrency | Measured plan/index changes on representative data, write/storage trade-offs, and isolation/locking experiments. | After real PostgreSQL use; transaction fundamentals before concurrency. |

Later dbt, warehouse and Spark SQL tasks reuse these capabilities rather than
restart SQL teaching. Procedural SQL, recursive queries and specialist engine
features enter when a project or role justifies them, not as early detours.

## Retention and progression

Use existing outcomes: **Independent**, **With a hint**, **Needs another
explanation**. One independent success plus another meaningfully different
independent use after a gap is the minimum basis for reducing routine practice
of that specific skill. It is not permanent mastery or proof that all SQL is
covered. Keep occasional mixed checks as projects grow.

Keep the existing flexible review intervals (about two days, one week, three
weeks and six weeks), adapted to actual sessions and results. Project reuse can
supply a delayed check. Strong performance means fewer standalone drills; a
failure means a targeted repair. Record only capability, date, task/commit,
assistance level and gap/next revisit in the existing record, or a short session
note when the tracker is unavailable. A commit alone does not prove recall.

Section checkpoints replace a normal task and combine two or three taught
skills. Repair the failed part and retest it in a new context; do not routinely
repeat the whole checkpoint. Do not schedule duplicate revision queues.

## First SQL slot — diagnostic, not the current active task

Calculate net transaction revenue per customer in a specified date range from
transactions and refunds. Transactions have unique IDs, customer IDs, timestamps
and amounts. Refunds have unique IDs, transaction IDs and amounts. A transaction
may have no refunds or several partial refunds. Use one currency. Select
transactions in a half-open timestamp interval, then subtract all supplied
refunds for those transactions regardless of refund date. Return one row per
customer with a selected transaction, including fully refunded transactions.

The instructor supplies a tiny runnable fixture and expected results including
no refunds, multiple refunds and exact date boundaries. Do not supply a solution
query or name the technique. Ask Nick to state grain, write/run the query and
explain its correctness for those cases. Schedule this at the next suitable SQL
slot after resolving the current task; no work is required now.

## Publication status

Stored in the learning repository and linked from its README. The separate
Engineering Lab dashboard was not edited or republished in this change.
Existing progress, practice history, source code, tests and NEXT.md are unchanged.
