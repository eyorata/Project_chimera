# Project Chimera — Agent Rules (CLAUDE.md)

## Project Context
This repository is **Project Chimera**, an **Autonomous Influencer Network** system.
The goal is to build a robust agentic infrastructure where autonomous AI agents can:
- fetch trends
- generate scripts/content
- generate media
- publish content
- monitor engagement
- operate with governance and traceability

This project is NOT a prototype. It is an engineering-grade foundation for scaling autonomous agents.

---

## Prime Directive (Non-Negotiable)
🚨 **NEVER generate or modify implementation code unless you have first read and aligned with the specs in `specs/`.**

All code must trace back to:
- `specs/_meta.md`
- `specs/functional.md`
- `specs/technical.md`
- `specs/openclaw_integration.md` (if present)

If a spec is unclear, STOP and request clarification.

---

## Architecture Mandate
This project follows a **Hierarchical Swarm Architecture** (Planner–Worker–Judge).

- **Planner Agent**
  - breaks down goals into tasks
  - assigns tasks to workers
  - produces structured plans

- **Worker Agents**
  - execute isolated tasks (fetch trends, generate scripts, create captions, etc.)
  - do not make final publishing decisions

- **Judge Agent**
  - validates outputs against safety rules, specs, and policy
  - can require human approval
  - rejects unsafe/low-confidence output

Human-in-the-loop approval happens at the Judge layer.

---

## Required Behavior Before Writing Code
Before writing code, always:
1. Summarize the relevant spec sections.
2. Explain the plan clearly in bullet points.
3. Confirm which files will be created/modified.
4. Only then write code.

---

## Spec-Driven Development Rules
All development must follow this order:

1. Spec exists in `specs/`
2. Tests are written in `tests/` (TDD, tests can fail initially)
3. Implementation code is written in `src/`
4. CI/CD validates tests and linting

No step skipping.

---

## Output Format Rules
When responding with technical output:
- Prefer structured bullet points
- Prefer JSON schemas for contracts
- Prefer explicit function signatures
- Avoid vague statements like “should work”
- Always include assumptions and edge cases

---

## Traceability Requirements
Every new feature must include:
- reference to the spec requirement it satisfies
- tests validating the behavior
- clear logging or output artifacts

If the agent cannot trace a requirement → it must not proceed.

---

## Security & Safety Requirements
This project may eventually handle:
- social media credentials
- API keys
- external publishing permissions

Rules:
- NEVER hardcode API keys
- NEVER print secrets to logs
- Use `.env` and environment variables only
- Always assume all external inputs are untrusted

---

## Git Hygiene Rules
- Commit early, commit often
- Commit messages must be descriptive
- Each commit should represent one meaningful improvement

Example:
✅ "Add API contract schema for trend fetcher"
❌ "update"

---

## Code Quality Expectations
All Python code must:
- follow typing (`typing`, `pydantic`, dataclasses if needed)
- be testable
- avoid tight coupling to external APIs
- isolate integrations behind skill interfaces

---

## Summary
Project Chimera is built for long-term reliability, auditability, and scale.
Specs are the source of truth.
Infrastructure and governance matter more than quick outputs.
