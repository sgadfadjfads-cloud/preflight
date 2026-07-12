# Contributing to Preflight

Thanks for helping improve Preflight.

## What to contribute

The most useful contributions are:

- pressure cases that expose action-first behavior or stale assumptions;
- compatibility feedback from different agents and models;
- clearer installation and integration examples;
- small, evidence-backed improvements to the protocol.

## Issue reports

Include:

1. Agent and model;
2. the smallest prompt that reproduces the behavior;
3. relevant Skill/template version;
4. observed response or action;
5. expected behavior and why it matters.

Do not include secrets, private prompts, customer data, or sensitive repository contents.

## Pull requests

- Keep one behavioral change per PR.
- Add or update an observable pressure case when changing protocol behavior.
- Run `python3 tests/validate_skill.py`.
- Run `git diff --check`.
- Explain what the change improves and what it does not prove.

Preflight is an instruction-level protocol. Pull requests should improve clarity and transferability without claiming deterministic enforcement that the tests cannot demonstrate.
