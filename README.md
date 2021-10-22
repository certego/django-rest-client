# django-rest-client

[![PyPI version](https://badge.fury.io/py/django-rest-client.svg)](https://badge.fury.io/py/django-rest-client)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/django-rest-client.svg)](https://pypi.python.org/pypi/django-rest-client/)

[![Lint & Tests](https://github.com/certego/django-rest-client/workflows/Lint%20&%20Tests/badge.svg)](https://github.com/certego/django-rest-client/actions)
[![codecov](https://codecov.io/gh/certego/django-rest-client/branch/main/graph/badge.svg?token=TWGZt6zfRD)](https://codecov.io/gh/certego/django-rest-client)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/certego/django-rest-client.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/certego/django-rest-client/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/certego/django-rest-client/badge)](https://www.codefactor.io/repository/github/certego/django-rest-client)

An abstract and extensible framework in python for building client SDKs and CLI tools for a RESTful API.

Suitable for APIs made with [django-rest-framework](https://github.com/encode/django-rest-framework) and other such general frameworks.

For rapid building of ease-of-use, type-hinted and self-documented API clients in python.

## Installation

Requires python version >=3.6.

```bash
$ pip3 install django_rest_client
```

- For usage with [click](https://github.com/pallets/click), `pip3 install django_rest_client[cli]`
- For development/testing, `pip3 install django_rest_client[dev]`

## Documentation

> [pydragonfly](https://github.com/certego/pydragonfly) is a complete project built on top of django-rest-client and serves as a good frame of reference for developers.

- Code reference: Please see [`example_project`](https://github.com/certego/django-rest-client/tree/main/example_project).
- CLI example: Open a terminal and run `django_rest_client_example -h`.
- Changelog: [CHANGELOG.md](https://github.com/certego/django-rest-client/blob/main/.github/CHANGELOG.md)

## Projects using django-rest-client

- [pydragonfly](https://github.com/certego/pydragonfly)

## License

BSD © [certego](https://github.com/certego)
