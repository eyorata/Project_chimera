# import pytest
# from skills.skill_fetch_trends import run


# def test_fetch_trends_contract():
#     """
#     This test enforces the expected contract from specs/technical.md.
#     """

#     input_data = {"platform": "tiktok", "limit": 3}
#     result = run(input_data)

#     assert isinstance(result, dict)
#     assert "platform" in result
#     assert "generated_at" in result
#     assert "trends" in result

#     assert isinstance(result["platform"], str)
#     assert isinstance(result["generated_at"], str)
#     assert isinstance(result["trends"], list)

#     for trend in result["trends"]:
#         assert "rank" in trend
#         assert "topic" in trend
#         assert "score" in trend

#         assert isinstance(trend["rank"], int)
#         assert isinstance(trend["topic"], str)
#         assert isinstance(trend["score"], float)
