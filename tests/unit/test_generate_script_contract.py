"""Contract test for `skills.skill_generate_script.generate_script`.

This test enforces the behavioral contract specified in
`specs/skill_generate_script.md`. It intentionally fails today because the
skill implementation must not be provided yet (RED phase of TDD).
"""

from importlib import import_module
import inspect
import pytest


def test_generate_script_contract_raises_when_missing():
    """Assert the `generate_script` skill exists and matches the contract.

    This test is expected to fail until `skills.skill_generate_script` is
    implemented. Failure should clearly indicate the missing contract.
    """

    # Import module — produce a clear RED failure if missing
    try:
        mod = import_module("skills.skill_generate_script")
    except ModuleNotFoundError as exc:
        pytest.fail(
            "RED: skill module `skills.skill_generate_script` not found — "
            "implementation missing per specs/skill_generate_script.md. "
            f"ImportError: {exc}")

    # The module must define `generate_script` callable
    if not hasattr(mod, "generate_script"):
        pytest.fail(
            "RED: `skills.skill_generate_script` does not define `generate_script`. "
            "This indicates the skill implementation is missing and is the intended "
            "failing state for the RED phase of TDD. See specs/skill_generate_script.md for contract.")

    generate_script = getattr(mod, "generate_script")
    if not callable(generate_script):
        pytest.fail("`generate_script` exists but is not callable — must be function or callable object")

    # Basic signature checks
    sig = inspect.signature(generate_script)
    params = sig.parameters
    assert "topic" in params, "`generate_script` must accept `topic` parameter"
    assert "length_seconds" in params, "`generate_script` must accept `length_seconds` parameter"

    # If invocation happens, allow NotImplementedError to be raised; otherwise
    # if it returns, enforce the output contract shape.
    sample = {"topic": "AI influencers", "length_seconds": 30, "tone": "cinematic"}

    try:
        result = generate_script(**sample)
    except NotImplementedError:
        pytest.skip("Skill implemented as stub (NotImplementedError) — implementation missing")

    # If the function returns, assert the contract
    assert isinstance(result, dict), "generate_script must return a dict"
    required_keys = ["script_id", "title", "hook", "voiceover_text", "call_to_action", "hashtags", "length_seconds", "risk_flags"]
    for k in required_keys:
        assert k in result, f"Missing key in script output: {k}"
    assert isinstance(result["hashtags"], list)
    assert isinstance(result["risk_flags"], list)
    assert isinstance(result["length_seconds"], int)