## Unreleased

## 2.0.0 (2024-06-12)

### Fix

- resolve test and type errors
- drop Python 3.7 and update minimum commitizen

## 1.0.2 (2024-04-16)

### Fix

- install beartype

## 1.0.1 (2024-03-31)

### Fix

- resolve CI failures
- **#15**: replace defaults with CZ variants

## 1.0.0 (2023-05-16)

### Fix

- remove unnecessary scripts configuration

## 1.0.0rc0 (2023-05-16)

### Feat

- migrate to new Entrypoint plugin format

### Fix

- don't extend Calcipy

### Refactor

- move EntryPoint config to pyproject.toml
- bump minimum pymdown dependency


- partially sync with latest copier

## 0.1.7 (2022-09-17)

### Fix

- update the version files list
- **#3**: ensure tests are only run when calcipy is available

## 0.1.6 (2022-02-18)

### Fix

- add link to changelog for PyPi
- regular imports do not work with this design

## 0.1.5 (2022-02-18)

### Fix

- update cz_legacy hook
- cleanup tests and import checks

## 0.1.3 (2022-01-16)

### Fix

- init calcipy template

### Refactor

- use "import as" for discover_this
- rename isort for copier

## 0.1.2 (2021-05-22)

### Fix

- specify minimum commitizen ver

## 0.1.1 (2020-12-31)

### Refactor

- raise commitizen CustomError

## 0.1.0 (2020-12-24)

### Fix

- update links in documentation

## 0.1.0rc0 (2020-12-24)

### Feat

- add pre-commit
- functional LegacyCz and docs

### Fix

- use cz>=2.11.1 by bumping min python
- prevent legacy types on new commits
