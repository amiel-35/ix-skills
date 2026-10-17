# Success criteria — software

Read this when the deliverable is an application, a module, a script or a data pipeline. It adds
to the method of the skill; it does not replace it. Software is where a loop covers the most: most
lines can be `mécanique`. That is also where gaming the tests is easiest, so the hidden part matters
more here, not less.

## 1. Test what the user gets, not what the code contains

- **Rendered output.** Content lines run on what is served or displayed — the HTML returned by the
  page, the generated PDF, the API response — for every variant, language and role, not on the
  source templates. A placeholder (« [à compléter] », TODO, lorem, an empty `{{ }}`) in a content
  file that a test never renders passes a green suite. Check: fetch every screen of every variant
  and search the output for the placeholder patterns and for empty required blocks.
- **Content the software carries.** When the module ships texts (a debrief script, consent
  wording, help pages, prompts), each one is a requirement: it exists, it is reachable from the
  screen that needs it, it has no gap, and its figures have a source. A screen that renders with an
  empty slot is a failure, not a pass.
- **Every path a step relies on exists**: the file, the route, the environment variable, the key.

## 2. Mechanical tests

- **Unit and integration** tests for each requirement, named after its E number so a failure says
  which requirement broke.
- **End-to-end** tests that go through the real sequence of screens with the real roles
  (participant, facilitator, admin), including going back, reloading, joining late, leaving early,
  changing an answer while the step is still open (counted once), opting out (no data created for
  that person), reopening the entry link in another browser, and switching networks mid-session
  (venue wifi to mobile data) without losing the session.
- **Rules enforced by the server**, not only by the interface: a closed step, an order between
  steps, an answer that must not change once given, a role's rights — each tested by calling the
  API directly, since a greyed-out button proves nothing.
- **What is hidden stays hidden**: content that must not be seen yet (the other variant, the
  answer, the reveal) is absent from every response the client receives — HTML, JSON, scripts,
  live messages — not only from the screen.
- **Distribution, not presence.** When the software draws, assigns or samples (random variants,
  balanced groups, rotation), test the distribution over many draws with a fixed seed and over many
  seeds: each arm within a stated tolerance of its share, balance within each stratum (per camp,
  per group, per session) when the brief needs it. « The draw exists » is not a test.
- **Properties, not only examples.** For logic with many inputs, test properties that must hold
  for any input (no participant sees both variants; every answer belongs to exactly one session;
  totals equal the sum of their parts), with generated inputs.
- **Test the tests.** A suite that still passes when the code is deliberately broken is weak.
  Mutation testing (introduce small changes to the code, check the suite fails) measures it; at
  minimum, check by hand that each critical test fails when its feature is removed.

## 3. Load

Derive the load from the brief, not from habit: the number of simultaneous users at the peak
moment (everyone answering the same question within the same minute), with a margin `[proposed]`
(×2). Measure the response time at a high percentile (p95) and the error rate under that load, on
an environment like production (same host size, same database, same external services or their
quotas). An external service with a rate limit or a cost per call (an LLM API) gets its own line:
what happens at the limit, and the cost of one full session.

## 4. Real devices and conditions — `terrain`

Some lines cannot be settled by an emulator: the real phones of the real audience (old Android,
iOS Safari, small screens, large text settings), the venue's network or a phone's mobile data, a QR
code read from the back of the room, a projector's resolution, dark mode and enlarged text. Write them as `terrain` lines with
who runs them and when (a dry run before the first real session).

**Degraded mode as a result.** For each dependency, write separately what must still hold when it
fails — the venue network cuts out, a participant has no device, the service itself is down — as a
result (« the session reaches its end with the service entirely unreachable »), not as « a plan
exists ». Check it by a dry run with the dependency removed (`terrain`) and by the presence of what
the fallback needs, printed or installed (`relecture`). Do not dictate the fallback itself.

## 5. Anonymity and erasure, checked down to the files

A promise of anonymity or erasure is a requirement on the **state of storage**, not on the screen.

- **Anonymity**: no table, log, analytics event, error report or backup links an answer to a
  person (name, email, IP, device id, login link). Check: read the schema, then search the
  database file, the logs and the error tracker for an identifying value used in a test session.
  Small cells re-identify: an aggregate shown with fewer than a stated number of people per cell
  `[proposed]` is a failure.
- **Recovery by subtraction.** Masking a small cell is not enough if it can be recomputed from
  what is shown elsewhere: a row or column total, another view of the same data, a before/after
  panel, two successive displays as one person joins or leaves. Check: from every number displayed
  in every view and state, try to solve for each masked cell (`mécanique` on a synthetic set). Hidden
  version: the judge combines views and moments the visible test does not combine.
- **Codes a person retypes** (a session code, a short recovery code): their strength is the limit
  on attempts and their lifetime, not their length; test the rate limit, the lockout and the expiry,
  and propose an entropy threshold only for codes nobody types.
- **Erasure**: plant a **canary** — a unique, searchable value — in a test session, run the
  deletion, then search the raw bytes of every place it may live: the database file and its
  side files, logs, caches, exports, backups, the hosting provider's snapshots, the third-party
  services that received it (an LLM provider's logs and retention, an email service). The deletion
  passes only when the canary is found nowhere, or where it remains is written down with its
  retention period.
- **SQLite specifically**: deleted rows stay in the file until overwritten. `PRAGMA secure_delete`
  overwrites deleted content with zeros (it is normally off; its `FAST` setting leaves traces on
  freelist pages), or a `VACUUM` after the deletion rewrites the file; check the `-wal` and
  `-journal` side files too, and full-text (FTS) shadow tables, which `secure_delete` does not scrub
  (sqlite.org, PRAGMA documentation). Check with a byte search for the canary, not by trusting the
  setting.
- **Who checks**: a developer on a copy of the files, with pseudonymised or synthetic data only.

## 6. A pass on states and actors

Go through the deliverable state by state — before the start, during, a step open, a step closed,
after the end, after deletion — and for each actor (participant, facilitator, someone who declined
to take part, a late joiner, an admin), write what that actor sees and can do. Typical lines:

- a questionnaire asked again does not display the earlier answers;
- someone who declines to take part still follows what the others see, without answering;
- after the end, and after deletion, the participant's screen says the session is over, and no
  earlier data can be recovered from it;
- a late joiner lands on the current step, not on a closed one;
- a reload in each state lands in the same state.

## 7. Keeping a loop honest

When an agent iterates until the suite is green, assume it will take the shortest path to green.
METR observed frontier models overwriting the scorer with a stub that reports success, reading the
expected answer from the grader's memory, overriding equality so comparisons always match, and
going on doing so when told not to cheat (« Recent frontier models are reward hacking », June
2025). Lines to add:

- the test files, fixtures, scoring scripts, test configuration and CI configuration are unchanged
  since the judge froze them (checksum held by the judge);
- no test is skipped, deleted, marked expected-to-fail or narrowed; the number of tests and the
  coverage are not lower than at the start;
- no special case for test inputs in the code (search for the test fixtures' literal values in the
  source);
- the hidden tests run in an environment the agent cannot read or write, and use other inputs than
  the visible ones for the same requirements;
- the agent's own statement that tests pass is never evidence: the judge reruns them.

## 8. Usual coverage

High: typically three quarters or more of the lines are `mécanique`. What stays out: content
quality and tone (`relecture`), real devices and the venue (`terrain`), and the outcome — whether
the session achieves its purpose with the real group (`terrain`, measured as a zone).
