# cz_legacy

Custom Commitizen parser for user-specified legacy change types. The parser utilizes the `cz_conventional_commits` pattern and extends with the tag mapping specified in the configuration file.

While old change types will appear in the "Changelog", the user will be prevented from using them in new commits. This is the reverse of the [revert/chore logic](https://github.com/commitizen-tools/commitizen#why-are-revert-and-chore-valid-types-in-the-check-pattern-of-cz-conventional_commits-but-not-types-we-can-select) from commitizen that allows use of those commit types, but won't display them in the changelog.

## Alternatives

This customization only works when old commits use the `<change_type>: <message>` format that can be parsed by commitizen. If that doesn't fit your use case, you may want to try out [incremental](https://commitizen-tools.github.io/commitizen/changelog/#incremental) which (I think) prepends to an existing `CHANGELOG`

## Usage

### Pre-Commit

To use in pre-commit, add this to your `pre-commit-config.yml`. Run `pre-commit autoupdate` to get the latest version

```yaml
repos:
  - repo: https://github.com/commitizen-tools/commitizen
    rev: main
    hooks:
      - id: commitizen
        additional_dependencies: [cz_legacy]
        stages: [commit-msg]
```

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

## Issues

If you have any feature requests, run into any bugs, or have questions, feel free to start a discussion or open an issue on Github at [https://github.com/kyleking/cz_legacy](https://github.com/kyleking/cz_legacy).

## Project Status

See the `Open Issues` and/or the [CODE_TAG_SUMMARY]. For release history, see the [CHANGELOG].

## Contributing

We welcome pull requests! For your pull request to be accepted smoothly, we suggest that you first open a GitHub issue to discuss your idea. For resources on getting started with the code base, see the below documentation:

- [DEVELOPER_GUIDE]
- [STYLE_GUIDE]

## Code of Conduct

We follow the [Contributor Covenant Code of Conduct][contributor-covenant].

### Open Source Status

We try to reasonably meet most aspects of the "OpenSSF scorecard" from [Open Source Insights](https://deps.dev/pypi/cz_legacy)

## Responsible Disclosure

If you have any security issue to report, please contact the project maintainers privately. You can reach us at [dev.act.kyle@gmail.com](mailto:dev.act.kyle@gmail.com).

## License

[LICENSE]

[changelog]: https://cz_legacy.kyleking.me/docs/CHANGELOG
[code_tag_summary]: https://cz_legacy.kyleking.me/docs/CODE_TAG_SUMMARY
[contributor-covenant]: https://www.contributor-covenant.org
[developer_guide]: https://cz_legacy.kyleking.me/docs/DEVELOPER_GUIDE
[license]: https://github.com/kyleking/cz_legacy/blob/main/LICENSE
[style_guide]: https://cz_legacy.kyleking.me/docs/STYLE_GUIDE
