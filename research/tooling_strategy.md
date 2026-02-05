# Project Chimera — Tooling Strategy (MCP + Developer Tools)

## Purpose
This document defines the tooling strategy for Project Chimera, separating:

1. **Developer Tools (MCP Servers)**  
   Tools used by the developer during building, debugging, and repo management.

2. **Runtime Agent Skills**  
   Tools the Chimera agent itself will call during execution in production.

This separation is important because MCP servers are external bridges for development,
while skills are stable contracts used by autonomous agents.

---

## Developer Tools (MCP Servers)

### 1. filesystem-mcp
**Purpose:**  
Enable the agent/developer to read and modify repository files safely.

**Use Cases:**
- auto-writing specs into `specs/`
- generating README files
- editing test files
- modifying configuration files

**Why it matters:**  
Chimera is spec-driven, so file operations must be safe and traceable.

---

### 2. git-mcp
**Purpose:**  
Enable commit, diff, status inspection, and controlled repository evolution.

**Use Cases:**
- checking repo state before edits
- creating meaningful commits
- tracking changes across days

**Why it matters:**  
Commit history must tell the story of system growth and decision-making.

---

### 3. docker-mcp (optional)
**Purpose:**  
Assist with Docker builds, environment debugging, and container validation.

**Use Cases:**
- validate that Chimera works in Docker
- run tests in isolated environment

**Why it matters:**  
The system must not rely on “works on my machine.”

---

### 4. database-mcp (future optional)
**Purpose:**  
Bridge for schema testing and DB validation (MongoDB / NoSQL).

**Use Cases:**
- verify metadata schema correctness
- simulate production database queries

**Why it matters:**  
Chimera stores high velocity influencer metadata that must scale horizontally.

---

### 5. browser-mcp (optional)
**Purpose:**  
Support research and browsing tasks during development.

**Use Cases:**
- reading OpenClaw docs
- validating API endpoints
- gathering examples of influencer trends

---

## Runtime Skills (Agent Execution Layer)

### Design Rule
A skill is a **stable contract** that can be called by agents.

Skills should:
- accept structured JSON inputs
- return structured JSON outputs
- support error reporting
- be deterministic when possible
- isolate external integrations

Skills are NOT MCP servers.

---

## Skills vs MCP: Why the Separation Matters
MCP servers can change, break, or vary by developer environment.

Skills are part of the product architecture and must remain stable over time.

Therefore:
- MCP servers are development infrastructure
- Skills are production interfaces

---

## Recommended Runtime Skill Categories
The Chimera system requires skills in these categories:

### Trend & Research Skills
- fetch trends
- scrape topics
- summarize news
- rank hashtags

### Content Generation Skills
- generate scripts
- generate captions
- generate titles
- generate hashtags

### Media Production Skills
- generate video prompts
- generate audio prompts
- render assets
- edit clips

### Publishing Skills
- upload video
- schedule post
- update profile metadata

### Analytics Skills
- fetch engagement metrics
- track performance per platform

---

## Summary
The Chimera architecture is only scalable if the system distinguishes:
- developer-time tools (MCP servers)
- runtime skills (stable contracts)

This ensures agent reliability, testability, and long-term maintainability.
