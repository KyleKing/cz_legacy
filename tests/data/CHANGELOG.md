
## v1.2.0 (2019-04-19)

### Feat

- custom cz plugins now support bumping version

## v1.1.1 (2019-04-18)

### Refactor

- changed stdout statements
- **schema**: command logic removed from commitizen base
- **info**: command logic removed from commitizen base
- removed delegator, added decli and many tests

### Fix

- **bump**: commit message now fits better with semver
- conventional commit "breaking change" in body instead of title
- **config**: load config reads in order without failing if there is no commitizen section
- parse scope (this is my punishment for not having tests)
- parse scope empty
- **scope**: parse correctly again

### BREAKING CHANGE

- API is stable

### Feat

- py3 only, tests and conventional commits 1.0

## v0.9.1 (2017-11-11)

### Fix

- **setup.py**: future is now required for every python version
