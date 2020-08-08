from agile_project.settings import INSTALLED_APPS
from django.test import TestCase # type: ignore


class SettingsTest(TestCase):
    def test_value_principles_is_configured(self):
        assert 'values_principles' in INSTALLED_APPS

    def test_rest_framework_is_configured(self):
        assert 'rest_framework' in INSTALLED_APPS