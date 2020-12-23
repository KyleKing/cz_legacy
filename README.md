# cz_legacy

Custom Commitizen parser for user-specified legacy change types. The parser utilizes the `cz_conventional_commits` pattern and extends with the tag mapping specified in the configuration file

## Usage

At minimum, you must have the `name = "cz_legacy"` and `[tool.commitizen.cz_legacy_map]` in your configuration file. The below example is for TOML, you can also utilize a YAML or JSON file.

Below is an example of the three change legacy types Chg, Fix, and New, but the user can choose any tag names and associated mapping for the Changelog

```toml
[tool.commitizen]
name = "cz_legacy"
# Other tool.commitizen configuration options

[tool.commitizen.cz_legacy_map]
Chg = "Change (old)"
Fix = "Fix (old)"
New = "New (old)"
```

## Background

I couldn't find a good way of just adding a few legacy change types from an old commit style to commitizen, but [you can extend the classes to provide custom logic](https://commitizen-tools.github.io/commitizen/customization/#2-customize-through-customizing-a-class). The `LegacyCz` class inherits from [`ConventionalCommitsCz`](https://github.com/commitizen-tools/commitizen/blob/master/commitizen/cz/conventional_commits/conventional_commits.py) so that you can use the Conventional Commit style moving forward. For reference, these are the [default settings](https://github.com/commitizen-tools/commitizen/blob/master/commitizen/defaults.py)

## Planned Changes

- TODO: Figure out how to prevent the Legacy tags from being used for new commits
  - TODO: Is the `schema_pattern` necessary?
