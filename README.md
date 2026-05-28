# Edict Agent

Edict Agent is a Codex skill for large or high-risk work that may benefit from multi-agent delegation. It helps Codex decide whether to stay single-agent or split work across explorer, reviewer, worker, and verifier roles, then requires strict evidence-based review before reporting.

The skill is inspired by an "edict" workflow: triage the request, draft acceptance criteria, delegate only when useful, review outputs as proposals, verify with evidence, and report residual risk.

## What It Does

- Decides whether a task is worth splitting across subagents.
- Defines role patterns for Explorer, Reviewer, Worker, and Verifier agents.
- Requires scoped delegation prompts with objective, context, scope, boundaries, and output expectations.
- Adds strict review gates for evidence, diff review, tests, claim audit, failure audit, and final audit.
- Keeps the main Codex agent responsible for integration, verification, and the final answer.

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill/edict-agent "${CODEX_HOME:-$HOME/.codex}/skills/edict-agent"
```

Then start a new Codex session so the skill can be discovered.

## Use

Explicit invocation:

```text
Use $edict-agent to decide whether to split this task across subagents and run strict review before reporting.
```

Implicit invocation is enabled in `skill/edict-agent/agents/openai.yaml`, so Codex can also use it when a task is large, ambiguous, cross-module, high-risk, or parallelizable.

## Privacy

This repository intentionally contains only generic skill instructions and metadata. It does not include local filesystem paths, private prompts, conversation logs, credentials, project data, or user-specific configuration.

Before publishing your own fork, scan for local paths, access credentials, proprietary names, and private data.

## License

MIT License. See `LICENSE`.
