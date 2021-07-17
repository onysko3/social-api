from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post


class PostCreateMixin(APITestCase):
    def setUp(self):
        self.author = get_user_model().objects.create_user(
            username='userauthor',
            password='userpass123'
        )
        self.test_user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.data = {
            'body': 'content'
        }
        self.client.login(username='userauthor', password='userpass123')
        self.response = self.client.post(reverse('post_list'), self.data, format='json')


class PostAuthorAPITests(PostCreateMixin, APITestCase):

    def test_api_post_create(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().author, self.author)
        self.assertEqual(Post.objects.get().body, 'content')

    def test_api_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)

    def test_api_post_detail(self):
        post = Post.objects.get()
        response = self.client.get(reverse('post_detail', kwargs={'pk': post.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)

    def test_api_post_update(self):
        post = Post.objects.get()
        new_data = {
            'body': 'text'
        }
        response = self.client.put(reverse('post_detail', kwargs={'pk': post.id}), data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().body, 'text')

    def test_api_post_delete(self):
        post = Post.objects.get()
        response = self.client.delete(reverse('post_detail', kwargs={'pk': post.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class PostUserAPITests(PostCreateMixin, APITestCase):

    def setUp(self):
        super().setUp()
        self.client.logout()
        self.client.login(username='testuser', password='testpass123')

    def test_api_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)

    def test_api_post_detail(self):
        post = Post.objects.get()
        response = self.client.get(reverse('post_detail', kwargs={'pk': post.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, post)

    def test_api_post_update(self):
        post = Post.objects.get()
        new_data = {
            'body': 'text'
        }
        response = self.client.put(reverse('post_detail', kwargs={'pk': post.id}), data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_post_delete(self):
        post = Post.objects.get()
        response = self.client.delete(reverse('post_detail', kwargs={'pk': post.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

