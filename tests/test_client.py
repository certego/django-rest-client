from .abstract_test_case import APIResourceBaseTestCase, APIResource
from .mock_utils import generic_200_mock, generic_201_mock


class ExampleResourceTestCase(APIResourceBaseTestCase):
    @property
    def resource(self) -> APIResource:
        return self.client.ExampleResource

    @generic_200_mock
    def test__custom_action(self, *args, **kwargs):
        response = self.resource.custom_action()
        self.assertEqual(200, response.code)

    @generic_201_mock
    def test__custom_action_detailed(self, *args, **kwargs):
        response = self.resource.custom_action_detailed(object_id=self.object_id)
        self.assertEqual(201, response.code)


class ExampleSingletonResourceTestCase(APIResourceBaseTestCase):
    @property
    def resource(self) -> APIResource:
        return self.client.ExampleSingletonResource
