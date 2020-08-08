from django.test import TestCase
from values_principles.models import Value


class TestValueCrud(TestCase):
    def test_value_create(self):
        Value.objects.create(title="title 1", description="description 1")
        assert Value.objects.count() == 1

    def test_value_view_details(self):
        value = Value.objects.create(title="title 1", description="description 1")
        assert value.title == "title 1"
        assert value.description == "description 1"

    def test_value_update(self):
        value = Value.objects.create(title="title 1", description="description 1")
        value.title = "This is a title"
        assert value.title == "This is a title"

    def test_value_delete(self):
        Value.objects.create(title="title 1", description="description 1")
        Value.objects.create(title="title 2", description="description 2")
        title2 = Value.objects.get(title="title 2")
        title2.delete()
        assert Value.objects.count() == 1
