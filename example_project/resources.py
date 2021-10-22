from typing import Optional

from django_rest_client import (
    APIResource,
    APIResponse,
    RetrievableAPIResourceMixin,
    ListableAPIResourceMixin,
    PaginationAPIResourceMixin,
    DeletableAPIResourceMixin,
    UpdateableAPIResourceMixin,
    SingletonAPIResourceMixin,
)
from django_rest_client.types import Toid, TParams


class ExampleResource(
    APIResource,
    RetrievableAPIResourceMixin,
    ListableAPIResourceMixin,
    PaginationAPIResourceMixin,
    DeletableAPIResourceMixin,
    UpdateableAPIResourceMixin,
):
    """
    An Example resource. Suitable for DRF's ``ModelView``.
    """

    OBJECT_NAME = "api.example"
    EXPANDABLE_FIELDS = {
        "retrieve": ["attr1", "attr2"],
        "list": ["attr1", "attr2"],
    }
    ORDERING_FIELDS = []

    @classmethod
    def custom_action(
        cls,
        params: Optional[TParams] = None,
    ) -> APIResponse:
        """
        Suitable for ``@action`` decorator views with  ``detaile=False``.
        """
        url = cls.class_url() + "/custom-action"
        return cls._request("GET", url=url, params=params)

    @classmethod
    def custom_action_detailed(
        cls,
        object_id: Toid,
        params: Optional[TParams] = None,
    ) -> APIResponse:
        """
        Suitable for ``@action`` decorator views with ``detaile=True``.
        """
        url = cls.instance_url(object_id) + "/custom-action-detailed"
        return cls._request("POST", url=url, params=params)


class ExampleSingletonResource(
    APIResource,
    SingletonAPIResourceMixin,
    RetrievableAPIResourceMixin,
    ListableAPIResourceMixin,
):
    """
    An Example singleton resource. Suitable for DRF's ``APIView``.
    """

    OBJECT_NAME = "api.singleton"
    EXPANDABLE_FIELDS = {
        "retrieve": [],
        "list": [],
    }
    ORDERING_FIELDS = []
