from abc import abstractmethod
from unittest import TestCase, SkipTest

from django_rest_client import APIResource
from example_project import ExampleClient, APIClientException

from tests import TEST_API_KEY, TEST_URL
from tests.mock_utils import if_mock_connections, patch, MockAPIResponse


class APIResourceBaseTestCase(TestCase):
    object_id = 1
    data = {}

    @classmethod
    def setUpClass(cls) -> None:
        if cls == APIResourceBaseTestCase:
            raise SkipTest(f"{cls.__name__} is an abstract base class.")
        # else, setup ExampleClient instance
        cls.client = ExampleClient(token=TEST_API_KEY)
        cls.client._server_url = TEST_URL
        return super().setUpClass()

    @property
    @abstractmethod
    def resource(self) -> APIResource:
        raise NotImplementedError()

    @if_mock_connections(
        patch(
            "requests.Session.request",
            side_effect=[
                MockAPIResponse({}, 200),
                MockAPIResponse({}, 400),
            ],
        )
    )
    def test__retrieve(self, *args, **kwargs):
        retrieve_fn = getattr(self.resource, "retrieve", None)
        if retrieve_fn:
            # a) ok
            response = retrieve_fn(object_id=self.object_id)
            self.assertEqual(200, response.code)
            # b) error
            with self.assertRaises(APIClientException):
                response = retrieve_fn(object_id=self.object_id)
                self.assertEqual(400, response.code)

    @if_mock_connections(
        patch(
            "requests.Session.request",
            side_effect=[
                MockAPIResponse({}, 200),
                MockAPIResponse({}, 400),
            ],
        )
    )
    def test__list(self, *args, **kwargs):
        list_fn = getattr(self.resource, "list", None)
        if list_fn:
            # a) ok
            response = list_fn()
            self.assertEqual(200, response.code)
            # b) error
            with self.assertRaises(APIClientException):
                response = list_fn()
                self.assertEqual(400, response.code)

    @if_mock_connections(
        patch(
            "requests.Session.request",
            side_effect=[
                MockAPIResponse({}, 201),
                MockAPIResponse({}, 400),
            ],
        )
    )
    def test__create(self, *args, **kwargs):
        create_fn = getattr(self.resource, "create", None)
        if create_fn:
            # a) ok
            response = create_fn(data=self.data)
            self.assertEqual(201, response.code)
            # b) error
            with self.assertRaises(APIClientException):
                response = create_fn(data=self.data)
                self.assertEqual(400, response.code)

    @if_mock_connections(
        patch(
            "requests.Session.request",
            side_effect=[
                MockAPIResponse({}, 200),
                MockAPIResponse({}, 400),
            ],
        )
    )
    def test__update(self, *args, **kwargs):
        update_fn = getattr(self.resource, "update", None)
        if update_fn:
            # a) ok
            response = update_fn(object_id=self.object_id, data=self.data)
            self.assertEqual(200, response.code)
            # b) error
            with self.assertRaises(APIClientException):
                response = update_fn(object_id=self.object_id, data=self.data)
                self.assertEqual(400, response.code)

    @if_mock_connections(
        patch(
            "requests.Session.request",
            side_effect=[
                MockAPIResponse({}, 204),
                MockAPIResponse({}, 400),
            ],
        )
    )
    def test__delete(self, *args, **kwargs):
        delete_fn = getattr(self.resource, "delete", None)
        if delete_fn:
            # a) ok
            response = delete_fn(object_id=self.object_id)
            self.assertEqual(204, response.code)
            # b) error
            with self.assertRaises(APIClientException):
                response = delete_fn(object_id=self.object_id)
                self.assertEqual(400, response.code)

    @if_mock_connections(
        patch(
            "requests.Session.request",
            side_effect=[
                MockAPIResponse({"total_pages": 2}, 200),
                MockAPIResponse({"total_pages": 2}, 200),
                MockAPIResponse({"total_pages": 2}, 400),
                MockAPIResponse({"total_pages": 2}, 400),
            ],
        )
    )
    def test__auto_paging_iter(self, *args, **kwargs):
        page_iter_fn = getattr(self.resource, "auto_paging_iter", None)
        if page_iter_fn:
            # a) ok
            for response in page_iter_fn():
                self.assertEqual(200, response.code)
            # b) error
            with self.assertRaises(APIClientException):
                for response in page_iter_fn():
                    self.assertEqual(200, response.code)

    @if_mock_connections(
        patch(
            "requests.Session.request",
            side_effect=[
                MockAPIResponse({}, 200),
                MockAPIResponse({}, 400),
            ],
        )
    )
    def test__get(self, *args, **kwargs):
        get_fn = getattr(self.resource, "get", None)
        if get_fn:
            # a) ok
            response = get_fn()
            self.assertEqual(200, response.code)
            # b) error
            with self.assertRaises(APIClientException):
                response = get_fn()
                self.assertEqual(400, response.code)
