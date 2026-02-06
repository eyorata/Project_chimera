# Skill: generate_script — Behavioral Contract

Reference: follows the same TDD and contract style as `specs/skill_fetch_trends.md`.

## Purpose
Generate short-form video scripts from trend-driven inputs so Worker agents
can produce consistent content. The skill is a pure function: it accepts a
structured input and returns a structured script artifact.

## Location
Module path: `skills.skill_generate_script`
Callable: `generate_script`

## Input (parameters)
- `topic` (str, required): concise topic or idea for the script.
- `tone` (str, optional): voice/tone indicator (e.g., `cinematic`, `funny`).
- `length_seconds` (int, required): desired script runtime in seconds.
- `platform` (str, optional): target platform to tune length/hook (e.g., `tiktok`).
- `metadata` (dict, optional): free-form additional context.

Implementations MUST accept these as positional or keyword args and validate types.

## Output (successful)
Return type: `dict` with keys:

- `script_id` (str): unique identifier
- `title` (str): short title suggestion
- `hook` (str): opening hook (short sentence)
- `voiceover_text` (str): the full narration/script
- `call_to_action` (str): short CTA
- `hashtags` (list[str]): suggested hashtags
- `length_seconds` (int): runtime in seconds (should match input or be within +/-2s)
- `risk_flags` (list[str]): empty list if no issues

Example:

```
{
  "script_id": "script_001",
  "title": "Why AI is the future",
  "hook": "What if your phone could think for you?",
  "voiceover_text": "Full script...",
  "call_to_action": "Follow for more",
  "hashtags": ["#AI", "#Future"],
  "length_seconds": 45,
  "risk_flags": []
}
```

## Failure Modes and Errors
- Invalid input types or missing required fields -> raise `ValueError`.
- Unsupported platform tuning -> raise `ValueError` with clear message.
- Temporary integration/system errors -> raise `IntegrationError` (implementation-defined).
- Unimplemented skill: may raise `NotImplementedError` until implemented.

## Non-Functional Requirements
- No external API calls from the skill; use MCP connectors for external integrations.

## Testing Guidance
- Unit tests should assert signature conformity and output shape.
- Tests should expect a failing RED state until implementation exists.
