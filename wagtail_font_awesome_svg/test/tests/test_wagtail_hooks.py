from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class WagtailHooksTestCase(TestCase):
    def setUp(self):
        username, password = "admin", "123"
        user = get_user_model().objects.create_superuser(
            username,
            password=password,
        )
        user.save()
        self.client.login(username=username, password=password)

    def test_sprite(self):
        url = reverse("wagtailadmin_sprite")
        self.assertTrue(url.startswith("/admin/sprite-"))
        response = self.client.get(url)
        for icon_name in [
            "facebook",
            "laugh",
            "yin-yang",
        ]:
            self.assertIn(f'id="icon-{icon_name}"', str(response.content))
