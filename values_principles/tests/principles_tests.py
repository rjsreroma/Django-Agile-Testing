from django.test import TestCase

from values_principles.models import Principle


class TestPrincipleCrud(TestCase):
    def test_principle_create(self):
        Principle.objects.create(title="principle 1", description="this is principle")
        assert Principle.objects.count() == 1

    def test_principle_view_details(self):
        principle = Principle.objects.create(
            title="principle 1", description="this is principle"
        )
        assert principle.title == "principle 1"
        assert principle.description == "this is principle"

    def test_principle_update(self):
        principle = Principle.objects.create(
            title="principle 1", description="this is principle"
        )
        principle.title = "principle updated"
        principle.description = "description updated"
        assert principle.title == "principle updated", (
            principle.description == "description updated"
        )

    def test_principle_delete(self):
        Principle.objects.create(title="principle 1", description="this is principle")
        Principle.objects.create(
            title="principle 2", description="this is another principle"
        )
        principle2 = Principle.objects.get(pk=2)
        principle2.delete()
        assert Principle.objects.count() == 1
