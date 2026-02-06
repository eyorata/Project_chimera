# Skill: fetch_trends — Behavioral Contract

Reference: derived from `specs/functional.md` (Trend Discovery) and
`specs/technical.md` (API Contracts).

## Purpose
Provide a deterministic, testable skill that fetches trending items from a
platform via MCP connectors and returns a structured JSON artifact for the
Planner to consume.

## Location
Module path: `skills.skill_fetch_trends`
Callable: `fetch_trends`

## Input (parameters)
- `platform` (str, required): provider identifier, e.g., `youtube`, `tiktok`.
- `region` (str, required): region code, e.g., `US`, `GB`.
- `category` (str, optional): content category, e.g., `gaming`.
- `limit` (int, optional, default=20): maximum number of trends to return.

Implementations MUST accept these as either positional or keyword args.

## Output (successful)
Return type: `dict` with the following keys:

- `platform` (str) — echoes input platform
- `region` (str) — echoes input region
- `timestamp` (str) — ISO8601 UTC timestamp of fetch operation
- `trends` (list) — list of trend items; each item is a dict with:
  - `id` (str)
  - `title` (str)
  - `url` (str)
  - `score` (float) — normalized 0.0..1.0 relevance score
  - `tags` (list[str]) — list of string tags/keywords

Example:

```
{
  "platform": "youtube",
  "region": "US",
  "timestamp": "2026-02-05T12:00:00Z",
  "trends": [
    {"id":"abc123","title":"Example","url":"https://...","score":0.91,"tags":["gaming"]}
  ]
}
```

## Failure Modes and Errors
- Input validation errors (bad `platform`/`region`) -> raise `ValueError`.
- Temporary MCP/integration failure -> raise `IntegrationError` (implementation-defined), or propagate a subclass of `Exception` that clearly indicates transient failure.
- Unimplemented skill: may raise `NotImplementedError` until implemented.

## Non-Functional Requirements
- No direct external API calls — all external access MUST go through MCP connectors.
- Structured logging and traceability: implementations must log `agent_id`, `action`, `input`, and `output` per FR-001.

## Testing Guidance
- Unit tests should verify signature conformity and output schema (see
  tests/unit/test_failing.py).
- Integration tests should exercise MCP connectors via mocks.
