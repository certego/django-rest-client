from unittest import skipIf, skip  # noqa: F401
from unittest.mock import patch, MagicMock  # noqa: F401

from requests.models import HTTPError

from tests import MOCK_CONNECTIONS, TEST_URL


class MockAPIResponse:
    def __init__(self, json_data, status_code, uri="", content=None, headers=None):
        self.json_data = json_data
        self.status_code = status_code
        self.url = TEST_URL + uri
        self.content = content
        self.headers = headers

    def json(self):
        return self.json_data

    def raise_for_status(self):
        http_error_msg = None
        if 400 <= self.status_code < 500:
            http_error_msg = u"%s Client Error: url: %s" % (
                self.status_code,
                self.url,
            )

        elif 500 <= self.status_code < 600:
            http_error_msg = u"%s Server Error: url: %s" % (
                self.status_code,
                self.url,
            )

        if http_error_msg:
            raise HTTPError(http_error_msg, response=self)


def if_mock_connections(*decorators):
    def apply_all(f):
        for d in reversed(decorators):
            f = d(f)
        return f

    return apply_all if MOCK_CONNECTIONS else lambda x: x


generic_200_mock = if_mock_connections(
    patch(
        "requests.Session.request",
        return_value=MockAPIResponse({}, 200),
    )
)

generic_201_mock = if_mock_connections(
    patch(
        "requests.Session.request",
        return_value=MockAPIResponse({}, 201),
    )
)

generic_204_mock = if_mock_connections(
    patch(
        "requests.Session.request",
        return_value=MockAPIResponse({}, 204),
    )
)

generic_400_mock = if_mock_connections(
    patch(
        "requests.Session.request",
        return_value=MockAPIResponse({}, 400),
    )
)
