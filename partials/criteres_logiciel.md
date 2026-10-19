# Success criteria — software

Read this when the deliverable is software: an application, a module, a script, an API, a data
pipeline. It adds to the method of the skill; it does not replace it. Part A applies to any
software. Part B applies only to applications that several people use at the same time in a live
session (a workshop, a vote, a quiz, a class): skip it otherwise, and do not import its load
profile, its venue or its roles into a deliverable that has none.

Software is where a loop covers the most: most lines can be `mécanique`. That is also where gaming
the tests is easiest, so the hidden part matters more here, not less.

# Part A — any software

## 1. Test what the user gets, not what the code contains

- **Rendered output.** Content lines run on what is served or produced — the page returned, the
  generated PDF, the API response, the file the pipeline writes — for every variant, language and
  role, not on the source templates. A placeholder (« [à compléter] », TODO, lorem, an empty
  `{{ }}`) in a content file that a test never renders passes a green suite. Check: produce every
  output of every variant and search it for the placeholder patterns and for empty required blocks.
- **Content the software carries.** When the software ships texts (consent wording, help pages,
  messages, prompts, a script someone reads aloud), each one is a requirement: it exists, it is
  reachable where it is needed, it has no gap, and its figures have a source.
- **Every path a step relies on exists**: the file, the route, the environment variable, the key.

## 2. Mechanical tests

- **Unit and integration** tests for each requirement, named after its E number so a failure says
  which requirement broke.
- **End-to-end** tests through the real sequence with the real roles, including going back,
  reloading, retrying, and doing the same action twice.
- **Rules enforced by the server**, not only by the interface: an order between steps, a state that
  forbids an action, a role's rights, one user's data closed to another — each tested by calling the
  API directly, since a greyed-out button proves nothing.
- **What is hidden stays hidden**: content a user must not see (another user's record, an answer
  not yet revealed, an internal field) is absent from every response the client receives — HTML,
  JSON, scripts, live messages — not only from the screen.
- **Distribution, not presence.** When the software draws, assigns or samples (random variants,
  balanced groups, rotation), test the distribution over many draws with a fixed seed and over many
  seeds: each arm within a stated tolerance of its share, and balance within each stratum when the
  brief needs it. « The draw exists » is not a test.
- **Properties, not only examples.** For logic with many inputs, test properties that must hold
  for any input (no double booking; every record belongs to exactly one owner; totals equal the sum
  of their parts), with generated inputs.
- **Test the tests.** A suite that still passes when the code is deliberately broken is weak.
  Mutation testing (introduce small changes to the code, check the suite fails) measures it; at
  minimum, check that each critical test fails when its feature is removed.
- **The label follows the instrument.** An automatic audit (accessibility, security scan, linter)
  is `mécanique`, and it settles only what it measures: « no automatic accessibility error » does not
  settle « usable with a screen reader », which needs its own `relecture` or `terrain` line.

## 3. Load and dependencies

- **Load from the brief, not from habit.** Derive the peak from what the brief implies (a booking
  page used by a few patients at once is not a vote of thirty people in the same minute), add a
  margin `[proposed]`, and measure response time at a high percentile and the error rate at that
  peak. A load test on an environment the brief does not provide is marked `[costly]` (skill,
  step 7).
- **External services** with a rate limit or a cost per call (an LLM API, an SMS gateway, a
  payment provider) get their own lines: what happens at the limit, the cost of a normal day, and
  what still works when the service is down — written as a result (« the booking is saved and the
  user is told the reminder may not be sent »), not as « a fallback exists ».

## 4. Personal data, anonymity and erasure, checked down to the files

A promise of anonymity, confidentiality or erasure is a requirement on the **state of storage**, not
on the screen.

- **No link to a person where none is promised**: no table, log, analytics event, error report or
  backup links a record to a person (name, email, IP, device id, login link) beyond what the
  brief allows. Check: read the schema, then search the database file, the logs and the error
  tracker for an identifying value used in a test run.
- **Aggregates** (when the software displays counts or averages by group): small cells re-identify
  — an aggregate shown with fewer than a stated number of people per cell `[proposed]` is a failure;
  and masking a small cell is not enough if it can be **recomputed by subtraction** from what is
  shown elsewhere — a row or column total, another view, a before/after panel, two successive
  displays as one person joins or leaves. Check: from every number displayed in every view and
  state, try to solve for each masked cell (`mécanique` on a synthetic set). Hidden version: the
  judge combines views and moments the visible test does not combine.
- **Codes a person retypes** (a session code, a short recovery code): their strength is the limit
  on attempts and their lifetime, not their length; test the rate limit, the lockout and the expiry,
  and propose an entropy threshold only for codes nobody types.
- **Erasure**: plant a **canary** — a unique, searchable value — in a test run, run the deletion,
  then search the raw bytes of every place it may live: the database file and its side files, logs,
  caches, exports, backups, the hosting provider's snapshots, the third-party services that received
  it (an LLM provider's logs and retention, an email or SMS service). The deletion passes only when
  the canary is found nowhere, or where it remains is written down with its retention period.
- **SQLite specifically**: deleted rows stay in the file until overwritten. `PRAGMA secure_delete`
  overwrites deleted content with zeros (it is normally off; its `FAST` setting leaves traces on
  freelist pages), or a `VACUUM` after the deletion rewrites the file; check the `-wal` and
  `-journal` side files too, and full-text (FTS) shadow tables, which `secure_delete` does not scrub
  (sqlite.org, PRAGMA documentation). Check with a byte search for the canary, not by trusting the
  setting.
- **A documented choice is not a compliant one**: « the hosting status for health data is written
  down » passes when the document says « not certified ». Test the requirement (the data is hosted
  where the rules require), not the existence of the paragraph.
- **Who checks**: a developer other than the author, on a copy of the files, with pseudonymised or
  synthetic data only.

## 5. Keeping a loop honest

When an agent iterates until the suite is green, assume it will take the shortest path to green.
METR observed frontier models overwriting the scorer with a stub that reports success, reading the
expected answer from the grader's memory, overriding equality so comparisons always match, and
going on doing so when told not to cheat (« Recent frontier models are reward hacking », June
2025). Lines to add:

- **the instrument is the judge's**: the scripts of the visible `mécanique` lines are written by the
  judge, or written by the agent and reviewed line by line by the judge, and frozen **before the
  first round**; a line whose script the author wrote and the judge has not reviewed counts as
  `relecture`, not `mécanique` (an empty assertion or a mock that always answers OK is « unchanged »
  and green);
- the frozen suite is the baseline: test files, fixtures, scoring scripts, test configuration and
  CI configuration unchanged since the freeze (checksum held by the judge); no test skipped, deleted,
  marked expected-to-fail or narrowed; the number of tests and the coverage not lower than **the
  frozen suite's** — not « than at the start », which is zero for new software;
- no special case for test inputs in the code (search for the test fixtures' literal values in the
  source);
- the hidden tests run in an environment the agent cannot read or write, and use other inputs than
  the visible ones for the same requirements;
- the agent's own statement that tests pass is never evidence: a judge who executes reruns them;
  an evaluator who only reads the conversation sees the raw outputs (skill, « Stopping criterion »).

## 6. Usual coverage

High: typically three quarters or more of the lines are `mécanique`. What stays out: content
quality and tone (`relecture`), real devices and real use (`terrain`), and the outcome — whether the
software is adopted and does its job (`terrain`, measured as a zone).

# Part B — live multi-user sessions

Read this part only when several people use the software at the same time in a live session.

## 7. Session flow

End-to-end tests with the session's real roles (participant, facilitator, admin), including
joining late, leaving early, changing an answer while a step is still open (counted once), opting
out (no data created for that person), reopening the entry link in another browser, and switching
networks mid-session (venue wifi to mobile data) without losing the session.

## 8. Load at the peak moment

The peak is the moment everyone acts at once (all participants answering the same question within
the same minute), with a margin `[proposed]`, on an environment like the one used in the session.

## 9. Real devices and the venue — `terrain`

Some lines cannot be settled by an emulator: the real phones of the real audience (old Android,
iOS Safari, small screens, large text, dark mode), the venue's network or a phone's mobile data, a
QR code read from the back of the room, a projector's resolution. Write them as `terrain` lines with
who runs them and when (a dry run before the first real session).

**Degraded mode as a result.** For each dependency, write separately what must still hold when it
fails — the venue network cuts out, a participant has no device, the service itself is down — as a
result (« the session reaches its end with the service entirely unreachable »), not as « a plan
exists ». Check it by a dry run with the dependency removed (`terrain`) and by the presence of what
the fallback needs, printed or installed (`relecture`). Do not dictate the fallback itself.

## 10. A pass on states and actors

Go through the session state by state — before the start, during, a step open, a step closed, after
the end, after deletion — and for each actor (participant, facilitator, someone who declined to take
part, a late joiner, an admin), write what that actor sees and can do. Typical lines:

- a questionnaire asked again does not display the earlier answers;
- someone who declines to take part still follows what the others see, without answering;
- after the end, and after deletion, the participant's screen says the session is over, and no
  earlier data can be recovered from it;
- a late joiner lands on the current step, not on a closed one;
- a reload in each state lands in the same state.
