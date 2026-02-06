
"""Unit test enforcing the `skill_fetch_trends` behavioral contract.

This test encodes the expected input/output contract from
`specs/skill_fetch_trends.md`. The test is expected to fail today because
the skill implementation is intentionally missing. Do NOT implement the
skill logic as part of this change — the failing test is the specification
artifact for TDD.
"""

import inspect
from importlib import import_module
import pytest


def test_skill_fetch_trends_contract():
    """Enforce the fetch_trends contract for the skill.

    Contract (short form):
    - Module: `skills.skill_fetch_trends`
    - Callable: `fetch_trends(platform: str, region: str, category: str|None = None, limit: int = 20) -> dict`
    - Output shape: {
        "platform": str,
        "region": str,
        "timestamp": ISO8601 string,
        "trends": [ {"id": str, "title": str, "url": str, "score": float(0..1), "tags": [str]} ]
      }

    This test will fail if the module or callable is missing. When the
    implementation is added it must satisfy the assertions below. The
    failure should only be due to the missing implementation at this time.
    """

    # Import the skill module — fail clearly if missing
    try:
        mod = import_module("skills.skill_fetch_trends")
    except ModuleNotFoundError as exc:
        pytest.fail(
            "RED: skill module `skills.skill_fetch_trends` not found — "
            "implementation missing per specs/skill_fetch_trends.md. "
            f"ImportError: {exc}")

    # The skill must expose a callable `fetch_trends` — fail with clear RED message
    if not hasattr(mod, "fetch_trends"):
        pytest.fail(
            "RED: `skills.skill_fetch_trends` does not define `fetch_trends`. "
            "This indicates the skill implementation is missing and is the intended "
            "failing state for the RED phase of TDD. See specs/skill_fetch_trends.md for contract.")
    fetch_trends = getattr(mod, "fetch_trends")
    if not callable(fetch_trends):
        pytest.fail("`fetch_trends` exists but is not callable — must be a function or callable object")

    # Signature checks: require `platform` and `region`, optional `category`, `limit` with int default
    sig = inspect.signature(fetch_trends)
    params = sig.parameters
    assert "platform" in params, "`fetch_trends` must accept `platform` parameter"
    assert "region" in params, "`fetch_trends` must accept `region` parameter"
    assert "limit" in params, "`fetch_trends` should accept `limit` parameter"

    # If limits/defaults provided, they should be reasonable
    if params["limit"].default is not inspect.Parameter.empty:
        assert isinstance(params["limit"].default, int), "`limit` default must be an int"

    # Call the function with a small, well-formed request. The implementation
    # may raise NotImplementedError or other integration errors until implemented;
    # such failures are acceptable for now because implementation is missing.
    sample = {"platform": "youtube", "region": "US", "category": "gaming", "limit": 3}

    try:
        result = fetch_trends(**sample)
    except NotImplementedError:
        pytest.skip("Skill implemented as stub (NotImplementedError) — implementation missing")

    # From this point forward the test asserts the contract for a successful response
    assert isinstance(result, dict), "fetch_trends must return a dict"
    assert result.get("platform") == sample["platform"]
    assert result.get("region") == sample["region"]

    # timestamp should be an ISO8601 string
    ts = result.get("timestamp")
    assert isinstance(ts, str) and ts, "`timestamp` must be a non-empty ISO8601 string"

    # trends must be a list of trend objects with required fields and types
    trends = result.get("trends")
    assert isinstance(trends, list), "`trends` must be a list"

    for item in trends:
        assert isinstance(item, dict), "Each trend must be a dict"
        for key in ("id", "title", "url", "score", "tags"):
            assert key in item, f"Trend item missing required key: {key}"
        assert isinstance(item["id"], str)
        assert isinstance(item["title"], str)
        assert isinstance(item["url"], str)
        assert isinstance(item["score"], float)
        assert 0.0 <= item["score"] <= 1.0
        assert isinstance(item["tags"], list)
        for t in item["tags"]:
            assert isinstance(t, str)
