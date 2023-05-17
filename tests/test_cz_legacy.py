"""Test the cz_legacy module."""

import pytest
from commitizen import changelog, git
from commitizen.config import BaseConfig
from commitizen.exceptions import CustomError

from cz_legacy.cz_legacy import _LegacyCz

from .configuration import PATH_TEST_CHANGELOG
from .constants import CHANGELOG_TREE


def test_missing_legacy_map():
    """Test that an error is raised when the `cz_legacy_map` setting is missing."""
    _config = BaseConfig()
    match = r'User must specify a `cz_legacy_map` dict in `\[tool.commitizen\]`. Example:\n\[tool.commitizen\]\n'

    with pytest.raises(CustomError, match=match):
        _LegacyCz(_config)


def test_message(config, messages):
    """Test _LegacyCz.message."""
    cz = _LegacyCz(config)

    message = cz.message(messages.answer)  # act

    assert message == messages.expected


def test_generate_tree_from_commits(config, gitcommits, tags):
    """Test generating the changelog tree."""
    cz = _LegacyCz(config)
    parser = cz.commit_parser
    changelog_pattern = cz.bump_pattern

    tree = changelog.generate_tree_from_commits(gitcommits, tags, parser, changelog_pattern)  # act

    assert tuple(tree) == CHANGELOG_TREE


def test_render_changelog(config, gitcommits, tags):
    """Test generating the changelog content with the user-specified mapping."""
    cz = _LegacyCz(config)
    parser = cz.commit_parser
    changelog_pattern = cz.bump_pattern
    tree = changelog.generate_tree_from_commits(
        commits=gitcommits,
        tags=tags,
        commit_parser=parser,
        changelog_pattern=changelog_pattern,
        change_type_map=cz.change_type_map,
    )

    result = changelog.render_changelog(tree)

    assert result == PATH_TEST_CHANGELOG.read_text()


def test_render_changelog_unsupported_type(config):
    """Test that unsupported types are excluded from the changelog content."""
    cz = _LegacyCz(config)
    parser = cz.commit_parser
    changelog_pattern = cz.bump_pattern
    gitcommits = [
        git.GitCommit(rev='003', title='feat: started commitizen', body=''),
        git.GitCommit(rev='002', title='Chg: some legacy commit with changes', body=''),
        git.GitCommit(rev='001', title='NotLegacy: unsupported change type', body=''),
    ]
    tree = changelog.generate_tree_from_commits(
        commits=gitcommits,
        tags=[],
        commit_parser=parser,
        changelog_pattern=changelog_pattern,
        change_type_map=cz.change_type_map,
    )
    expected = """
## Unreleased

### Feat

- started commitizen

### Change (Old)

- some legacy commit with changes
"""

    result = changelog.render_changelog(tree)

    assert result == expected
