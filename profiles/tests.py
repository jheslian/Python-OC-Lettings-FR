from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class TestProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="test",
            password="test_password",
            first_name="test_fname",
            last_name="test_lname",
            email="test@test.tst"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_index(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def test_title(self):
        response = self.client.get(reverse('profiles:profile', args=['test']))
        assert response.status_code == 200
        assert b"<title>test</title>" in response.content
