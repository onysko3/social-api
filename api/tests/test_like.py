from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post, PostLike
from .test_post import PostCreateMixin


class PostLikeAuthorAPITests(PostCreateMixin, APITestCase):

    def setUp(self):
        super().setUp()
        post = Post.objects.get()
        self.like_data = {
            'post': post.id
        }
        self.response = self.client.post(reverse('like_list'), self.like_data, format='json')

    def test_api_like_create(self):
        post = Post.objects.get()
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PostLike.objects.count(), 1)
        self.assertEqual(PostLike.objects.get().user, self.author)
        self.assertEqual(PostLike.objects.get().post, post)

    def test_api_like_list(self):
        response = self.client.get(reverse('like_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PostLike.objects.count(), 1)

    def test_api_like_detail(self):
        like = PostLike.objects.get()
        response = self.client.get(reverse('like_detail', kwargs={'pk': like.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, like.post.id)

    def test_api_like_update(self):
        like = PostLike.objects.get()
        new_data = {
            'post': 0
        }
        response = self.client.put(reverse('like_detail', kwargs={'pk': like.id}), data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_api_like_delete(self):
        like = PostLike.objects.get()
        response = self.client.delete(reverse('like_detail', kwargs={'pk': like.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PostLike.objects.count(), 0)


class PostLikeAnalyticsAPITests(PostCreateMixin, APITestCase):

    def setUp(self):
        super().setUp()
        post = Post.objects.get()
        self.like_data = {
            'post': post.id
        }
        self.response = self.client.post(reverse('like_list'), self.like_data, format='json')

    def test_api_like_analytics_today(self):
        likes = PostLike.objects.filter(created=timezone.now().date())
        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)
        response = self.client.get(reverse('like_analytics',
                                           kwargs={'from': f'{today}', 'to': f'{tomorrow}'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, timezone.now().date())
        self.assertContains(response, likes.count())