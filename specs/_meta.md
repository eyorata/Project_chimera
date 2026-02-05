# Project Chimera - Specification Meta

## Vision
Project Chimera is an autonomous AI influencer system designed to operate with minimal human intervention. The system will research trends, generate content ideas, produce scripts, and coordinate publishing workflows across social media platforms.

The goal is not to build a single AI bot, but to build a robust agentic infrastructure ("the Factory") that can reliably produce autonomous influencer agents.

This repository is designed for Spec-Driven Development (SDD), where the specification is the source of truth and implementation must always trace back to the specs.

---

## Business Objective
The business objective is to create a scalable infrastructure where AI agents can:
- Fetch and analyze trending content
- Generate engaging influencer-style scripts
- Generate or coordinate multimedia creation (audio/video/images)
- Publish content to platforms
- Track engagement metrics and iterate

The system must be resilient, auditable, and suitable for future AI agent swarms.

---

## Core Constraints
### Spec-Driven Development (SDD)
- Specs are the source of truth.
- No implementation code should be written unless aligned with the specs/ directory.
- All major components must have explicit API contracts.

### Traceability (MCP Sense Requirement)
- Tenx MCP Sense must remain connected to the IDE during development.
- Agent actions and developer changes must be traceable.

### Reliability and Governance
- The system must include:
  - structured logging
  - validation of agent outputs
  - safety checks
  - human-in-the-loop approval checkpoints
  - test-first development

---

## Non-Goals (Out of Scope for Phase 1)
This project will NOT initially focus on:
- building a polished UI dashboard
- real-time human chat engagement automation
- scaling to millions of posts per day
- direct monetization integrations

---

## Key Principles
- Deterministic workflows over prompt hacking
- Structured JSON contracts instead of free-form prompts
- Modular skills-based architecture
- Safe-by-default publishing workflows
- Clear separation of development tooling vs runtime agent skills

---

## Success Criteria
This repository is considered successful if:
- A swarm of agents can enter the repo and build features without ambiguity.
- The system has specs, skills contracts, tests, CI/CD, and containerization.
- Implementation can be done safely by AI agents with minimal hallucination.

---

## Assumptions
- Primary language: Python 3.11+
- Package manager: uv
- Storage: SQL database (Postgres recommended)
- Orchestration: skill-based runtime agent design
- CI/CD: GitHub Actions
- Governance: automated review + tests + linting
