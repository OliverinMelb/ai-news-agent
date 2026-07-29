"""Tests for GitHub repository hotspot discovery."""

import asyncio
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, Mock

import pytest
from pydantic import ValidationError

from src.models import GitHubSourceConfig
from src.scrapers.github import GitHubScraper


def _repository(
    *,
    repo_id: int = 123,
    full_name: str = "mattpocock/skills",
    pushed_at: datetime | None = None,
) -> dict:
    pushed_at = pushed_at or datetime.now(timezone.utc) - timedelta(hours=1)
    return {
        "id": repo_id,
        "full_name": full_name,
        "html_url": f"https://github.com/{full_name}",
        "description": "Skills for real engineers",
        "pushed_at": pushed_at.isoformat().replace("+00:00", "Z"),
        "stargazers_count": 170_000,
        "forks_count": 4_200,
        "open_issues_count": 18,
        "language": "TypeScript",
        "topics": ["agent-skills", "claude-code"],
        "owner": {"login": full_name.split("/", 1)[0]},
    }


def _response(items: list[dict]) -> Mock:
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"items": items}
    return response


def test_repository_search_builds_hotspot_query_and_metadata():
    client = AsyncMock()
    client.get.return_value = _response([_repository()])
    source = GitHubSourceConfig(
        type="repo_search",
        query="skills in:name,description,readme",
        min_stars=500,
        fetch_limit=25,
        lookback_days=7,
        category="skills-hotspot",
    )

    items = asyncio.run(
        GitHubScraper([source], client).fetch(
            datetime.now(timezone.utc) - timedelta(hours=24)
        )
    )

    assert len(items) == 1
    assert items[0].metadata["repo"] == "mattpocock/skills"
    assert items[0].metadata["stars"] == 170_000
    assert items[0].metadata["category"] == "skills-hotspot"
    assert "Stars: 170000" in items[0].content

    params = client.get.await_args.kwargs["params"]
    assert params["sort"] == "stars"
    assert params["per_page"] == 25
    assert "stars:>=500" in params["q"]
    assert "archived:false" in params["q"]
    assert "pushed:>=" in params["q"]


def test_overlapping_repository_searches_are_deduplicated():
    client = AsyncMock()
    client.get.side_effect = [
        _response([_repository()]),
        _response([_repository()]),
    ]
    sources = [
        GitHubSourceConfig(type="repo_search", query="skills", category="first"),
        GitHubSourceConfig(type="repo_search", query="agent skills", category="second"),
    ]

    items = asyncio.run(
        GitHubScraper(sources, client).fetch(
            datetime.now(timezone.utc) - timedelta(hours=24)
        )
    )

    assert len(items) == 1
    assert items[0].metadata["category"] == "first"


def test_repository_search_config_rejects_invalid_bounds():
    with pytest.raises(ValidationError):
        GitHubSourceConfig(type="repo_search", query="skills", fetch_limit=101)

    with pytest.raises(ValidationError):
        GitHubSourceConfig(type="repo_search", query="skills", lookback_days=0)
