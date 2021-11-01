"""
Generated by generate/generate.py - 2020-08-02 12:25:07.157407
"""
from aiogithubapi.objects.repos.traffic.pageviews import (
    AIOGitHubAPIReposTrafficPageviews,
)

from tests.legacy.responses.repos.traffic.pageviews_fixtrue import (
    pageviews_fixtrue_response,
)


def test_pageviews(pageviews_fixtrue_response):
    obj = AIOGitHubAPIReposTrafficPageviews(pageviews_fixtrue_response)
    assert obj.count == pageviews_fixtrue_response["count"]
    assert obj.uniques == pageviews_fixtrue_response["uniques"]
    assert obj.views[0].timestamp == pageviews_fixtrue_response["views"][0]["timestamp"]
    assert obj.views[0].count == pageviews_fixtrue_response["views"][0]["count"]
    assert obj.views[0].uniques == pageviews_fixtrue_response["views"][0]["uniques"]