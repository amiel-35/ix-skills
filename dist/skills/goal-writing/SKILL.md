---
name: goal-writing
description: "Writes the goal of an agent that works alone, in autonomy, from a closed scoping and a set of settings \u2014 intent, deliverables (each with its format skill received as an input), constraints and prohibitions, authorisations, a stopping condition that points to an acceptance script without knowing its content, a turn ceiling. Triggers on \"write the goal for this closed scoping\", \"turn this scoping into an instruction for an autonomous agent\", \"write the mission this agent will hold to the end\". The goal holds in 1,200 words at most, its details going into an annex; if its core exceeds that limit, it returns \u00ab to split \u00bb with a proposed split instead of a goal. Does not write the success criteria or the acceptance script, does not choose any format skill, and does not describe any tool's command \u2014 it describes the content of a goal."
---
# Role

You write the goal of an agent that will work alone, for many turns, without anyone to ask. The goal is the only document that agent reads to know what it must achieve, what it may and may not do, and when it stops. You write its content; you do not describe how any particular tool launches it.

# Absolute rule

- Write only what the closed scoping and the settings support. When the scoping does not say something the goal needs, do not invent the decision: take the option that commits the least (fewest files touched, nothing irreversible), mark it « to confirm », and list it apart (see « Writer's notes »).
- The goal never contains the acceptance criteria, the content of the acceptance script, or any threshold other than the turn ceiling. You do not receive them and you do not write for them.
- The stopping condition points to the acceptance script **without knowing what it checks**.
- Every format skill named in the goal comes from the input. You never choose one, add one, or drop one. When the list says how a deliverable is matched to one of its lines (for example by its subject), follow that rule; when it says nothing, a deliverable with no line has no format skill.
- **The goal holds in 1,200 words at most.** This is a hard limit, not a target (see « Length and splitting »). Above it, you do not compress: you return « to split ».
- The agent that reads the goal reads nothing else: the goal names, by path or by slot, every document the agent must read (the closed scoping, any procedure or reference the scoping tells it to follow), and says which places it may read and write.

# Length and splitting

A goal that is too long is a signal, and it can mean two different things. Tell them apart before you hand anything back.

1. **Write the core first.** The core is the intent, the deliverables (what, reader, where, format skill), the major prohibitions, the authorisations, the stopping condition, the turn ceiling, the conduct at the ceiling and what to trace, each in its shortest exact form.
2. **Move the details into an annex.** Explanations, interfaces, contracts, long lists of paths, and detailed conduct that the core only needs to point to go into an **annex of the goal**: a separate document, named in the goal by path or by slot, that the agent reads before it starts and that is frozen with the rest. The annex adds no decision and no deliverable; it details what the core already says. The core names the annex in « Values fixed later » and in the list of documents to read.
3. **Measure the core** — the goal without its annex and without the writer's notes — in words.
   - At most 1,200 words: hand back the goal and its annex.
   - More than 1,200 words: **do not compress, do not cut a rule to fit.** The core is long because the subject is too large for one goal. Write no goal. Return « to split »: the word count of the core, and a proposed split of the closed scoping into parts, each a group of deliverables that can be produced and accepted on its own, with the reason for each cut. The split goes back to the scoping, which decides it; you do not decide it.
4. A correction asked after a review (an ambiguity, a missing rule) goes into the annex when it is a detail, and into the core only when it changes what the agent must do. If the core then exceeds the limit, the same rule applies: return « to split ».

# Expected inputs

| Input | Required | What it is |
|---|---|---|
| Closed scoping | yes | The document that records the decisions, constraints with their rationale, scope and out of scope, deliverables with their reader, accepted risks. The goal is derived from it and from nothing else about the subject |
| Settings | yes | The values the goal must carry: the turn ceiling, the model of each role, the limits on sub-agents, the suites offered when a ceiling is reached, whether the acceptance script and its grid are frozen |
| Format skills per deliverable | yes | For each deliverable, the skill that fixes its form and the instruction given to it; a deliverable absent from this list has no format skill |
| Names of values fixed later | no | Names of the values that will only be known once the acceptance script exists (its path, its fingerprints file, the folder of the pieces, the branch) |

**Not inputs.** The success criteria, the grid they come from, and anything sealed from the producer are not inputs. If the message supplies one of them, do not use it, and say in the writer's notes that you ignored it.

# Method

1. **Intent.** Take the intent from the closed scoping and state it as a goal — what must become true — not as an artefact to produce. If the scoping says what is *not* the aim (for example, a better deliverable), carry that sentence over.
2. **Deliverables.** For each deliverable of the scoping, write: what it is, its reader, where it is written, and **its format skill exactly as received** with the instruction given to it. A deliverable with no format skill in the input says « no format skill ». Documentation is a deliverable like the others. Where the scoping marks a deliverable as to be produced by a sub-agent applying a skill, say so; the writing of the deliverable itself stays on the main thread (see authorisations).
3. **Constraints and prohibitions.** List each constraint of the scoping with its rationale, in a line. Add the prohibitions the scoping states, and always these: do not modify the acceptance script, the grid it comes from, or anything frozen with them, and do not work around them; do not read or search for anything the scoping says is sealed; do not step outside the places the scoping assigns for reading and writing; do not do what the scoping puts out of scope.
4. **Authorisations.** State what the agent may delegate: sub-agents to read, to give an expert opinion, or to review. Every call to a sub-agent carries an explicit model, chosen from the settings by role (mechanical bulk work, reading and bounded expertise, verification). The nesting and parallel limits are those of the settings. The deliverables are written on the main thread only; no sub-agent writes into a deliverable. Name nothing the settings do not grant.
5. **Stopping condition.** The work is done when the acceptance script, named by its slot, exits with code 0 — or when the turn ceiling is reached, whichever comes first. Do not say what the script checks, number its lines, quote a command from it, or give any expected result. Add the rules that make a result count: the agent shows the exact command and the full raw output of the script; the agent's own report that everything passes does not count; no check of the script is skipped, removed, commented out or weakened, and no variable is changed; the number of checks never goes down from one run to the next. If the settings freeze the script and the grid, add that the agent checks the integrity of the frozen files at the start of every turn, and stops at the first mismatch. Say plainly that a zero exit code is not the acceptance of the work: the review that follows plays what the script does not cover.
6. **Turn ceiling.** Write the value of the settings, and what a turn is: one iteration of the autonomous loop, which ends when the agent hands control back. It is neither a message nor a tool call. Say that the agent should work at length within a turn and hand back only at a useful stopping point.
7. **When the ceiling is reached.** The agent tries nothing more and works around nothing. It writes down the failure — the last result of the script, what is still failing, what has been delivered — and hands control back. It lists the suites the settings offer for that ceiling, without choosing one. Corrections that follow the review are counted apart from the turn ceiling; say so only if the scoping or the settings do.
8. **What to trace.** Say what the agent records, in the trace named by its slot: the start of the session; at each run of the script, the turn number, the exit code and the failures; each sub-agent call with its role and model; each skill used with its version and a fingerprint of its text; each point marked « to confirm »; each path outside the allowed places that came up and was not opened.
9. **Values fixed later.** Wherever a value is not known yet (the path of the script, the fingerprints file, the folder of the pieces, the branch, an identifier), write a named slot between angle brackets, for example `<ACCEPTANCE_SCRIPT>`. Put at the top of the goal the rule that if any slot is still unfilled when the agent starts, it produces nothing, writes the reason in its final message and hands control back. Three slots always exist, under the names the input gives them or, failing that, `<ACCEPTANCE_SCRIPT>` (the script of the stopping condition), `<FROZEN_FILES_CHECK>` (the integrity check of the frozen files, when the settings freeze anything) and `<TRACE_FILE>` (where the agent records what step 8 lists). Any other slot name is used only for a value the input told you to expect; otherwise it is a gap (see the Absolute rule).

# Constraints

- Make the goal consistent with itself. One term names one object: when the inputs use a word for two things (for example « grid » for a grid that judges a scoping and for the grid of success criteria), define each once and keep a distinct name for each. No instruction contradicts another (a rule on where to write, for example, leaves room for the places the slots will name).
- Every check you ask the agent to make states what to do for each outcome (« check whether X exists » says what to do if it does, and if it does not).
- Say what « handing control back » means each time you use it: end of a turn, to be relaunched, or final stop with a written reason. An agent that works alone has nobody to ask: a blocker is written down and ends the work with a final stop.
- Name each sub-agent model by its key in the settings, not by a family of tasks.
- Write a slot's definition without relying on its angle brackets: the unfilled test is that the angle-bracket form still appears outside the section « Values fixed later ».
- Mark every narrowest-option choice (a gap) « to confirm » in the goal at the place where it applies, as well as in the writer's notes. A gap about committing, delivering or publishing is settled in the goal by the least irreversible option: do not commit or publish unless the scoping says to.
- Say what the agent may read among the frozen files and fixtures (the acceptance script, the grid, the fixtures): reading them is allowed unless the scoping says otherwise; modifying them never is.
- Describe the content of a goal, not a tool. Do not give the syntax of a command, an option, a hook or a file format of any particular tool. If an example helps, give it as an example.
- Do not copy a criterion, a threshold or a check. The ceiling of turns is the only number you write for the stopping condition, and you take it from the settings.
- Do not write to be graded: the goal serves the intent, not a particular grid.
- Do not weaken a prohibition of the scoping or of the settings.
- Write the goal in the language of the closed scoping.
- Do not add a deliverable, a prohibition or an authorisation the inputs do not support.

# Expected output format

```markdown
---
status: draft
skill: goal-writing
---

# Goal — {subject}

## Values fixed later
{the rule on unfilled slots; the list of slots}

## Intent
## Deliverables
{one entry per deliverable: what, reader, where, format skill and instruction}
## Constraints and prohibitions
## Authorisations
## Stopping condition
## Turn ceiling
## When the ceiling is reached
## What to trace

---
## Annex of the goal (separate document, named in the goal)
{the details the core points to; no new decision or deliverable}

---
## Writer's notes (not part of the goal)
- word count of the core (the limit is 1,200)
- gaps in the scoping, each with the narrowest option taken, marked « to confirm »
- inputs ignored (criteria, grid, sealed material), if any
- slots used and where each is expected to be filled
```

When the core exceeds the limit, the output is instead:

```markdown
---
status: to split
skill: goal-writing
---

# To split — {subject}

Core of the goal: {n} words (limit 1,200). No goal written.

## Proposed split
| Part | Deliverables | Accepted on its own because |
|---|---|---|

## What goes back to the scoping
{the decision the scoping must take before a goal can be written for each part}
```

# Definition of done

- The core of the goal holds in 1,200 words or fewer, and its details are in an annex it names; or no goal is written and the output is « to split », with the word count of the core and a proposed split of the scoping, each part with its reason.

- The goal has an intent, deliverables each with its reader and its format skill (or the statement that it has none), constraints and prohibitions, authorisations, a stopping condition, and a turn ceiling.
- The stopping condition names the acceptance script by its slot, says nothing of what it checks, and says that a report from the agent does not count.
- The prohibition on modifying the acceptance script and the grid is written.
- Every call to a sub-agent is authorised with an explicit model, and the writing of deliverables stays on the main thread.
- The turn ceiling equals the value of the settings.
- No criterion, check or threshold other than the ceiling is copied into the goal.
- Every gap is listed apart with the narrowest option taken.
- A reader who knows nothing of the subject can start the work from the goal alone.
