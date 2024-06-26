"""Support legacy commit tags specified in toml file."""

from commitizen.config.base_config import BaseConfig
from commitizen.cz.conventional_commits.conventional_commits import ConventionalCommitsCz
from commitizen.exceptions import CustomError

EXAMPLE = """[tool.commitizen]
name = "cz_legacy"
# Other tool.commitizen configuration options

[tool.commitizen.cz_legacy_map]
Chg = "Change (old)"
Fix = "Fix (old)"
New = "New (old)"
"""
"""Example custom TOML file configuration. Note: keep in-sync with README."""


class _LegacyCz(ConventionalCommitsCz):
    """Extend Conventional Commits with custom labels."""

    def __init__(self, config: BaseConfig) -> None:
        """Initialize the class and override the data members.

        Args:
        ----
            config: commitizen BaseConfig that stores the parsed settings. Passed to base class

        Raises:
        ------
            CustomError: commitizen-specific error and exit code to indicate that a configuration item is missing

        """
        super().__init__(config)

        # Read the user-specified legacy change types (ct)
        cz_legacy_map = self.config.settings.get('cz_legacy_map')
        if not cz_legacy_map or not isinstance(cz_legacy_map, dict):
            raise CustomError(
                f'User must specify a `cz_legacy_map` dict in `[tool.commitizen]`. Example:\n{EXAMPLE}',  # noqa: EM102
            )
        joined_types = '|'.join(cz_legacy_map)

        if not ConventionalCommitsCz.commit_parser or not ConventionalCommitsCz.bump_pattern:  # for pyright
            raise NotImplementedError('Try downgrading commitizen. Missing required config')

        self.commit_parser = ConventionalCommitsCz.commit_parser.replace(
            '<change_type>',
            f'<change_type>{joined_types}|',
        )
        if not isinstance(self.change_type_map, dict):
            raise NotImplementedError('Incompatible ConventionalCommitsCz.change_type_map')
        self.change_type_map = {**self.change_type_map, **cz_legacy_map}

        extended_pattern = ConventionalCommitsCz.bump_pattern.replace('refactor', f'refactor|{joined_types}')
        self.bump_pattern = extended_pattern
        self.changelog_pattern = extended_pattern
