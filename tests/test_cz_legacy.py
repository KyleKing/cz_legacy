"""Test the cz_legacy module."""

import pytest
from commitizen.config import BaseConfig

from cz_legacy import discover_this


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

