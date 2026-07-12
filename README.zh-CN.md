# Preflight

一个与厂商无关的 AI Agent 行为协议，帮助 Agent 在行动前先理解真正的问题。

[English](README.md)

> **问题：** Agent 可能完成表面要求，却遗漏真正目标、约束或授权边界。**Preflight：** 先完成任务预检，再采取行动。

### 30 秒示例

| 请求 | 未使用 Preflight | 使用 Preflight |
|---|---|---|
| “今天做一个支持 CSV、Excel 和 JSON 的客户数据导出。” | 擅自编造字段和权限，然后开始写代码。 | 先确认目标用户、数据范围、授权方式、成功标准、风险和最小阻塞决策。 |

Preflight 有意保持轻量：“修正这个错别字”仍然应该直接修正。

## 为什么需要它

Agent 有时能够完成表面上的要求，却遗漏用户真正的目标、隐藏约束、授权边界或成功标准。Preflight 在有意义的行动前加入一个轻量检查：

- 简单任务保持简单；
- 模糊需求先暴露真正影响方案的决策；
- 风险被说明，而不是被默默忽略；
- 不凭空越过受保护的边界；
- 多轮对话在目标或范围变化时重新校准；
- 默认不展示内部工作流名称或私有思维过程。

Preflight 是指令级行为协议，不是运行时强制执行器，也不是安全系统。平台安全策略、系统指令、用户明确约束和应用自身的权限控制始终优先。

## 仓库内容

- [`SKILL.md`](SKILL.md)：供支持 Skill 的 Agent 使用的可复用能力。
- [`AGENTS.md`](AGENTS.md)：可复制到全局或项目级指令文件中的任务边界模板。
- [`tests/cases.md`](tests/cases.md)：可观察的压力测试场景。
- [`tests/validate_skill.py`](tests/validate_skill.py)：无第三方依赖的结构校验。
- [`tests/evaluate_response.py`](tests/evaluate_response.py)：对保存下来的 Agent 响应进行保守的可观察性检查。
- [`examples/customer-export-before-after.md`](examples/customer-export-before-after.md)：可复现的前后对比演示。

## 安装方式

### Skill-aware Agent

将本仓库作为 Skill 安装或复制，保留 `SKILL.md` 和 `agents/openai.yaml`。当任务可能隐藏重要目标、约束、风险、成功条件、授权边界或未决假设时，加载 Preflight。

对于 Codex、Claude Code、Cursor 和其他支持 Skill 的 Agent，请使用对应平台的标准 Skill 目录或市场安装流程。本仓库只有指令文件，没有运行时依赖。

### 全局或项目级激活

将 [`AGENTS.md`](AGENTS.md) 的内容复制到 Agent 支持的全局或项目级指令文件中。这样可以在每个新任务开始时运行一次，并在后续对话实质改变任务目标、范围、权限、数据、环境、期限或风险时重新运行。

### 两者一起使用

Skill 提供完整的可复用方法，`AGENTS.md` 提供任务边界级的激活方式。建议只保留一份权威模板，避免不同版本的规则互相冲突。

## 发布版本

首个公开版本是 [v0.1.0](https://github.com/sgadfadjfads-cloud/preflight/releases/tag/v0.1.0)。Preflight 是一个持续演进的 Agent 行为实验，欢迎通过 Issue 或 Pull Request 提交具体失败案例。

## 示例

对于“今天做一个支持 CSV、Excel 和 JSON 的客户数据导出功能”，Agent 不应擅自编造字段、权限或上线审批。它应先识别目标用户、数据范围、授权方式、成功标准、主要风险和最小的待确认决策。

对于“修正这句话里的错别字”，Agent 应直接完成修正，不应启动完整的需求访谈。

想看一个可复现的前后对比，请参阅 [`examples/customer-export-before-after.md`](examples/customer-export-before-after.md)。

## 验证

运行结构校验：

```bash
python3 tests/validate_skill.py
```

然后按照 [`tests/cases.md`](tests/cases.md) 中的场景，分别在加载和未加载 Skill 的情况下测试，并比较可观察行为。提示词测试只能评估行为倾向，不能证明所有模型都能被确定性约束。

对保存下来的响应运行保守检查：

```bash
python3 tests/evaluate_response.py ambiguous-feature response.txt
```

该检查器只检查可观察概念和明显违规，不是语义裁判，仍应配合人工复核。

## 设计原则

深入判断，简洁且完整地表达；透明说明风险；尊重授权边界；不暴露私有思维过程。

## 当前限制

- Skill 和 `AGENTS.md` 都是自然语言指令，不是硬性运行时控制。
- 不同 Agent、模型和宿主环境的触发与遵循程度可能不同。
- 自动评估器只能发现明显信号，不能替代真实环境中的人工评估。
- Preflight 不替代权限系统、审批系统、审计系统或平台安全策略。

## 贡献

欢迎通过 Issue 或 Pull Request 提交新的压力场景、兼容性反馈和改进建议。贡献时请说明：

1. 使用的 Agent 或模型；
2. 触发问题的最小提示词；
3. 实际观察到的行为；
4. 期望行为和可复现方式。

## 贡献者与致谢

- **sgadfadjfads-cloud**：项目创建者与维护者。
- **OpenAI Codex**：AI 辅助开发与审查支持，不是法律意义上的版权持有人。

Preflight 的设计受到 Agent 工具社区的启发，尤其参考了 [AGENTS.md 格式](https://github.com/openai/agents.md)、[obra/superpowers](https://github.com/obra/superpowers)、[problem-statement](https://www.skills.sh/open-horizon-labs/skills/problem-statement) 和 [asking-clarifying-questions](https://eliteai.tools/agent-skills/asking-clarifying-questions)。这些项目及其作者属于参考和致谢来源，不是本仓库声称的实际贡献者。

## 许可证

MIT，详见 [`LICENSE`](LICENSE)。
