"""Tests for `bot_jobs` package."""

import pytest

from bot_jobs import discordbot


@pytest.mark.parametrize(
    "owner,repo",
    [
        ("pytorch", "pytorch"),
    ],
)
def test_get_pull_requests(owner, repo):
    result = discordbot.get_pull_requests(owner, repo)
    assert result
