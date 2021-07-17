from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


class UserTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_api_user_list(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_api_user_detail(self):
        response = self.client.get(reverse('user_detail', kwargs={'pk': self.user.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.user.username)
