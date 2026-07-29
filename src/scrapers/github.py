"""GitHub scraper implementation."""

import logging
import os
from datetime import datetime, timedelta, timezone
from typing import List, Optional
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, GitHubSourceConfig

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    """Scraper for GitHub events, releases, and repository discovery."""

    def __init__(self, sources: List[GitHubSourceConfig], http_client: httpx.AsyncClient):
        """Initialize GitHub scraper.

        Args:
            sources: List of GitHub source configurations
            http_client: Shared async HTTP client
        """
        super().__init__({"sources": sources}, http_client)
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"

    def _get_headers(self) -> dict:
        """Get request headers with optional authentication.

        Returns:
            dict: HTTP headers
        """
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Horizon-Aggregator"
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch GitHub content items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        seen_search_repositories: set[str] = set()
        sources = self.config["sources"]

        for source in sources:
            if not source.enabled:
                continue

            if source.type == "user_events" and source.username:
                user_items = await self._fetch_user_events(source, since)
                items.extend(user_items)
            elif source.type == "repo_releases" and source.owner and source.repo:
                release_items = await self._fetch_repo_releases(source, since)
                items.extend(release_items)
            elif source.type == "repo_search" and source.query:
                search_items = await self._fetch_repository_search(source, since)
                for item in search_items:
                    repo_name = str(item.metadata.get("repo", "")).lower()
                    if repo_name and repo_name in seen_search_repositories:
                        continue
                    if repo_name:
                        seen_search_repositories.add(repo_name)
                    items.append(item)

        return items

    async def _fetch_repository_search(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Find popular repositories matching a configurable GitHub query."""
        cutoff = since
        if cutoff.tzinfo is None:
            cutoff = cutoff.replace(tzinfo=timezone.utc)
        else:
            cutoff = cutoff.astimezone(timezone.utc)

        if source.lookback_days is not None:
            cutoff = datetime.now(timezone.utc) - timedelta(days=source.lookback_days)

        query_parts = [
            source.query.strip(),
            f"pushed:>={cutoff:%Y-%m-%d}",
            "archived:false",
        ]
        if source.min_stars:
            query_parts.append(f"stars:>={source.min_stars}")

        params = {
            "q": " ".join(query_parts),
            "sort": source.sort,
            "order": source.order,
            "per_page": source.fetch_limit,
        }

        try:
            response = await self.client.get(
                f"{self.base_url}/search/repositories",
                params=params,
                headers=self._get_headers(),
                follow_redirects=True,
            )
            response.raise_for_status()
            repositories = response.json().get("items", [])
        except httpx.HTTPError as e:
            logger.warning("Error searching GitHub repositories for %r: %s", source.query, e)
            return []

        items: List[ContentItem] = []
        for repository in repositories:
            item = self._parse_repository(repository, source)
            if item is None or item.published_at < cutoff:
                continue
            items.append(item)
        return items

    def _parse_repository(
        self,
        repository: dict,
        source: GitHubSourceConfig,
    ) -> Optional[ContentItem]:
        """Convert a GitHub repository search result into a content item."""
        repo_id = repository.get("id")
        full_name = repository.get("full_name")
        html_url = repository.get("html_url")
        pushed_at_raw = repository.get("pushed_at")
        if not repo_id or not full_name or not html_url or not pushed_at_raw:
            return None

        try:
            pushed_at = datetime.fromisoformat(pushed_at_raw.replace("Z", "+00:00"))
        except (TypeError, ValueError):
            return None

        stars = int(repository.get("stargazers_count") or 0)
        forks = int(repository.get("forks_count") or 0)
        open_issues = int(repository.get("open_issues_count") or 0)
        topics = [str(topic) for topic in repository.get("topics") or []]
        language = repository.get("language")
        description = (repository.get("description") or "").strip()

        content_lines = [
            f"Popular GitHub repository: {full_name}",
            f"Stars: {stars}",
            f"Forks: {forks}",
            f"Open issues: {open_issues}",
            f"Primary language: {language or 'Unknown'}",
            f"Recently pushed: {pushed_at.isoformat()}",
        ]
        if topics:
            content_lines.append(f"Topics: {', '.join(topics)}")
        if description:
            content_lines.extend(["", description])

        owner = repository.get("owner") or {}
        return ContentItem(
            id=self._generate_id("github", "repository-search", str(repo_id)),
            source_type=SourceType.GITHUB,
            title=f"{full_name} ({stars:,}★)",
            url=html_url,
            content="\n".join(content_lines),
            author=owner.get("login") or full_name.split("/", 1)[0],
            published_at=pushed_at,
            metadata={
                "repo": full_name,
                "stars": stars,
                "forks": forks,
                "open_issues": open_issues,
                "language": language,
                "topics": topics,
                "search_query": source.query,
                "category": source.category,
            },
        )

    async def _fetch_user_events(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Fetch public events for a user.

        Args:
            source: GitHub source configuration
            since: Only fetch events after this time

        Returns:
            List[ContentItem]: Event content items
        """
        url = f"{self.base_url}/users/{source.username}/events/public"
        items = []

        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            response.raise_for_status()
            events = response.json()

            for event in events:
                created_at = datetime.fromisoformat(
                    event["created_at"].replace("Z", "+00:00")
                )

                if created_at < since:
                    continue

                # Filter interesting event types
                event_type = event["type"]
                if event_type not in [
                    "PushEvent", "CreateEvent", "ReleaseEvent",
                    "PublicEvent", "WatchEvent"
                ]:
                    continue

                item = self._parse_event(event, source)
                if item:
                    items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching GitHub events for %s: %s", source.username, e)

        return items

    def _parse_event(self, event: dict, source: GitHubSourceConfig) -> Optional[ContentItem]:
        """Parse GitHub event into ContentItem.

        Args:
            event: GitHub event data
            username: GitHub username

        Returns:
            Optional[ContentItem]: Parsed content item or None
        """
        event_type = event["type"]
        event_id = event["id"]
        created_at = datetime.fromisoformat(event["created_at"].replace("Z", "+00:00"))
        username = source.username

        repo_name = event["repo"]["name"]
        repo_url = f"https://github.com/{repo_name}"

        # Generate title and content based on event type
        if event_type == "PushEvent":
            commits = event["payload"].get("commits", [])
            title = f"{username} pushed {len(commits)} commit(s) to {repo_name}"
            content = "\n".join([c.get("message", "") for c in commits[:3]])
        elif event_type == "CreateEvent":
            ref_type = event["payload"].get("ref_type", "repository")
            title = f"{username} created {ref_type} in {repo_name}"
            content = event["payload"].get("description", "")
        elif event_type == "ReleaseEvent":
            release = event["payload"].get("release", {})
            title = f"{username} released {release.get('tag_name', '')} in {repo_name}"
            content = release.get("body", "")
            repo_url = release.get("html_url", repo_url)
        elif event_type == "PublicEvent":
            title = f"{username} made {repo_name} public"
            content = ""
        elif event_type == "WatchEvent":
            title = f"{username} starred {repo_name}"
            content = ""
        else:
            return None

        return ContentItem(
            id=self._generate_id("github", "event", event_id),
            source_type=SourceType.GITHUB,
            title=title,
            url=repo_url,
            content=content,
            author=username,
            published_at=created_at,
            metadata={
                "event_type": event_type,
                "repo": repo_name,
                "category": source.category,
            }
        )

    async def _fetch_repo_releases(
        self,
        source: GitHubSourceConfig,
        since: datetime,
    ) -> List[ContentItem]:
        """Fetch releases for a repository.

        Args:
            source: GitHub source configuration
            since: Only fetch releases after this time

        Returns:
            List[ContentItem]: Release content items
        """
        owner, repo = source.owner, source.repo
        url = f"{self.base_url}/repos/{owner}/{repo}/releases"
        items = []

        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            response.raise_for_status()
            releases = response.json()

            for release in releases:
                published_at = datetime.fromisoformat(
                    release["published_at"].replace("Z", "+00:00")
                )

                if published_at < since:
                    continue

                item = ContentItem(
                    id=self._generate_id("github", "release", str(release["id"])),
                    source_type=SourceType.GITHUB,
                    title=f"{owner}/{repo} released {release['tag_name']}",
                    url=release["html_url"],
                    content=release.get("body", ""),
                    author=release["author"]["login"],
                    published_at=published_at,
                    metadata={
                        "repo": f"{owner}/{repo}",
                        "tag": release["tag_name"],
                        "prerelease": release.get("prerelease", False),
                        "category": source.category,
                    }
                )
                items.append(item)

        except httpx.HTTPError as e:
            logger.warning("Error fetching releases for %s/%s: %s", owner, repo, e)

        return items
