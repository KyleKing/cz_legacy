"""Test the cz_legacy module."""

import pytest
from commitizen import changelog
from commitizen.config import BaseConfig

from cz_legacy import discover_this

from .configuration import PATH_TEST_CHANGELOG
from .conftest import CHANGELOG_TREE


def test_missing_legacy_map():
    """Test that an error is raised when the `cz_legacy_map` setting is missing."""
    _config = BaseConfig()
    match = r'User must specify a `cz_legacy_map` dict in `\[tool.commitizen\]`. Example:\n\[tool.commitizen\]\n'

    with pytest.raises(RuntimeError, match=match):
        discover_this(_config)


def test_message(config, messages):
    """Test discover_this.message."""
    cz = discover_this(config)

    message = cz.message(messages.answer)  # act

    assert message == messages.expected


def test_generate_tree_from_commits(config, gitcommits, tags):
    """Test generating the changelog tree."""
    cz = discover_this(config)
    parser = cz.commit_parser
    changelog_pattern = cz.bump_pattern

    tree = changelog.generate_tree_from_commits(gitcommits, tags, parser, changelog_pattern)  # act

    assert tuple(tree) == CHANGELOG_TREE


def test_render_changelog(config, gitcommits, tags):  # , changelog_content):
    """Test generating the changelog content."""
    cz = discover_this(config)
    parser = cz.commit_parser
    changelog_pattern = cz.bump_pattern
    tree = changelog.generate_tree_from_commits(gitcommits, tags, parser, changelog_pattern)

    result = changelog.render_changelog(tree)

    assert result == PATH_TEST_CHANGELOG.read_text()
