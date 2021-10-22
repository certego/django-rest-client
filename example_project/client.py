from django_rest_client import APIClient

from .resources import ExampleResource, ExampleSingletonResource


class ExampleClient(APIClient):
    # overwrite
    _server_url: str = "https://fake_url.com/"
    _headers = {"User-Agent": "ExampleClient"}

    # resources
    ExampleResource = ExampleResource
    ExampleSingletonResource = ExampleSingletonResource
