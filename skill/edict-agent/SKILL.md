---
name: edict-agent
description: Apply automatically before writing a plan, creating tasks, or delegating work whenever the request touches three or more files, modules, or deliverables, is cross-module or architectural, is hard to reverse, or can be split across workers; also apply when the user asks for orchestration, review gates, or a final audit. Do not wait to be invoked, and do not ask whether to run the preflight. Single-file edits, trivial fixes, and pure Q&A are exempt. Also use for Edict, 三省六部, 求是分析, Quest Experts, custom subagents, multi-agent orchestration, file-exclusive worker slices, conflict-safe implementation, reviewer/verifier gates, final audits, or evidence-based review of complex coding, research, documentation, and analysis tasks.
when_to_use: Automatically before planning or delegating large, multi-file, cross-module, irreversible, or parallelizable work; also on explicit Edict, 三省六部, or 求是分析 requests. Skip for single-file edits, trivial fixes, and pure Q&A.
---

# Edict Agent

Use a lightweight Edict pattern to turn complex work into conflict-safe delivery. Preserve one clear owner: the main Qoder Agent, or the Team Lead in Quest Experts mode, runs the qiushi preflight, cuts the work into file-exclusive slices, delegates when the current Qoder surface supports it, reviews, integrates, verifies, and answers.

## Choose the Qoder Execution Path

Determine the active Qoder surface before dispatching work. Never assume another platform's agent-launch API or a fixed concurrency setting exists.

- **Normal Agent mode:** stay single-agent. Run the complete preflight, implementation, review, and verification as explicit phases in the same Agent context. Use the role checklists below as self-review lenses. Do not claim parallel execution.
- **Quest Experts mode (default multi-agent path):** let the Team Lead assign non-overlapping slices to Qoder's built-in Experts. Map the logical Edict roles by capability: Explorer/Researcher for investigation, Worker/Engineer for delivery, Reviewer for skeptical review, and Verifier/QA for testing. These built-in Experts are sufficient; this Skill does not require globally installed custom Agents. The Quest UI and runtime, not this Skill, determine the exact Expert names and actual concurrency.
- **Qoder CLI/custom-subagent mode:** use the closest built-in Agent/subagent capability exposed by the current Qoder surface. Chained calls may be sequential; describe work as parallel only when the active runtime explicitly schedules it concurrently.

If the closest built-in Expert is unavailable, continue with the equivalent single-agent phase instead of blocking the task.

### Fixed-name roles

The four roles `edict-explorer`, `edict-worker`, `edict-reviewer`, and `edict-verifier` are installed **user-level** in `~/.qoder/agents/`, so any session can delegate to them without per-project setup. The same definitions stay packaged under `assets/project-agent-templates/` as the source of truth, and `manage_project_agents.py` can still copy them into one project's `.qoder/agents/` when a project needs a pinned or modified variant.

This is a deliberate user decision (2026-11-01): always-available delegation was chosen over a minimal Agent menu. Trade it back to project-only by deleting those four files and reinstalling with the script below.

On Codex, this repository keeps `agents/openai.yaml` for the skill menu and the roles stay as prose checklists; Codex has no user-level Agent directory for these names, so treat the four roles as self-review lenses there rather than installed Agents. On Qoder, they are installed user-level as described above.

Do not install role Agents for any other reason, and do not duplicate a role into both scopes silently. A new or reloaded Quest may be required before Qoder shows newly added Agents.

```bash
python3 <resolved-edict-skill-dir>/scripts/manage_project_agents.py install --project-root <project-root>
```

Inspect without changing anything with `status` in place of `install`. Installation refuses to overwrite a different same-named file unless the user explicitly authorizes `--force`.

## Operating Bias

Default to finding deliverable worker slices, not serial execution and not parallel exploration for its own sake. Use explorers, reviewers, or verifiers only when they materially improve boundary clarity, safety, or confidence.

Stay single-agent when most of these are true:

- The change is small, local, or easy to verify.
- The work requires one tightly coherent edit across shared state.
- Safe file or directory ownership boundaries cannot be drawn.
- Delegation would create more merge risk than delivery value.
- The current Qoder surface does not expose Experts or custom subagents; in that case, use the normal Agent path and emulate the roles with an explicit checklist and separate self-review passes.

Use parallel workers when at least two of these are true:

- The task spans multiple modules, services, languages, papers, datasets, or artifacts.
- Independent implementation slices can be assigned with clear file, directory, subsystem, or artifact ownership.
- Several concrete features, fixes, checks, or document sections can progress at the same time.
- The user has requested autonomous multi-agent judgment, Edict mode, delegation, or parallel work.
- Parallel delivery would shorten the critical path without causing shared-file conflicts.

## Edict Flow

1. Qiushi preflight.
   Resolve the workflow source portably. First locate the sibling file `../qiushi-skill/references/workflows/METHOD.md` relative to this installed Skill directory. For a user-level Qoder installation, the equivalent fallback is `~/.qoder/skills/qiushi-skill/references/workflows/METHOD.md`. For a project-level installation, use that project's `.qoder/skills/qiushi-skill/references/workflows/METHOD.md`. Read and follow the resolved file. Keep this preflight lightweight unless the task itself demands the full workflow. Produce:
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

4. Choose the execution path and fanout.
   Use the normal Agent path for simple tasks or when Experts/subagents are unavailable. In Quest Experts mode, start with 2-4 Experts for medium tasks and add more only when there are additional clean ownership boundaries and the active Quest session permits it. In CLI/custom-subagent mode, use the smallest useful set of Agents. Never rely on a fixed thread-cap setting inherited from another platform.

5. Dispatch delivery workers when supported.
   In Quest Experts mode, assign slices through the Team Lead to Qoder's built-in Experts using the capability mapping below. In a Qoder surface exposing an Agent/subagent capability, invoke the closest available built-in role. Give each worker a narrow implementation objective, context, exclusive scope, forbidden scope, edit permissions, and expected output. Workers should advance one concrete functional point or subtask, not merely explore. Use an Explorer/Researcher only when ownership boundaries are not yet knowable. In normal Agent mode, execute the same slices serially yourself.

6. Conflict gate.
   Before edits begin, check for overlap. If two slices need the same file or artifact, do not let both workers edit it. Re-slice the work, make one worker advisory-only, or keep the shared change for the main agent to do serially.

7. Review gate.
   Treat worker outputs as proposals until inspected. Require evidence for important claims. Re-read important files yourself before merging or reporting. Use a built-in Reviewer or Verifier/QA Expert for high-risk, cross-module, user-facing, security-sensitive, financially or legally consequential tasks, or when workers disagree. In normal Agent mode, perform distinct skeptical-review and verification passes yourself.

8. Integrate and verify.
   The main agent owns final integration, shared files, diff review, tests/checks/renders when feasible, and the final answer.

9. Final audit.
   Before answering, check scope, evidence, diffs, tests, unverified areas, residual risks, and whether the parallel plan avoided shared-file conflicts.

## Role Patterns and Built-in Expert Mapping

- Explorer/Researcher (user-level Agent `edict-explorer`, or a built-in Expert): read-only investigation of architecture, call chains, failing behavior, data sources, or test coverage. Use only when boundaries are unclear.
- Worker/Engineer (user-level Agent `edict-worker`, or a built-in Expert): scoped implementation for one feature point, subsystem, artifact, or document section with exclusive ownership. Prefer this role for delivery slices.
- Reviewer (user-level Agent `edict-reviewer`, or a built-in Expert): skeptical, read-only audit of a plan, diff, paper section, migration, API contract, or UI behavior. Use for risk and contradiction checks.
- Verifier/QA (user-level Agent `edict-verifier`, or a built-in Expert): run targeted checks, reproduce bugs, and compare expected with actual behavior without editing implementation files.

Prefer the named `edict-*` Agents when the current surface can dispatch them: they carry the role's tool restrictions (`edict-explorer` and `edict-reviewer` cannot write; `edict-verifier` cannot edit), which a generic Expert does not. Fall back to built-in Experts when custom Agents are not dispatchable here.

## Worker Dispatch Prompt Shape

When assigning an Expert, invoking a custom subagent, or beginning a serial worker phase, include:

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
- Do not invoke Experts or custom Agents just to create ceremony.
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
- High-risk review: For high-risk tasks, use at least one built-in Reviewer or Verifier/QA Expert when Experts are available. If unavailable, perform a separate self-review pass using the same criteria.
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
