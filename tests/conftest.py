"""PyTest configuration."""

from itertools import starmap
from pathlib import Path

import pytest
from beartype import beartype
from beartype.typing import List
from calcipy.dot_dict import ddict
from commitizen import defaults, git
from commitizen.config.base_config import BaseConfig
from syrupy.extensions.json import JSONSnapshotExtension

from .configuration import TEST_TMP_CACHE, clear_test_cache
from .constants import ANSWERS, COMMITS_DATA, TAGS


@pytest.fixture()
def snapshot_json(snapshot):
    return snapshot.use_extension(JSONSnapshotExtension)


@pytest.fixture()
@beartype
def fix_test_cache() -> Path:
    """Fixture to clear and return the test cache directory for use.

    Returns
    -------
        Path: Path to the test cache directory

    """
    clear_test_cache()
    return TEST_TMP_CACHE


@pytest.fixture()
@beartype
def config() -> BaseConfig:
    """Create default configuration.

    Returns
    -------
        BaseConfig: base commitizen configuration

    """
    # https://github.com/commitizen-tools/commitizen/blob/7fce6670fdc44f994243babf37ba873f8c6ae587/commitizen/config/base_config.py#L8-L12
    _config = BaseConfig()
    _config.settings.update({'name': defaults.name})
    _config.settings.update({'cz_legacy_map': {'Chg': 'Change (Old)'}})  # type: ignore[misc] # pyright: ignore[reportCallIssue]
    return _config


@pytest.fixture(
    params=[
        (
            ANSWERS[0],
            'fix(users): email pattern corrected',
        ),
        (
            ANSWERS[1],
            'Chg: this is an Old-style Change',
        ),
        (
            ANSWERS[2],
            'New: this is an Old-style New type',
        ),
    ],
)
def messages(request):
    """Fixture for raw answer and expected formatted commit message.

    Args:
    ----
        request: see https://docs.pytest.org/en/stable/fixture.html#fixture-parametrize

    Returns:
    -------
        Box: raw commit `answer` and formatted `expected` message

    """
    return ddict(answer=request.param[0], expected=request.param[1])


@pytest.fixture()
@beartype
def gitcommits() -> List[git.GitCommit]:
    """Generate list of Git Commits.

    Returns
    -------
        List[git.GitCommit]: commits from `COMMITS_DATA`

    """
    return [
        git.GitCommit(
            commit['rev'],
            commit['title'],
            commit['body'],
        )
        for commit in COMMITS_DATA
    ]


@pytest.fixture()
@beartype
def tags() -> List[git.GitTag]:
    """Generate list of Git tTags.

    Returns
    -------
        List[git.GitTag]: tags from `TAGS`

    """
    return list(starmap(git.GitTag, TAGS))
