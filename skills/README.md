# Project Chimera — Skills Directory

## Overview
This directory defines the **runtime skills** that autonomous Chimera agents will use.

A skill is a reusable capability package that exposes a stable contract.

Skills are NOT MCP servers.
Skills are part of the product design and must remain consistent.

Each skill must define:
- purpose
- input schema (JSON contract)
- output schema (JSON contract)
- error format
- expected side effects

---

## Skill Design Principles
All skills must:
- accept structured JSON input
- return structured JSON output
- support deterministic outputs when possible
- never leak credentials
- log safely without exposing secrets
- be testable through unit tests

---

## Current Skills
The following skills are currently defined:

1. `skill_fetch_trends`
2. `skill_generate_script`
3. `skill_publish_video`

---

## Standard Skill Response Format
All skills must return responses in this format:

```json
{
  "success": true,
  "skill": "skill_name",
  "data": {},
  "error": null,
  "metadata": {
    "timestamp": "ISO-8601",
    "execution_time_ms": 1200
  }
}

On failure:

{
  "success": false,
  "skill": "skill_name",
  "data": null,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message"
  },
  "metadata": {
    "timestamp": "ISO-8601",
    "execution_time_ms": 1200
  }
}
