"""Support legacy commit tags specified in toml file."""

from commitizen import defaults
from commitizen.cz.conventional_commits.conventional_commits import ConventionalCommitsCz

EXAMPLE = """[tool.commitizen]
name = "cz_legacy"
# Other tool.commitizen configuration options

[tool.commitizen.cz_legacy_map]
Chg = "Change (old)"
Fix = "Fix (old)"
New = "New (old)"
"""
"""Example custom TOML file configuration. Note: should be kept consistent with the README."""


class _LegacyCz(ConventionalCommitsCz):

    def __init__(self, *args, **kwargs):
        """Initialize the class and override the data members."""
        super().__init__(*args, **kwargs)

        # Read the user-specified legacy change types (ct)
        cz_legacy_map = self.config.settings.get("cz_legacy_map")
        if not cz_legacy_map:
            raise RuntimeError(f"User must specify a `cz_legacy_map` dict in `[tool.commitizen]`. Example:\n{EXAMPLE}")
        joined_types = '|'.join([*cz_legacy_map.keys()])

        self.commit_parser = defaults.commit_parser.replace('<change_type>', f'<change_type>{joined_types}|')
        self.change_type_map = {**self.change_type_map, **cz_legacy_map}

        extended_pattern = defaults.bump_pattern.replace('refactor', f'refactor|{joined_types}')
        self.bump_pattern = extended_pattern
        self.changelog_pattern = extended_pattern
