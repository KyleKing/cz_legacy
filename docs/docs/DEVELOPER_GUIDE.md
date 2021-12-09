# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/cz_legacy.git
cd cz_legacy
poetry install

# See the available tasks
poetry run doit list

# Run the default task list (lint, auto-format, test coverage, etc.)
poetry run doit --continue

# Make code changes and run specific tasks as needed:
poetry run doit run test
```

## Publishing

For testing, create an account on [TestPyPi](https://test.pypi.org/legacy/). Replace `...` with the appropriate API token

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi ...

poetry run doit run publish_test_pypi
# If you didn't configure a token, you will need to provide your username and password to publish
```

To publish to the real PyPi

```sh
poetry config pypi-token.pypi ...
poetry run doit run publish

# For a full release, increment the version, the documentation, and publish
poetry run doit run --continue
poetry run doit run cl_bump document deploy_docs publish
# Note: cl_bump_pre is helpful for pre-releases rather than full increments
```

## Current Status

<!-- {cts} COVERAGE -->
| File                     |   Statements |   Missing |   Excluded | Coverage   |
|:-------------------------|-------------:|----------:|-----------:|:-----------|
| `cz_legacy/__init__.py`  |            5 |         0 |          0 | 100.0%     |
| `cz_legacy/cz_legacy.py` |           17 |         0 |          0 | 100.0%     |
| **Totals**               |           22 |         0 |          0 | 100.0%     |

Generated on: 2021-12-08T22:37:06.758322
<!-- {cte} -->
