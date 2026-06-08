# Edict Agent

Edict Agent is a Codex skill for complex, ambiguous, high-risk, cross-module, or parallelizable tasks. It gives Codex a strict action plan for running a qiushi/workflows preflight, splitting work into conflict-safe delivery slices when useful, reviewing worker outputs, and keeping the main agent accountable for the final result.

This skill is inspired by the logic of the **Three Departments and Six Ministries** system, known in Chinese as **三省六部制**. The goal is not to roleplay an ancient bureaucracy. The goal is to borrow its governance logic: separation of planning, review, execution, and final responsibility.

In practical terms, Edict Agent defines a small set of rules for improving the relationship between the Codex main agent and subagents during complex work. Subagents can investigate, challenge, implement, or verify, but they do not own the final answer. The main Codex agent must run the preflight, cut file-exclusive slices, delegate, audit, integrate, test, and report.

## Why This Skill Exists

Large AI coding or research tasks often fail for predictable reasons:

- One agent tries to understand a whole codebase serially and misses important context.
- Multiple agents work without clear ownership and create conflicts.
- Subagent findings are accepted too easily without evidence.
- Implementation happens before the problem is properly scoped.
- Final answers sound confident even when some parts were not verified.

Edict Agent addresses these failure modes by turning multi-agent work into a governed process. It asks Codex to start with a lightweight qiushi preflight, prefer deliverable worker slices over vague exploration, assign non-overlapping ownership, require evidence, inspect diffs, run checks when possible, and disclose residual risk.

## Three Departments and Six Ministries Logic

The historical 三省六部制 separated state work into planning, review, and execution bodies. Edict Agent adapts that idea into a lightweight AI workflow:

| Historical Logic | Edict Agent Interpretation |
| --- | --- |
| Edict / imperial command | The user's goal, constraints, and acceptance criteria |
| 中书省 / drafting | The main agent turns the request and qiushi preflight into a concrete plan |
| 门下省 / review and rejection | Reviewer or verifier logic challenges assumptions and checks evidence |
| 尚书省 / administration | The main agent dispatches scoped work and coordinates integration |
| 六部 / specialized ministries | Workers handle bounded delivery slices; explorers, reviewers, and verifiers support when useful |
| 回奏 / report back | The main agent reports changes, validation, unknowns, and residual risk |

This structure creates productive friction. Planning is separated from review. Execution is scoped. Verification is explicit. The final response is not simply what a subagent claimed; it is what the main agent can defend with evidence.

## Main Agent and Subagent Rules

Edict Agent treats the main Codex agent as the accountable owner.

The main agent must:

- Run a lightweight qiushi/workflows preflight before delegation.
- Convert the request and preflight into acceptance criteria and likely affected areas.
- Split work only along natural, non-overlapping ownership boundaries.
- Keep shared entrypoints, configuration, lockfiles, generated manifests, and cross-cutting integration under one clear owner.
- Give workers narrow objectives, context, exclusive scope, forbidden scope, and output expectations.
- Treat subagent outputs as proposals, not final truth.
- Re-read important files or evidence before integrating conclusions.
- Inspect final diffs for code changes.
- Run relevant checks when feasible.
- Perform a final audit before answering.
- Clearly report verified items, unverified items, and residual risk when they matter.

Subagents may:

- Explore unfamiliar code, data, documents, or architecture.
- Review a plan, diff, claim, paper section, or API contract.
- Implement one clearly scoped subsystem, file group, artifact, or document section.
- Verify behavior through tests, reproduction steps, logs, screenshots, or source evidence.

Subagents must not:

- Own the final answer.
- Modify unrelated files.
- Work in overlapping files, directories, artifacts, or document sections without coordination.
- Replace direct evidence with confidence.
- Cause the main agent to skip review.

## Role Patterns

Edict Agent defines four common subagent roles:

- **Worker**: scoped implementation for one feature point, subsystem, file group, artifact, or document section with exclusive ownership.
- **Explorer**: read-only investigation of architecture, call chains, failing behavior, data sources, or test coverage. Use this when ownership boundaries are unclear.
- **Reviewer**: skeptical audit of a plan, diff, paper section, migration, API contract, or UI behavior.
- **Verifier**: targeted checking through tests, reproduction, smoke checks, rendered output, logs, or other evidence.

The default posture is delivery-oriented but conflict-aware: look for useful worker slices, use explorers only when boundaries are not yet knowable, and keep final integration with the main agent.

## Strict Action Plan

When Edict Agent is triggered, Codex follows this action plan:

1. **Qiushi preflight**
   Identify the current situation, key constraints, main contradiction or bottleneck, acceptance criteria, verification signals, candidate delivery slices, and shared artifacts that must stay under main-agent ownership.

2. **Draft the edict**
   Convert the user request and preflight into goals, constraints, acceptance criteria, likely affected areas, worker slices, and verification commands.

3. **Plan file-exclusive ministries**
   Split work by natural boundaries such as subsystem, file group, research question, test surface, artifact type, or document section. Do not assign overlapping write ownership.

4. **Choose fanout**
   Use one agent for simple tasks, 2-6 workers for medium tasks with clean boundaries, and more only when the work is highly decomposable.

5. **Dispatch delivery workers**
   Assign narrow roles with objective, context, exclusive scope, forbidden scope, coordination rules, and expected output.

6. **Conflict gate**
   Check for overlapping file, directory, artifact, or document ownership before edits begin. Re-slice or keep shared work with the main agent when needed.

7. **Review gate**
   Treat worker output as a proposal. Require evidence for important claims. Re-read important files, logs, sources, or diffs.

8. **Integrate and verify**
   The main agent performs final edits, inspects the diff, runs relevant checks when feasible, and resolves contradictions.

9. **Final audit**
   Before answering, the main agent checks scope, evidence, diff, tests, unverified items, residual risk, and conflict avoidance.

## Strict Review Gates

For large, user-facing, security-sensitive, financial, legal, cross-module, or high-risk work, Edict Agent requires stricter review:

- Important worker or reviewer findings should include file paths, line numbers, command outputs, source links, screenshots, logs, or other primary evidence when available.
- Code changes require final diff inspection.
- Relevant tests, type checks, linters, renders, or smoke checks should be run when feasible.
- If checks cannot be run, the final answer should state what remains unverified.
- High-risk tasks should use at least one Reviewer or Verifier subagent when subagents are available.
- "A subagent says so" is not sufficient evidence.
- Conflicting worker, reviewer, or verifier conclusions must be resolved against primary artifacts.

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill/edict-agent "${CODEX_HOME:-$HOME/.codex}/skills/edict-agent"
```

Then start a new Codex session so the skill can be discovered.

Edict Agent can use the installed `workflows` skill as its qiushi workflow source when available, typically at `${CODEX_HOME:-$HOME/.codex}/skills/workflows/SKILL.md`. If that skill is unavailable, Edict Agent still runs the compact preflight described in `SKILL.md`.

## Use

Explicit invocation:

```text
Use $edict-agent to run a lightweight qiushi/workflows preflight, split this task into file-exclusive parallel worker slices where safe, then integrate and review with strict evidence gates.
```

Implicit invocation is enabled in `skill/edict-agent/agents/openai.yaml`, so Codex can also use it when a task is large, ambiguous, cross-module, high-risk, or parallelizable.

---

# Edict Agent 中文说明

Edict Agent 是一个面向 Codex 的 skill，用于处理复杂、模糊、高风险、跨模块或适合并行拆解的任务。它为 Codex 制定一套严格行动计划：先运行 qiushi/workflows 预检，再在安全时把工作拆成不冲突的交付切片，审查 worker 输出，并确保主 agent 对最终结果负责。

这个 skill 参考了中国古代 **三省六部制** 的治理逻辑。它不是为了做古风角色扮演，而是借用其中更重要的制度思想：**规划、审核、执行、归责相互分离，但最终责任必须清楚**。

在实际使用中，Edict Agent 会规范 Codex 主 agent 与子 agent 的关系。子 agent 可以调查、质疑、实现或验证，但不能替代主 agent 对最终答案负责。主 agent 必须完成预检、切出文件独占的工作边界、分派、审查、整合、测试和最终汇报。

## 为什么需要这个 Skill

大型 AI 编程或研究任务经常出现几个问题：

- 单个 agent 串行理解整个项目，容易漏掉关键上下文。
- 多个 agent 没有清楚分工，容易产生冲突。
- 子 agent 的结论被过早接受，缺少证据。
- 问题还没界定清楚就开始实现。
- 最终回答看起来很自信，但部分结果并没有验证。

Edict Agent 的作用就是把多 agent 工作变成一套有治理结构的流程。它要求 Codex 先做轻量 qiushi 预检，优先寻找可交付的 worker 切片而不是空泛探索，再设置不重叠的所有权边界，要求证据，检查 diff，在可行时运行测试，并在最终回答中说明残余风险。

## 三省六部制的映射

三省六部制把政务拆成起草、审核、执行等不同环节。Edict Agent 将这种制度逻辑转化为轻量级 AI 工作流：

| 三省六部逻辑 | Edict Agent 中的含义 |
| --- | --- |
| 皇帝下旨 | 用户目标、约束和验收标准 |
| 中书省起草 | 主 agent 将用户需求和 qiushi 预检转化为具体计划 |
| 门下省审核/封驳 | Reviewer 或 Verifier 对假设和证据进行挑战 |
| 尚书省统筹执行 | 主 agent 分派任务并协调整合 |
| 六部分工办事 | Worker 处理边界清楚的交付切片；Explorer、Reviewer、Verifier 在有帮助时支持 |
| 回奏 | 主 agent 汇报改动、验证结果、未知项和残余风险 |

这套结构的重点是制造有益的制衡。规划和审核分离，执行有边界，验证必须显式进行。最终回答不是简单复述某个子 agent 的说法，而是主 agent 能够用证据支撑的结论。

## 主 Agent 与子 Agent 的法规

Edict Agent 将 Codex 主 agent 设定为最终责任人。

主 agent 必须：

- 在分派前运行轻量 qiushi/workflows 预检。
- 将用户需求和预检结论转化为验收标准和可能影响范围。
- 只按照自然且不重叠的所有权边界拆分任务。
- 将共享入口、配置、锁文件、生成清单和跨切片整合代码保留给一个明确负责人。
- 为 worker 指定明确目标、上下文、独占范围、禁止范围和输出要求。
- 将子 agent 的输出视为建议，而不是最终事实。
- 在整合结论前重新阅读关键文件或证据。
- 对代码改动检查最终 diff。
- 在可行时运行相关检查。
- 在最终回答前进行 final audit。
- 在必要时清楚说明已验证项、未验证项和残余风险。

子 agent 可以：

- 调查不熟悉的代码、数据、文档或架构。
- 审查方案、diff、结论、论文段落或 API 契约。
- 在明确边界内实现某个子系统、文件组、产物或文档章节。
- 通过测试、复现步骤、日志、截图或来源证据验证行为。

子 agent 不得：

- 拥有最终答案。
- 修改无关文件。
- 在没有协调的情况下处理相互重叠的文件、目录、产物或文档章节。
- 用自信替代证据。
- 让主 agent 跳过审查。

## 角色模式

Edict Agent 定义了四类常见子 agent：

- **Worker**：在独占边界内实现某个功能点、子系统、文件组、产物或文档章节。
- **Explorer**：只读调查架构、调用链、失败行为、数据来源或测试覆盖。仅在边界尚不清楚时使用。
- **Reviewer**：对方案、diff、论文段落、迁移、API 契约或 UI 行为进行怀疑式审查。
- **Verifier**：通过测试、复现、smoke check、渲染结果、日志或其他证据进行验证。

默认策略是面向交付但避免冲突：先寻找有用的 worker 切片，只有在边界还不清楚时使用 Explorer，最终整合仍由主 agent 负责。

## 严格行动计划

当 Edict Agent 被触发时，Codex 遵循以下行动计划：

1. **Qiushi 预检**
   识别当前现状、关键约束、主要矛盾或瓶颈、验收标准、验证信号、候选交付切片，以及必须由主 agent 保留的共享产物。

2. **拟定诏令**
   将用户需求和预检结论转化为目标、约束、验收标准、可能影响范围、worker 切片和验证命令。

3. **规划文件独占部司**
   按照子系统、文件组、研究问题、测试面、产物类型或文档章节等自然边界拆分工作，不分配相互重叠的写入所有权。

4. **选择并行度**
   简单任务使用一个 agent；边界清楚的中型任务使用 2-6 个 worker；只有在高度可拆解时才扩大并行度。

5. **分派交付 worker**
   设定明确角色、目标、上下文、独占范围、禁止范围、协作规则和输出要求。

6. **冲突关口**
   在编辑开始前检查文件、目录、产物或文档章节所有权是否重叠。必要时重新切片，或将共享工作留给主 agent。

7. **审核关口**
   将 worker 输出视为建议。关键结论必须有证据。主 agent 需要重新阅读关键文件、日志、来源或 diff。

8. **整合与验证**
   主 agent 负责最终编辑、检查 diff、在可行时运行相关检查，并解决不同结论之间的冲突。

9. **最终审计**
   在回答前检查范围、证据、diff、测试、未验证项、残余风险和冲突规避情况。

## 严格审查关卡

对于大型、面向用户、安全敏感、金融、法律、跨模块或高风险任务，Edict Agent 要求更严格的审查：

- 重要的 worker 或 reviewer 结论应尽可能包含文件路径、行号、命令输出、来源链接、截图、日志或其他原始证据。
- 代码改动必须检查最终 diff。
- 在可行时应运行相关测试、类型检查、lint、渲染检查或 smoke check。
- 如果无法运行检查，最终回答应说明哪些内容仍未验证。
- 高风险任务在子 agent 可用时，至少应使用一个 Reviewer 或 Verifier。
- “某个子 agent 是这么说的”不能作为充分证据。
- worker、reviewer 或 verifier 之间结论冲突时，必须回到原始材料判断。

## 安装

将 skill 文件夹复制到 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skill/edict-agent "${CODEX_HOME:-$HOME/.codex}/skills/edict-agent"
```

然后启动新的 Codex 会话，让 Codex 发现这个 skill。

当已安装 `workflows` skill 时，Edict Agent 可以将它作为 qiushi workflow 来源，通常路径是 `${CODEX_HOME:-$HOME/.codex}/skills/workflows/SKILL.md`。如果没有安装该 skill，Edict Agent 仍会按 `SKILL.md` 中描述的简化预检直接执行。

## 使用

显式调用：

```text
Use $edict-agent to run a lightweight qiushi/workflows preflight, split this task into file-exclusive parallel worker slices where safe, then integrate and review with strict evidence gates.
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
