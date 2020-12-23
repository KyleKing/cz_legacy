# cz_legacy

Custom Commitizen parser for user-specified legacy change types. The parser utilizes the `cz_conventional_commits` pattern and extends with the tag mapping specified in the configuration file

While old change types will appear in the Changelog, the user will be prevented from using them in new commits. This is the reverse of the [`revert`/`chore` logic](https://github.com/commitizen-tools/commitizen#why-are-revert-and-chore-valid-types-in-the-check-pattern-of-cz-conventional_commits-but-not-types-we-can-select) from commitizen that allows use of those commit types, but won't display them in the changelog

## Alternatives

This customization only works when old commits use the `<change_type>: <message>` format that can be parsed by commitizen. If that doesn't fit your use case, you may want to try out the [incremental](https://commitizen-tools.github.io/commitizen/changelog/#incremental) which doesn't modify existing portions of a `CHANGELOG`

## Usage

### Configuration

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

### Install

You will also need to install this package. At the time, i haven't published this to PyPi, so you will need to use git. Below is an example with poetry:

```toml
[tool.poetry.dev-dependencies.cz_legacy]
git = "https://github.com/kyleking/cz_legacy.git"
branch = "main"
```

or with pip: `pip install git+https://github.com/KyleKing/cz_legacy.git`

To use in pre-commit, add this to your `pre-commit-config.yml`

```yaml
repos:
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v2.11.1
    hooks:
      - id: commitizen
        additional_dependencies: ["git+https://github.com/KyleKing/cz_legacy.git"]
        stages: [commit-msg]
```

> Note: I plan to publish this to PyPi, but it is not yet published at the time of writing

## Background

I couldn't find a good way of just adding a few legacy change types from an old commit style to commitizen, but [you can extend the classes to provide custom logic](https://commitizen-tools.github.io/commitizen/customization/#2-customize-through-customizing-a-class). The `LegacyCz` class inherits from [`ConventionalCommitsCz`](https://github.com/commitizen-tools/commitizen/blob/master/commitizen/cz/conventional_commits/conventional_commits.py) so that you can use the Conventional Commit style moving forward. For reference, these are the [default settings](https://github.com/commitizen-tools/commitizen/blob/master/commitizen/defaults.py)

## Planned Changes

- TODO: publish to PyPi
