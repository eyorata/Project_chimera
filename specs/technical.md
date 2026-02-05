# Project Chimera — Technical Specification

## 1. Architectural Overview
Project Chimera is an autonomous influencer infrastructure platform built as a **Hierarchical Swarm** of agents using the **Planner–Worker–Judge** pattern.

The goal is to build a repository that is stable enough for large-scale agent collaboration, where intent is driven by specifications and reliability is enforced by infrastructure.

This project is not designed as a prompt-driven prototype. It is designed as a governed, testable, scalable agentic system.

---

## 2. Core Architectural Principles

### 2.1 Spec-Driven Development (SDD)
- Specs are the source of truth.
- Implementation must be traceable to `specs/`.
- Ambiguity is treated as a bug.

### 2.2 Governance-First Infrastructure
- Agents must operate inside strict boundaries.
- Unsafe or low-confidence outputs must not reach production systems.
- Validation and approvals are part of the system, not optional add-ons.

### 2.3 MCP as the Integration Boundary
Agents must never call external APIs directly.
All external integrations must be routed through MCP servers.

This prevents agent logic from breaking when platform APIs change.

---

## 3. Agent System Design (Planner–Worker–Judge)

### 3.1 Planner Agent
Responsibilities:
- Ingest trend signals (via MCP tools or skills)
- Generate a content plan
- Decompose objectives into atomic tasks
- Dispatch tasks to workers
- Retry failed tasks or re-plan pipelines

Output Type:
- structured task graph / pipeline plan

---

### 3.2 Worker Agents
Responsibilities:
- Execute isolated tasks such as:
  - trend normalization
  - script writing
  - video generation
  - metadata generation
  - publishing requests (through MCP only)
- Produce structured JSON outputs only
- Never commit final publishing actions without Judge approval

Output Type:
- structured artifacts (JSON + media files)

---

### 3.3 Judge Agent (Governance Layer)
Responsibilities:
- Validate Worker outputs against:
  - format requirements
  - safety policies
  - spec-defined constraints
- Decide approve/reject for publishing
- Trigger Human-in-the-Loop escalation when needed

The Judge layer is the official **Safety Layer**.

Output Type:
- approval decision + structured validation report

---

## 4. Pipeline Orchestration Model

### 4.1 Execution Flow
The pipeline is event-driven and supports retries.

Typical execution pipeline:

1. Planner requests trend signals
2. Workers fetch + normalize trends
3. Planner selects a content direction and generates a content plan
4. Workers generate scripts and media artifacts
5. Judge validates outputs and enforces safety constraints
6. Human approves if required (escalation path)
7. Workers publish content via MCP connector
8. Metadata and logs are persisted into database

---

### 4.2 Retry Strategy
Retry-based recovery is allowed and expected.

If a Worker fails:
- Planner may retry the same Worker task
- Planner may assign the task to another Worker
- Planner may re-plan the pipeline entirely

Failure must not cascade across the entire system.

---

## 5. External Integration Strategy (MCP)

### 5.1 Hard Constraint
Agent code MUST NOT call external APIs directly.

All external integrations must go through MCP servers, such as:
- YouTube/TikTok/Instagram connectors
- OpenClaw network connector
- database connector
- filesystem/media storage connector

MCP acts as the stable interface boundary.

---

## 6. API Contracts (JSON Input/Output)

### 6.1 Trend Fetch Request
```json
{
  "platform": "youtube",
  "region": "US",
  "category": "gaming",
  "limit": 20
}


6.2 Trend Fetch Response
{
  "platform": "youtube",
  "region": "US",
  "timestamp": "2026-02-05T12:00:00Z",
  "trends": [
    {
      "id": "abc123",
      "title": "Example Trend",
      "url": "https://example.com",
      "score": 0.91,
      "tags": ["gaming", "viral"]
    }
  ]
}

6.3 Content Plan Output (Planner → Workers)
{
  "plan_id": "plan_001",
  "topic": "AI Influencers",
  "content_type": "short_video",
  "tasks": [
    {
      "task_id": "task_script",
      "type": "generate_script",
      "input": {
        "tone": "cinematic",
        "length_seconds": 45
      }
    },
    {
      "task_id": "task_video",
      "type": "generate_video",
      "input": {
        "style": "nature",
        "duration_seconds": 8
      }
    }
  ]
}

6.4 Script Generation Output (Worker → Judge)
{
  "script_id": "script_001",
  "title": "The Future of AI Influencers",
  "hook": "What if your favorite influencer wasn't human?",
  "voiceover_text": "Full narration here...",
  "hashtags": ["#AI", "#Future", "#Tech"],
  "risk_flags": []
}

6.5 Publishing Request (Worker → MCP)
{
  "platform": "tiktok",
  "video_path": "exports/video_001.mp4",
  "caption": "The future is here. #AI #Tech",
  "metadata": {
    "topic": "AI Influencers",
    "plan_id": "plan_001"
  }
}

6.6 Publishing Response
{
  "success": true,
  "platform": "tiktok",
  "post_id": "post_8823",
  "url": "https://tiktok.com/@chimera/video/8823",
  "timestamp": "2026-02-05T12:10:00Z"
}

7. Database Design (NoSQL-First)
7.1 Rationale

Project Chimera is expected to handle high-velocity metadata such as:

content generation logs

trend signals

engagement signals

asset metadata

publishing history

A NoSQL database is recommended because:

schema evolves rapidly

write throughput is high

metadata structures are nested and flexible

horizontal scaling is easier for swarm workloads

7.2 Proposed Collections
influencers
{
  "_id": "chimera_001",
  "name": "ChimeraAlpha",
  "persona": {
    "tone": "cinematic",
    "topics": ["tech", "AI", "future"]
  },
  "created_at": "2026-02-05T00:00:00Z"
}

trend_signals
{
  "_id": "trend_001",
  "platform": "youtube",
  "region": "US",
  "timestamp": "2026-02-05T12:00:00Z",
  "trends": []
}

content_plans
{
  "_id": "plan_001",
  "topic": "AI Influencers",
  "status": "approved",
  "tasks": [],
  "created_at": "2026-02-05T12:01:00Z"
}

generated_assets
{
  "_id": "asset_001",
  "type": "video",
  "path": "exports/video_001.mp4",
  "duration_seconds": 8,
  "file_size_bytes": 10485760,
  "created_at": "2026-02-05T12:05:00Z"
}

audit_logs
{
  "_id": "log_001",
  "agent_role": "worker",
  "action": "generate_script",
  "input": {},
  "output": {},
  "timestamp": "2026-02-05T12:03:00Z"
}

8. ERD (Mermaid Diagram)
erDiagram
    INFLUENCERS ||--o{ CONTENT_PLANS : owns}
    CONTENT_PLANS ||--o{ GENERATED_ASSETS : produces}
    CONTENT_PLANS ||--o{ AUDIT_LOGS : logs}
    TREND_SIGNALS ||--o{ CONTENT_PLANS : informs}

    INFLUENCERS {
        string _id
        string name
        json persona
        datetime created_at
    }

    TREND_SIGNALS {
        string _id
        string platform
        string region
        datetime timestamp
        json trends
    }

    CONTENT_PLANS {
        string _id
        string topic
        string status
        json tasks
        datetime created_at
    }

    GENERATED_ASSETS {
        string _id
        string type
        string path
        int duration_seconds
        int file_size_bytes
        datetime created_at
    }

    AUDIT_LOGS {
        string _id
        string agent_role
        string action
        json input
        json output
        datetime timestamp
    }

9. Testing Requirements (TDD Alignment)

This project must follow strict Test-Driven Development.

Before implementing real logic, the repository must contain failing tests that define:

trend API contract compliance

skill input/output interface compliance

publishing contract validation

governance decision logic expectations

Failing tests are considered success at the specification stage because they define the target behavior that future agent swarms must implement.

10. Summary

Project Chimera is designed as a governed agent platform.

Key technical goals:

scale to swarm execution

isolate volatility through MCP

enforce safety through Judge governance

maintain traceability through specs and logs

support rapid evolution through NoSQL storage and modular skill contracts