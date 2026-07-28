---
name: edict-agent
description: Use when Codex is facing a large, ambiguous, cross-module, high-risk, or parallelizable project and should use qiushi/workflows preflight before delegating work. Also use when the user asks for Edict, 三省六部, qiushi analysis before execution, multi-agent orchestration, autonomous subagent judgment, delegation, parallel delivery workers, file-exclusive worker slices, conflict-safe implementation, verifier/reviewer gates, final audit, or evidence-based review for complex coding, research, documentation, or analysis tasks.
---

# Edict Agent

Use a lightweight Edict pattern to turn complex work into conflict-safe parallel delivery. Preserve one clear owner: the main Codex agent runs the qiushi preflight, cuts the work into file-exclusive slices, delegates implementation workers, reviews, integrates, verifies, and answers.

## Operating Bias

Default to finding deliverable worker slices, not serial execution and not parallel exploration for its own sake. Use explorers, reviewers, or verifiers only when they materially improve boundary clarity, safety, or confidence.

Stay single-agent when most of these are true:

- The change is small, local, or easy to verify.
- The work requires one tightly coherent edit across shared state.
- Safe file or directory ownership boundaries cannot be drawn.
- Delegation would create more merge risk than delivery value.
- Tooling for subagents is unavailable; in that case, emulate the pattern with an explicit checklist and self-review.

Use parallel workers when at least two of these are true:

- The task spans multiple modules, services, languages, papers, datasets, or artifacts.
- Independent implementation slices can be assigned with clear file, directory, subsystem, or artifact ownership.
- Several concrete features, fixes, checks, or document sections can progress at the same time.
- The user has requested autonomous multi-agent judgment, Edict mode, delegation, or parallel work.
- Parallel delivery would shorten the critical path without causing shared-file conflicts.

## Edict Flow

1. Qiushi preflight.
   Read and follow `${CODEX_HOME:-$HOME/.codex}/skills/qiushi-skill/references/workflows/METHOD.md` as the qiushi workflow source. Keep this preflight lightweight unless the task itself demands the full workflow. Produce:
   - current situation
   - key constraints
   - main contradiction or bottleneck
   - acceptance criteria and verification signals
   - candidate parallel delivery slices
   - files, directories, or artifacts that must stay under main-agent ownership

2. Draft the edict.
   Convert the user's goal and qiushi preflight into concrete acceptance criteria, constraints, likely affected areas, worker slices, and verification commands.

3. Plan file-exclusive ministries.
   Split along natural ownership boundaries. Each worker must own a non-overlapping file, directory, subsystem, artifact, or document section. Shared files, entrypoints, configuration files, migrations, lockfiles, public API glue, and cross-cutting integration code stay with the main agent unless explicitly assigned to exactly one worker.

4. Choose fanout.
   Use one agent for simple tasks. Use 2-6 workers for medium tasks. For highly decomposable tasks with clean ownership boundaries, scale beyond 6 and up to the configured agents.max_threads cap, which may be 30. Do not chase the cap when slices are vague or overlapping.

5. Dispatch delivery workers.
   Give each worker a narrow implementation objective, context, exclusive scope, forbidden scope, edit permissions, and expected output. Workers should advance one concrete functional point or subtask, not merely explore. Use an explorer only when ownership boundaries are not yet knowable.

6. Conflict gate.
   Before edits begin, check for overlap. If two slices need the same file or artifact, do not let both workers edit it. Re-slice the work, make one worker advisory-only, or keep the shared change for the main agent to do serially.

7. Review gate.
   Treat worker outputs as proposals until inspected. Require evidence for important claims. Re-read important files yourself before merging or reporting. Use Reviewer or Verifier agents for high-risk, cross-module, user-facing, security-sensitive, financially or legally consequential tasks, or when workers disagree.

8. Integrate and verify.
   The main agent owns final integration, shared files, diff review, tests/checks/renders when feasible, and the final answer.

9. Final audit.
   Before answering, check scope, evidence, diffs, tests, unverified areas, residual risks, and whether the parallel plan avoided shared-file conflicts.

## Role Patterns

- Worker: scoped implementation for one feature point, subsystem, artifact, or document section with exclusive ownership. Prefer this role for parallel delivery.
- Explorer: read-only investigation of architecture, call chains, failing behavior, data sources, or test coverage. Use only when boundaries are unclear.
- Reviewer: skeptical audit of a plan, diff, paper section, migration, API contract, or UI behavior. Use for risk and contradiction checks.
- Verifier: run or design targeted checks, reproduce bugs, compare expected and actual behavior.

## Worker Dispatch Prompt Shape

When launching a worker subagent, include:

- Objective: the concrete deliverable to implement or advance.
- Context: only the relevant user goal, qiushi preflight result, and constraints.
- Exclusive scope: exact files, directories, systems, sources, or artifact sections the worker may modify.
- Forbidden scope: shared files, overlapping areas, unrelated cleanup, assumptions not to make, and anything reserved for the main agent.
- Coordination: whether the worker may edit files directly or must return a patch/proposal.
- Output: changed files, commands run, evidence, risks, and any integration notes for the main agent.

Do not pass hidden conclusions as facts. Independent review should stay independent.

## Conflict Rules

- Never assign the same file or artifact to multiple editing workers.
- Keep shared entrypoints, config, migrations, generated manifests, lockfiles, and broad public API wiring under main-agent control unless one worker receives exclusive ownership.
- If overlap appears after dispatch, stop the overlapping work, collect partial results, and reassign or merge serially.
- Ask workers to make the smallest scoped change that satisfies their slice.
- The main agent resolves cross-slice integration and final behavior.

## Quality Rules

- Run qiushi preflight every time this skill is used.
- Keep delegation proportional to the task, but do not default to serial when safe delivery slices exist.
- Do not delegate final responsibility.
- Do not spawn agents just to create ceremony.
- Do not let subagents overwrite unrelated user work.
- Do not accept subagent output without direct verification when correctness matters.
- Prefer deterministic tests, diffs, rendered checks, or source citations over vibes.
- If subagents disagree, inspect the primary artifacts and decide with evidence.
- Do not treat "a subagent says so" as sufficient evidence.

## Strict Review Protocol

Apply this protocol whenever the task is large, high-risk, user-facing, security-sensitive, financially or legally consequential, cross-module, or uses subagents for implementation.

- Evidence: Require important worker or reviewer findings to include file paths, line numbers, command outputs, source links, screenshots, logs, or other primary evidence when available.
- Diff review: For code changes, inspect the final diff before answering. Confirm the diff matches the intended scope and does not include unrelated changes.
- Tests: Run relevant tests, type checks, linters, renders, or smoke checks when feasible. If not feasible, state why and identify what remains unverified.
- High-risk review: For high-risk tasks, use at least one Reviewer or Verifier subagent when subagents are available. If unavailable, perform a separate self-review pass using the same criteria.
- Claim audit: Before final response, check that each material claim is supported by direct inspection, a command result, a test result, or a cited source.
- Failure audit: Look for likely failure modes: missed call sites, stale assumptions, edge cases, race conditions, migration gaps, UI regressions, security/privacy leaks, and test blind spots.
- Final audit: End with an internal checklist covering scope, evidence, diff, tests, unverified items, residual risk, and conflict avoidance.
- Final response: Include delegated slices, changed or learned items, verified items, unverified items, and residual risks when they matter. Keep the report compact.

## Lightweight Labels

Use the Edict metaphor internally as structure, not as performance. In user updates, plain engineering language is usually better:

- Qiushi preflight: what is the real situation and main bottleneck?
- Planning: what are the safe delivery slices?
- Dispatch: which worker owns which files or artifacts?
- Conflict gate: what must stay with the main agent?
- Review: what needs challenge?
- Integration: what lands?
- Verification: how do we know?
