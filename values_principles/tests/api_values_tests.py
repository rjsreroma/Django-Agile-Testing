from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from values_principles.models import Value


class APITestValue(APITestCase):
    def test_create_value(self):
        factory = APIRequestFactory()
        request = factory.post(
            "/values/",
            {"title": "new idea", "description": "new description"},
            format="json",
        )

    def test_update_value(self):
        factory = APIRequestFactory()
        request = factory.put(
            "/values/344",
            {"title": "update title", "description": "update description"},
            format="json",
        )

    def test_delete_value(self):
        factory = APIRequestFactory()
        request = factory.delete("/values/2", format="json")
