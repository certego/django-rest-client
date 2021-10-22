from django_rest_client import APIClient
from django_rest_client.types import THeaders

from .resources import ExampleResource, ExampleSingletonResource


class ExampleClient(APIClient):
    # overwrite
    _server_url: str = "https://fake_url.com/"

    @property
    def _headers(self) -> THeaders:
        return {
            **super()._headers,
            "User-Agent": "ExampleClient",
        }

    # resources
    ExampleResource = ExampleResource
    ExampleSingletonResource = ExampleSingletonResource
