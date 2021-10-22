import os

TEST_API_KEY = os.environ.get("DJANGO_REST_CLIENT_TEST_API_KEY", None)
TEST_URL = os.environ.get("DJANGO_REST_CLIENT_TEST_URL", "http://localhost:80")
MOCK_CONNECTIONS = True
