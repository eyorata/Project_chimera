"""Contract test: unsupported platform must raise an explicit exception.

This enforces the failure mode from `specs/skill_fetch_trends.md`:
"Input validation errors (bad `platform`/`region`) -> raise `ValueError`."

The current minimal implementation does not perform this validation, so
this test is expected to fail (RED) until validation is added.
"""

import pytest
from importlib import import_module


def test_fetch_trends_raises_on_unsupported_platform():
    """If an unsupported platform is passed, the skill must raise ValueError.

    The exception message should clearly indicate the platform is unsupported.
    """
    mod = import_module("skills.skill_fetch_trends")
    assert hasattr(mod, "fetch_trends"), "skill module must expose `fetch_trends`"
    fetch_trends = getattr(mod, "fetch_trends")

    with pytest.raises(ValueError, match=r"(?i)unsupported|not supported"):
        fetch_trends(platform="unsupported_platform", region="US", limit=1)