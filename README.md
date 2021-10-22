# DRF-client

[![PyPI version](https://badge.fury.io/py/drf-client.svg)](https://badge.fury.io/py/drf-client)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/drf-client.svg)](https://pypi.python.org/pypi/drf-client/)

[![Lint & Tests](https://github.com/certego/drf-client/workflows/Lint%20&%20Tests/badge.svg)](https://github.com/certego/drf-client/actions)
[![codecov](https://codecov.io/gh/certego/drf-client/branch/main/graph/badge.svg?token=KBk4rQj08b)](https://codecov.io/gh/certego/drf-client)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/certego/drf-client.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/certego/drf-client/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/certego/drf-client/badge)](https://www.codefactor.io/repository/github/certego/drf-client)

An abstract and extensible implementation of python SDK and CLI for APIs built with [django-rest-framework](https://github.com/encode/django-rest-framework) and other such general frameworks.

For rapid building of ease-of-use, type-hinted and self-documented API clients in python.

## Installation

Requires python version >=3.6.

```bash
$ pip3 install drf_client
```

- For usage with [click](https://github.com/pallets/click), `pip3 install drf_client[cli]`
- For development/testing, `pip3 install drf_client[dev]`

## Documentation

> [pydragonfly](https://github.com/certego/pydragonfly) is a complete project built on top of DRF-client and serves as a good frame of reference for developers.

- Code reference: Please see [`example_project`](https://github.com/certego/drf-client/tree/main/example_project).
- CLI Example: Open a terminal and run `drf_client_example -h`.
- Changelog: [CHANGELOG.md](https://github.com/certego/drf-client/blob/main/.github/CHANGELOG.md)

## Projects using drf-client

- [pydragonfly](https://github.com/certego/pydragonfly)
