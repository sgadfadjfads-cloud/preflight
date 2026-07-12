# Preflight

A vendor-neutral behavior protocol for AI agents that helps them understand the real problem before acting.

## Why this exists

Agents can complete the visible request while missing the user's actual goal, hidden constraints, authorization boundary, or definition of success. Preflight adds a lightweight check before meaningful action:

- simple tasks stay simple;
- ambiguous work surfaces the decisions that matter;
- risks are explained instead of silently ignored;
- protected boundaries are not crossed by assumption;
- multi-turn changes trigger recalibration;
- the mechanism stays implicit unless the user asks about it.

This is an instruction-level protocol, not a runtime enforcement or safety system. Platform policies, system instructions, explicit user constraints, and application authorization remain higher-priority controls.

## Contents

- [`SKILL.md`](SKILL.md): reusable Skill for Skill-aware agents.
- [`AGENTS.md`](AGENTS.md): copyable global/project instruction template for activation at task and material scope-change boundaries.
- [`tests/cases.md`](tests/cases.md): observable pressure cases.
- [`tests/validate_skill.py`](tests/validate_skill.py): deterministic package checks.
- [`tests/evaluate_response.py`](tests/evaluate_response.py): conservative checks for saved agent responses.

## Installation

### Skill-aware agents

Install or copy this repository as a Skill, preserving `SKILL.md` and `agents/openai.yaml` in the Skill package directory. The Skill is intended for tasks where the request may hide important goals, constraints, risks, authorization boundaries, success conditions, or unresolved assumptions.

### Global activation

Copy the contents of [`AGENTS.md`](AGENTS.md) into the global or project-level instruction file supported by your agent. Use this when you want the protocol to run for every new task and to re-run when a follow-up materially changes the task frame.

### Both

Use the Skill for the reusable detailed guidance and the template for task-boundary activation. Keep only one authoritative copy of the template in your environment to avoid contradictory instruction variants.

## Example behavior

For “Build a customer export for CSV, Excel, and JSON today,” an agent should not invent fields, permissions, or deployment approval. It should identify the audience, data scope, authorization, success condition, risks, and the smallest unresolved decisions before implementation.

For “Fix this typo,” it should make the correction directly without a full requirements interview.

## Validation

Run:

```bash
python3 tests/validate_skill.py
python3 <your-agent-skill-validator>/quick_validate.py .
```

Then use the prompts in [`tests/cases.md`](tests/cases.md) with and without the Skill and compare observable behavior. Prompt tests measure behavior; they do not prove deterministic enforcement across all models.

To run a conservative check against a saved response:

```bash
python3 tests/evaluate_response.py ambiguous-feature response.txt
```

The evaluator checks observable concepts and obvious violations only. It is intentionally not a semantic judge and should be supplemented by human review.

## Design principles

Deep judgment, concise complete communication, transparent risk reasoning, explicit authorization boundaries, and no private chain-of-thought disclosure.

## License

MIT. See [`LICENSE`](LICENSE).
