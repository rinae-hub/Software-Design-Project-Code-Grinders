from django.apps import apps
from django.test import TestCase
from web.apps import WebConfig


class WebConfig (TestCase):
    def test_apps(self):
        self.assertEqual(WebConfig.name, 'web')
        self.assertEqual(apps.get_app_config('web').name, 'web')
