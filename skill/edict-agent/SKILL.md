---
name: edict-agent
description: Use when Codex is facing a large, ambiguous, cross-module, high-risk, or parallelizable project and should decide whether to delegate work to subagents with strict review gates. Also use when the user asks for Edict, 三省六部, multi-agent orchestration, autonomous subagent judgment, delegation, parallel agents, explorer/worker splits, verifier/reviewer agents, final audit, or evidence-based review for complex coding, research, documentation, or analysis tasks.
---

# Edict Agent

Use a lightweight Edict pattern to decide whether to stay single-agent or split work across subagents. Preserve one clear owner: the main Codex agent plans, delegates, reviews, integrates, verifies, and answers.

## Decision Rubric

Consider subagents when at least two of these are true:

- The task spans multiple modules, services, languages, papers, datasets, or artifacts.
- The codebase or evidence base is unfamiliar and needs parallel reconnaissance.
- Independent slices can be assigned with clear file, subsystem, or question ownership.
- A read-only audit, risk review, test-gap review, or alternative implementation check would materially improve quality.
- The task has enough uncertainty that one agent would spend a long time serially searching.
- The user has requested autonomous multi-agent judgment, Edict mode, delegation, or parallel work.

Stay single-agent when most of these are true:

- The change is small, local, or easy to verify.
- The work requires one tightly coherent edit across shared state.
- Delegation would create more merge risk than learning value.
- The task depends on private context that is not safe or useful to distribute.
- Tooling for subagents is unavailable; in that case, emulate the pattern with an explicit checklist and self-review.

## Edict Flow

1. Triage the request.
   Decide whether the project is large enough for delegation. Name the reason briefly.

2. Draft the edict.
   Convert the user's goal into acceptance criteria, constraints, likely affected areas, and verification commands.

3. Plan the ministries.
   Split only along natural ownership boundaries. Prefer one read-only explorer before multiple write workers when the codebase is not understood.

4. Dispatch subagents if justified and available.
   Give each subagent a narrow role, context, allowed scope, forbidden scope, and expected output. Avoid overlapping write ownership.

5. Review gate.
   Treat subagent outputs as proposals. Require evidence for important claims. Re-read important files yourself before editing or merging. Resolve contradictions explicitly.

6. Integrate and verify.
   The main agent performs final edits, inspects diffs, runs relevant tests/checks when possible, and owns the final answer.

7. Final audit.
   Before answering, perform a final pass over claims, changes, evidence, verification results, unverified areas, and residual risks.

8. Report compactly.
   Tell the user what was delegated, what was changed or learned, what was verified, what could not be verified, and any residual risk.

## Role Patterns

- Explorer: read-only investigation of architecture, call chains, failing behavior, data sources, or test coverage.
- Reviewer: skeptical audit of a plan, diff, paper section, migration, API contract, or UI behavior.
- Worker: scoped implementation for one subsystem or artifact with clear ownership.
- Verifier: run or design targeted checks, reproduce bugs, compare expected and actual behavior.

Default to Explorer or Reviewer for uncertain tasks. Use Worker only after ownership boundaries are clear.

## Delegation Prompt Shape

When launching a subagent, include:

- Objective: the one question or deliverable.
- Context: only the relevant user goal and constraints.
- Scope: exact files, directories, systems, sources, or questions to inspect or modify.
- Boundaries: what not to touch, what assumptions not to make, and whether edits are allowed.
- Output: concise findings, recommended actions, changed files, commands run, and risks.

Do not pass hidden conclusions as if they were facts. Independent review should stay independent.

## Quality Rules

- Keep delegation proportional to the task.
- Do not delegate final responsibility.
- Do not spawn agents just to create ceremony.
- Do not let subagents overwrite unrelated user work.
- Do not accept subagent output without direct verification when correctness matters.
- Prefer deterministic tests, diffs, rendered checks, or source citations over vibes.
- If subagents disagree, inspect the primary artifacts and decide with evidence.
- Do not treat "a subagent says so" as sufficient evidence.

## Strict Review Protocol

Apply this protocol whenever the task is large, high-risk, user-facing, security-sensitive, financially or legally consequential, cross-module, or uses subagents for implementation.

- Evidence: Require important subagent findings to include file paths, line numbers, command outputs, source links, screenshots, logs, or other primary evidence when available.
- Diff review: For code changes, inspect the final diff before answering. Confirm the diff matches the intended scope and does not include unrelated changes.
- Tests: Run relevant tests, type checks, linters, renders, or smoke checks when feasible. If not feasible, state why and identify what remains unverified.
- High-risk review: For high-risk tasks, use at least one Reviewer or Verifier subagent when subagents are available. If unavailable, perform a separate self-review pass using the same criteria.
- Claim audit: Before final response, check that each material claim is supported by direct inspection, a command result, a test result, or a cited source.
- Failure audit: Look for likely failure modes: missed call sites, stale assumptions, edge cases, race conditions, migration gaps, UI regressions, security/privacy leaks, and test blind spots.
- Final audit: End with an internal checklist covering scope, evidence, diff, tests, unverified items, and residual risk.
- Final response: Include verified items, unverified items, and residual risks when they matter. Keep the report compact.

## Lightweight Labels

Use the Edict metaphor internally as structure, not as performance. In user updates, plain engineering language is usually better:

- Triage: should this be parallel?
- Planning: what are the slices?
- Dispatch: who investigates or implements what?
- Review: what needs challenge?
- Integration: what lands?
- Verification: how do we know?
