# Developer Notes

## Local Development

This project is built with `calcipy` with some minor modifications

```sh
git clone https://github.com/KyleKing/cz_legacy.git
cd cz_legacy
poetry install

# See the available tasks
poetry run doit list

# Run the default task list (lint, auto-format, test coverage, etc.)
poetry run doit
```

## Publishing

For testing, create an account on [TestPyPi](https://test.pypi.org/legacy/)

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi ...

poetry build
poetry publish --repository testpypi
# If you didn't configure a token, you will need to provide your username and password to publish
```

To publish to the real PyPi

```sh
poetry config pypi-token.pypi ...
poetry build
poetry publish
```

Other useful poetry snippets

```sh
# Choose Pre-Release Type ({alpha,beta,rc})
poetry run cz bump --prerelease rc --changelog --dry-run
# git push --tags?

# Combine build and publish
poetry publish --build
```

## Resources

- [Official Docs](https://python-poetry.org/docs/repositories/)
- [Ian Wootten: Publishing a Package to PyPi With Poetry](https://www.ianwootten.co.uk/2020/10/20/publishing-a-package-to-pypi-with-poetry/)
