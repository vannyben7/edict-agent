# Edict Agent

Edict Agent is a Codex skill for complex, ambiguous, high-risk, or cross-module tasks. It gives Codex a strict action plan for deciding when to use subagents, how to assign them, how to review their outputs, and how the main agent should remain accountable for the final result.

This skill is inspired by the logic of the **Three Departments and Six Ministries** system, known in Chinese as **三省六部制**. The goal is not to roleplay an ancient bureaucracy. The goal is to borrow its governance logic: separation of planning, review, execution, and final responsibility.

In practical terms, Edict Agent defines a small set of rules for improving the relationship between the Codex main agent and subagents during complex work. Subagents can investigate, challenge, implement, or verify, but they do not own the final answer. The main Codex agent must plan, delegate, audit, integrate, test, and report.

## Why This Skill Exists

Large AI coding or research tasks often fail for predictable reasons:

- One agent tries to understand a whole codebase serially and misses important context.
- Multiple agents work without clear ownership and create conflicts.
- Subagent findings are accepted too easily without evidence.
- Implementation happens before the problem is properly scoped.
- Final answers sound confident even when some parts were not verified.

Edict Agent addresses these failure modes by turning multi-agent work into a governed process. It asks Codex to decide whether delegation is useful, assign narrow roles, require evidence, inspect diffs, run checks when possible, and disclose residual risk.

## Three Departments and Six Ministries Logic

The historical 三省六部制 separated state work into planning, review, and execution bodies. Edict Agent adapts that idea into a lightweight AI workflow:

| Historical Logic | Edict Agent Interpretation |
| --- | --- |
| Edict / imperial command | The user's goal, constraints, and acceptance criteria |
| 中书省 / drafting | The main agent turns the request into a concrete plan |
| 门下省 / review and rejection | Reviewer or verifier logic challenges assumptions and checks evidence |
| 尚书省 / administration | The main agent dispatches scoped work and coordinates execution |
| 六部 / specialized ministries | Subagents handle bounded investigation, implementation, review, or verification |
| 回奏 / report back | The main agent reports changes, validation, unknowns, and residual risk |

This structure creates productive friction. Planning is separated from review. Execution is scoped. Verification is explicit. The final response is not simply what a subagent claimed; it is what the main agent can defend with evidence.

## Main Agent and Subagent Rules

Edict Agent treats the main Codex agent as the accountable owner.

The main agent must:

- Decide whether the task actually needs subagents.
- Convert the request into acceptance criteria and likely affected areas.
- Split work only along natural ownership boundaries.
- Give subagents narrow objectives, context, scope, boundaries, and output expectations.
- Treat subagent outputs as proposals, not final truth.
- Re-read important files or evidence before integrating conclusions.
- Inspect final diffs for code changes.
- Run relevant checks when feasible.
- Perform a final audit before answering.
- Clearly report verified items, unverified items, and residual risk when they matter.

Subagents may:

- Explore unfamiliar code, data, documents, or architecture.
- Review a plan, diff, claim, paper section, or API contract.
- Implement one clearly scoped subsystem or artifact.
- Verify behavior through tests, reproduction steps, logs, screenshots, or source evidence.

Subagents must not:

- Own the final answer.
- Modify unrelated files.
- Work in overlapping areas without coordination.
- Replace direct evidence with confidence.
- Cause the main agent to skip review.

## Role Patterns

Edict Agent defines four common subagent roles:

- **Explorer**: read-only investigation of architecture, call chains, failing behavior, data sources, or test coverage.
- **Reviewer**: skeptical audit of a plan, diff, paper section, migration, API contract, or UI behavior.
- **Worker**: scoped implementation for one subsystem or artifact with clear ownership.
- **Verifier**: targeted checking through tests, reproduction, smoke checks, rendered output, logs, or other evidence.

The default posture is conservative: use Explorer or Reviewer first when the task is unclear, then use Worker only after ownership boundaries are clear.

## Strict Action Plan

When Edict Agent is triggered, Codex follows this action plan:

1. **Triage the request**
   Decide whether the task is large, high-risk, cross-module, ambiguous, or parallelizable enough to justify delegation.

2. **Draft the edict**
   Convert the user request into goals, constraints, acceptance criteria, likely affected areas, and verification commands.

3. **Plan the ministries**
   Split work by natural boundaries such as subsystem, file group, research question, test surface, or artifact type.

4. **Dispatch subagents**
   Assign narrow roles with objective, context, scope, boundaries, and expected output. Avoid overlapping write ownership.

5. **Review gate**
   Treat subagent output as a proposal. Require evidence for important claims. Re-read important files, logs, sources, or diffs.

6. **Integrate and verify**
   The main agent performs final edits, inspects the diff, runs relevant checks when feasible, and resolves contradictions.

7. **Final audit**
   Before answering, the main agent checks scope, evidence, diff, tests, unverified items, and residual risk.

8. **Report compactly**
   The final answer explains what was delegated, what changed or was learned, what was verified, what could not be verified, and what risk remains.

## Strict Review Gates

For large, user-facing, security-sensitive, financial, legal, cross-module, or high-risk work, Edict Agent requires stricter review:

- Important findings should include file paths, line numbers, command outputs, source links, screenshots, logs, or other primary evidence when available.
- Code changes require final diff inspection.
- Relevant tests, type checks, linters, renders, or smoke checks should be run when feasible.
- If checks cannot be run, the final answer should state what remains unverified.
- High-risk tasks should use at least one Reviewer or Verifier subagent when subagents are available.
- "A subagent says so" is not sufficient evidence.
- Conflicting subagent conclusions must be resolved against primary artifacts.

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

---

# Edict Agent 中文说明

Edict Agent 是一个面向 Codex 的 skill，用于处理复杂、模糊、高风险、跨模块或适合并行拆解的任务。它为 Codex 制定一套严格行动计划：什么时候应该使用子 agent，如何分派子 agent，如何审查子 agent 的结论，以及主 agent 如何对最终结果负责。

这个 skill 参考了中国古代 **三省六部制** 的治理逻辑。它不是为了做古风角色扮演，而是借用其中更重要的制度思想：**规划、审核、执行、归责相互分离，但最终责任必须清楚**。

在实际使用中，Edict Agent 会规范 Codex 主 agent 与子 agent 的关系。子 agent 可以调查、质疑、实现或验证，但不能替代主 agent 对最终答案负责。主 agent 必须完成规划、分派、审查、整合、测试和最终汇报。

## 为什么需要这个 Skill

大型 AI 编程或研究任务经常出现几个问题：

- 单个 agent 串行理解整个项目，容易漏掉关键上下文。
- 多个 agent 没有清楚分工，容易产生冲突。
- 子 agent 的结论被过早接受，缺少证据。
- 问题还没界定清楚就开始实现。
- 最终回答看起来很自信，但部分结果并没有验证。

Edict Agent 的作用就是把多 agent 工作变成一套有治理结构的流程。它要求 Codex 先判断是否值得分派，再设置清晰角色，要求证据，检查 diff，在可行时运行测试，并在最终回答中说明残余风险。

## 三省六部制的映射

三省六部制把政务拆成起草、审核、执行等不同环节。Edict Agent 将这种制度逻辑转化为轻量级 AI 工作流：

| 三省六部逻辑 | Edict Agent 中的含义 |
| --- | --- |
| 皇帝下旨 | 用户目标、约束和验收标准 |
| 中书省起草 | 主 agent 将需求转化为具体计划 |
| 门下省审核/封驳 | Reviewer 或 Verifier 对假设和证据进行挑战 |
| 尚书省统筹执行 | 主 agent 分派任务并协调执行 |
| 六部分工办事 | 子 agent 承担调查、实现、审查或验证等边界清楚的任务 |
| 回奏 | 主 agent 汇报改动、验证结果、未知项和残余风险 |

这套结构的重点是制造有益的制衡。规划和审核分离，执行有边界，验证必须显式进行。最终回答不是简单复述某个子 agent 的说法，而是主 agent 能够用证据支撑的结论。

## 主 Agent 与子 Agent 的法规

Edict Agent 将 Codex 主 agent 设定为最终责任人。

主 agent 必须：

- 判断任务是否真的需要子 agent。
- 将需求转化为验收标准和可能影响范围。
- 只按照自然边界拆分任务。
- 为子 agent 指定明确目标、上下文、范围、边界和输出要求。
- 将子 agent 的输出视为建议，而不是最终事实。
- 在整合结论前重新阅读关键文件或证据。
- 对代码改动检查最终 diff。
- 在可行时运行相关检查。
- 在最终回答前进行 final audit。
- 在必要时清楚说明已验证项、未验证项和残余风险。

子 agent 可以：

- 调查不熟悉的代码、数据、文档或架构。
- 审查方案、diff、结论、论文段落或 API 契约。
- 在明确边界内实现某个子系统或产物。
- 通过测试、复现步骤、日志、截图或来源证据验证行为。

子 agent 不得：

- 拥有最终答案。
- 修改无关文件。
- 在没有协调的情况下处理相互重叠的范围。
- 用自信替代证据。
- 让主 agent 跳过审查。

## 角色模式

Edict Agent 定义了四类常见子 agent：

- **Explorer**：只读调查架构、调用链、失败行为、数据来源或测试覆盖。
- **Reviewer**：对方案、diff、论文段落、迁移、API 契约或 UI 行为进行怀疑式审查。
- **Worker**：在清楚边界内实现一个子系统或产物。
- **Verifier**：通过测试、复现、smoke check、渲染结果、日志或其他证据进行验证。

默认策略是保守的：当任务还不清楚时，优先使用 Explorer 或 Reviewer；只有当边界清楚后，才使用 Worker。

## 严格行动计划

当 Edict Agent 被触发时，Codex 遵循以下行动计划：

1. **分拣任务**
   判断任务是否足够复杂、高风险、跨模块、模糊或可并行，是否值得分派子 agent。

2. **拟定诏令**
   将用户需求转化为目标、约束、验收标准、可能影响范围和验证命令。

3. **规划部司**
   按照子系统、文件组、研究问题、测试面或产物类型等自然边界拆分工作。

4. **分派子 agent**
   设定明确角色、目标、上下文、范围、边界和输出要求，避免多个子 agent 同时写同一范围。

5. **审核关口**
   将子 agent 输出视为建议。关键结论必须有证据。主 agent 需要重新阅读关键文件、日志、来源或 diff。

6. **整合与验证**
   主 agent 负责最终编辑、检查 diff、在可行时运行相关检查，并解决不同结论之间的冲突。

7. **最终审计**
   在回答前检查范围、证据、diff、测试、未验证项和残余风险。

8. **简明回奏**
   最终回答说明分派了什么、改变或发现了什么、验证了什么、什么没有验证，以及还剩什么风险。

## 严格审查关卡

对于大型、面向用户、安全敏感、金融、法律、跨模块或高风险任务，Edict Agent 要求更严格的审查：

- 重要结论应尽可能包含文件路径、行号、命令输出、来源链接、截图、日志或其他原始证据。
- 代码改动必须检查最终 diff。
- 在可行时应运行相关测试、类型检查、lint、渲染检查或 smoke check。
- 如果无法运行检查，最终回答应说明哪些内容仍未验证。
- 高风险任务在子 agent 可用时，至少应使用一个 Reviewer 或 Verifier。
- “某个子 agent 是这么说的”不能作为充分证据。
- 子 agent 之间结论冲突时，必须回到原始材料判断。

## 安装

将 skill 文件夹复制到 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill/edict-agent "${CODEX_HOME:-$HOME/.codex}/skills/edict-agent"
```

然后启动新的 Codex 会话，让 Codex 发现这个 skill。

## 使用

显式调用：

```text
Use $edict-agent to decide whether to split this task across subagents and run strict review before reporting.
```

`skill/edict-agent/agents/openai.yaml` 已启用隐式调用，因此当任务大型、模糊、跨模块、高风险或适合并行时，Codex 也可以自动使用它。

## Privacy / 隐私

This repository intentionally contains only generic skill instructions and metadata. It does not include local filesystem paths, private prompts, conversation logs, credentials, project data, or user-specific configuration.

本仓库只包含通用的 skill 指令和元数据，不包含本地文件路径、私人提示词、对话记录、凭据、项目数据或用户特定配置。

Before publishing your own fork, scan for local paths, access credentials, proprietary names, and private data.

发布你自己的 fork 前，请扫描本地路径、访问凭据、专有名称和私人数据。

## License / 许可证

MIT License. See `LICENSE`.

采用 MIT License，详见 `LICENSE`。
