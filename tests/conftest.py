"""Pytest configuration.

Based on: https://github.com/commitizen-tools/commitizen/tree/master/tests
and: https://github.com/marcelomaia/commitizen-emoji/tree/master/tests

"""

from typing import List, Tuple

import pytest
from box import Box
from commitizen import defaults
from commitizen.config import BaseConfig
from loguru import logger


@pytest.fixture()
def config() -> BaseConfig:
    """Create default configuration.

    Returns:
        BaseConfig: base commitizen configuration

    """
    _config = BaseConfig()
    logger.debug(_config.settings)
    _config.settings.update({'name': defaults.name})
    _config.settings.update({'cz_legacy_map': {'Chg': 'Change (Old)'}})
    logger.debug(_config.settings)
    return _config


@pytest.fixture(params=[
    (
        {
            'prefix': 'fix',
            'scope': 'users',
            'subject': 'email pattern corrected',
            'is_breaking_change': False,
            'body': '',
            'footer': '',
        },
        'fix(users): email pattern corrected',
    ),
    (
        {
            'prefix': 'Chg',
            'scope': '',
            'subject': 'this is an Old-style Change',
            'is_breaking_change': False,
            'body': '',
            'footer': '',
        },
        'Chg: this is an Old-style Change',
    ),
    (
        {
            'prefix': 'New',
            'scope': '',
            'subject': 'this is an Old-style New type',
            'is_breaking_change': False,
            'body': '',
            'footer': '',
        },
        'New: this is an Old-style New type',
    ),
])
def messages(request: List[Tuple[dict, str]]) -> Box:
    """Fixture for raw answer and expected formatted commit message.

    Args:
        request: see https://docs.pytest.org/en/stable/fixture.html#fixture-parametrize

    Returns:
        Box: raw commit `answer` and formatted `expected` message

    """
    return Box({'answer': request.param[0], 'expected': request.param[1]})
