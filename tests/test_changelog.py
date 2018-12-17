from commitizen.cz.conventional_commits.auto_changelog import AutoChangelog

VALID_MESSAGES = [
    "BREAKING CHANGE: `extends` key in config file is now used for extending other config files",
    "feat(cli): added version",
    "feat(commiter): conventional commit is a bit more intelligent now",
    "docs(README): motivation",
    "fix(setup.py): future is now required for every python version",
    "refactor: python 2 support",
    "docs(README): python 2 support limited",
    "chore(setup.py): support for python 2 (by a friend request)",
    "chore(setup.py): python requires only > 3.4 (last time)",
    "chore(setup.py): python 3 only again",
    "chore(setup.py): python 3 only now",
    "chore(setup.py): support for python3 only",
    "chore(cz): added .cz.cfg to the project",
    "docs(README): git log example and renamed example",
    "docs: minor correction",
    "docs: improved commitizens tab in readme",
    "feat(cz): jira smart commits",
    "refactor(cli): renamed all to ls command",
    "refactor(cz): renamed angular cz to conventional changelog cz",
    "docs: modified usage page",
    "docs(README): table of contents",
]

INVALID_MESSAGES = [
    "Bump version: 0.9.3 → 0.9.4",
    "Update README.md",
    "ci",
    "Merge branch 'master' of github.com:jhfjhfj1/autokeras",
    "Add DebugMiddleware",
    "Raise ClientDisconnect if disconnected while reading request body",
]


def test_parse_message():
    a = AutoChangelog()

    for message in VALID_MESSAGES:
        r = a.parse_message(message)
        assert r is not None


def test_parse_message_fails():
    a = AutoChangelog()
    for message in INVALID_MESSAGES:
        r = a.parse_message(message)
        assert r is None
