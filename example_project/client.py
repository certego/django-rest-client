from django_rest_client import APIClient

from .resources import ExampleResource, ExampleSingletonResource


class ExampleClient(APIClient):
    # overwrite
    _server_url: str = "https://fake_url.com/"

    @property
    def _headers(self):
        return {
            "Authorization": f"Token {self.__token}",
            "User-Agent": "ExampleClient",
        }

    # resources
    ExampleResource = ExampleResource
    ExampleSingletonResource = ExampleSingletonResource
