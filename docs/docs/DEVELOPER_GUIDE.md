# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/cz_legacy.git
cd cz_legacy
poetry install --sync

# See the available tasks
poetry run calcipy
# Or use a local 'run' file (so that 'calcipy' can be extended)
./run

# Run the default task list (lint, auto-format, test coverage, etc.)
./run main

# Make code changes and run specific tasks as needed:
./run lint.fix test
```

## Publishing

For testing, create an account on [TestPyPi](https://test.pypi.org/legacy/). Replace `...` with the API token generated on TestPyPi or PyPi respectively

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi ...

./run main pack.publish --to-test-pypi
# If you didn't configure a token, you will need to provide your username and password to publish
```

To publish to the real PyPi

```sh
poetry config pypi-token.pypi ...
./run release

# Or for a pre-release
./run release --suffix=rc
```

## Current Status

<!-- {cts} COVERAGE -->
| File                     |   Statements |   Missing |   Excluded | Coverage   |
|--------------------------|--------------|-----------|------------|------------|
| `cz_legacy/__init__.py`  |           17 |         0 |         17 | 100.0%     |
| `cz_legacy/cz_legacy.py` |           18 |         0 |          0 | 100.0%     |
| **Totals**               |           35 |         0 |         17 | 100.0%     |

Generated on: 2023-12-10
<!-- {cte} -->
