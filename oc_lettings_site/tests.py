from django.test import TestCase
from django.urls import reverse


class TestIndex(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200

    def test_title(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Welcome to Holiday Homes")


# test sentry
def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero
