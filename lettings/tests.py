from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class TestLettings(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="test street",
            city="test city",
            state="test state",
            zip_code=11100,
            country_iso_code="TST"
        )
        self.letting = Letting.objects.create(title="Test Obj Letting", address=self.address)

    def test_index(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_title(self):
        response = self.client.get(reverse('lettings:letting', args=[1]))
        assert response.status_code == 200
        assert b"<title>Test Obj Letting</title>" in response.content
