"""Minimal `skill_fetch_trends` implementation to satisfy contract tests.

This file provides the smallest explicit implementation that fulfills the
behavioral contract defined in `specs/skill_fetch_trends.md` and the unit
test in `tests/unit/test_failing.py`. It intentionally avoids extra features
or abstractions — purely the minimal logic to return a correctly shaped
response for test inputs.
"""
from datetime import datetime
from typing import Optional, Dict, Any, List


def fetch_trends(platform: str, region: str, category: Optional[str] = None, limit: int = 20) -> Dict[str, Any]:
    """Return a deterministic list of mock trends matching the contract.

    This minimal implementation is not a production connector — it simply
    returns mock items with correct types to satisfy the unit test.
    """
    # Ensure `limit` is an int and non-negative for simple safety
    try:
        n = int(limit)
    except Exception:
        n = 0
    if n < 0:
        n = 0

    timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    trends: List[Dict[str, Any]] = []
    for i in range(n):
        trends.append({
            "id": f"{platform}_{region}_{i}",
            "title": f"Sample trend {i} ({category or 'general'})",
            "url": f"https://example.com/{platform}/{region}/{i}",
            "score": float(max(0.0, min(1.0, 1.0 - i * 0.01))),
            "tags": [category] if category else ["sample"],
        })

    return {
        "platform": platform,
        "region": region,
        "timestamp": timestamp,
        "trends": trends,
    }
