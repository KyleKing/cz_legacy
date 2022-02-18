"""Constants used for conftest factories."""

ANSWERS = [
    {
        'prefix': 'fix',
        'scope': 'users',
        'subject': 'email pattern corrected',
        'is_breaking_change': False,
        'body': '',
        'footer': '',
    },
    {
        'prefix': 'Chg',
        'scope': '',
        'subject': 'this is an Old-style Change',
        'is_breaking_change': False,
        'body': '',
        'footer': '',
    },
    {
        'prefix': 'New',
        'scope': '',
        'subject': 'this is an Old-style New type',
        'is_breaking_change': False,
        'body': '',
        'footer': '',
    },
]

COMMITS_DATA = [
    {
        'rev': '141ee441c9c9da0809c554103a558eb17c30ed17',  # pragma: allowlist secret
        'title': 'bump: version 1.1.1 → 1.2.0',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '6c4948501031b7d6405b54b21d3d635827f9421b',  # pragma: allowlist secret
        'title': 'docs: how to create custom bumps',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'ddd220ad515502200fe2dde443614c1075d26238',  # pragma: allowlist secret
        'title': 'feat: custom cz plugins now support bumping version',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'ad17acff2e3a2e141cbc3c6efd7705e4e6de9bfc',  # pragma: allowlist secret
        'title': 'docs: added bump gif',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '56c8a8da84e42b526bcbe130bd194306f7c7e813',  # pragma: allowlist secret
        'title': 'bump: version 1.1.0 → 1.1.1',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '74c6134b1b2e6bb8b07ed53410faabe99b204f36',  # pragma: allowlist secret
        'title': 'refactor: changed stdout statements',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'cbc7b5f22c4e74deff4bc92d14e19bd93524711e',  # pragma: allowlist secret
        'title': 'fix(bump): commit message now fits better with semver',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '1ba46f2a63cb9d6e7472eaece21528c8cd28b118',  # pragma: allowlist secret
        'title': 'fix: conventional commit "breaking change" in body instead of title',
        'body': 'closes #16',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'c35dbffd1bb98bb0b3d1593797e79d1c3366af8f',  # pragma: allowlist secret
        'title': 'refactor(schema): command logic removed from commitizen base',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '25313397a4ac3dc5b5c986017bee2a614399509d',  # pragma: allowlist secret
        'title': 'refactor(info): command logic removed from commitizen base',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '80105fb3c6d45369bc0cbf787bd329fba603864c',  # pragma: allowlist secret
        'title': 'refactor: removed delegator, added decli and many tests',
        'body': 'BREAKING CHANGE: API is stable',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'a96008496ffefb6b1dd9b251cb479eac6a0487f7',  # pragma: allowlist secret
        'title': 'docs: updated test command',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'aab33d13110f26604fb786878856ec0b9e5fc32b',  # pragma: allowlist secret
        'title': 'Bump version: 1.0.0b1 → 1.0.0b2',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'b73791563d2f218806786090fb49ef70faa51a3a',  # pragma: allowlist secret
        'title': 'docs(README): updated to reflect current state',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '7aa06a454fb717408b3657faa590731fb4ab3719',  # pragma: allowlist secret
        'title': 'Merge pull request #9 from Woile/dev',
        'body': 'feat: py3 only, tests and conventional commits 1.0',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '7c7e96b723c2aaa1aec3a52561f680adf0b60e97',  # pragma: allowlist secret
        'title': 'Bump version: 0.9.11 → 1.0.0b1',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'ed830019581c83ba633bfd734720e6758eca6061',  # pragma: allowlist secret
        'title': 'feat: py3 only, tests and conventional commits 1.0',
        'body': 'more tests\npyproject instead of Pipfile\nquestionary instead of whaaaaat (promptkit 2.0.0 support)',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'c52eca6f74f844ab3ffbde61d98ef96071e132b7',  # pragma: allowlist secret
        'title': 'Bump version: 0.9.10 → 0.9.11',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '0326652b2657083929507ee66d4d1a0899e861ba',  # pragma: allowlist secret
        'title': 'fix(config): load config reads in order without failing if there is no commitizen section',
        'body': 'Closes #8',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'b3f89892222340150e32631ae6b7aab65230036f',  # pragma: allowlist secret
        'title': 'Bump version: 0.9.9 → 0.9.10',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '5e837bf8ef0735193597372cd2d85e31a8f715b9',  # pragma: allowlist secret
        'title': 'fix: parse scope (this is my punishment for not having tests)',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '684e0259cc95c7c5e94854608cd3dcebbd53219e',  # pragma: allowlist secret
        'title': 'Bump version: 0.9.8 → 0.9.9',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': 'ca38eac6ff09870851b5c76a6ff0a2a8e5ecda15',  # pragma: allowlist secret
        'title': 'fix: parse scope empty',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '64168f18d4628718c49689ee16430549e96c5d4b',  # pragma: allowlist secret
        'title': 'Bump version: 0.9.7 → 0.9.8',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '9d4def716ef235a1fa5ae61614366423fbc8256f',  # pragma: allowlist secret
        'title': 'fix(scope): parse correctly again',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '46e9032e18a819e466618c7a014bcb0e9981af9e',  # pragma: allowlist secret
        'title': 'Bump version: 0.9.0 → 0.9.1',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
    {
        'rev': '0fef73cd7dc77a25b82e197e7c1d3144a58c1350',  # pragma: allowlist secret
        'title': 'fix(setup.py): future is now required for every python version',
        'body': '',
        'author': 'Commitizen',
        'author_email': 'author@cz.dev',
    },
]


TAGS = [
    ('v1.2.0', '141ee441c9c9da0809c554103a558eb17c30ed17', '2019-04-19'),  # pragma: allowlist secret
    ('v1.1.1', '56c8a8da84e42b526bcbe130bd194306f7c7e813', '2019-04-18'),  # pragma: allowlist secret
    ('v0.9.1', '46e9032e18a819e466618c7a014bcb0e9981af9e', '2017-11-11'),  # pragma: allowlist secret
]

CHANGELOG_TREE = (
    {
        'changes': {
            'feat': [
                {
                    'breaking': None,
                    'message': 'custom cz plugins now support bumping version',
                    'scope': None,
                },
            ],
        },
        'date': '2019-04-19',
        'version': 'v1.2.0',
    },
    {
        'changes': {
            'BREAKING CHANGE': [
                {'breaking': None, 'message': 'API is stable', 'scope': None},
            ],
            'feat': [
                {
                    'breaking': None,
                    'message': 'py3 only, tests and conventional commits 1.0',
                    'scope': None,
                },
            ],
            'fix': [
                {
                    'breaking': None,
                    'message': 'commit message now fits better with semver',
                    'scope': 'bump',
                },
                {
                    'breaking': None,
                    'message': 'conventional commit "breaking change" in body instead of title',
                    'scope': None,
                },
                {
                    'breaking': None,
                    'message': 'load config reads in order without failing if there is no commitizen section',
                    'scope': 'config',
                },
                {
                    'breaking': None,
                    'message': 'parse scope (this is my punishment for not having tests)',
                    'scope': None,
                },
                {
                    'breaking': None,
                    'message': 'parse scope empty',
                    'scope': None,
                },
                {
                    'breaking': None,
                    'message': 'parse correctly again',
                    'scope': 'scope',
                },
            ],
            'refactor': [
                {
                    'breaking': None,
                    'message': 'changed stdout statements',
                    'scope': None,
                },
                {
                    'breaking': None,
                    'message': 'command logic removed from commitizen base',
                    'scope': 'schema',
                },
                {
                    'breaking': None,
                    'message': 'command logic removed from commitizen base',
                    'scope': 'info',
                },
                {
                    'breaking': None,
                    'message': 'removed delegator, added decli and many tests',
                    'scope': None,
                },
            ],
        },
        'date': '2019-04-18',
        'version': 'v1.1.1',
    },
    {
        'changes': {
            'fix': [
                {
                    'breaking': None,
                    'message': 'future is now required for every python version',
                    'scope': 'setup.py',
                },
            ],
        },
        'date': '2017-11-11',
        'version': 'v0.9.1',
    },
)
