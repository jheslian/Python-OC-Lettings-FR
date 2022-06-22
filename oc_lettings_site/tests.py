from django.http import HttpResponse
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
    """ try:
        division_by_zero = 1 / 0
    except Exception as err:
        print(err)
    return HttpResponse('This is an error')"""

