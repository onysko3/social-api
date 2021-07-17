from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post, PostLike


class PostCreateMixin(TestCase):

    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.test_post = Post.objects.create(
            body='content',
            author=self.test_user
        )
        self.post_like = PostLike.objects.create(
            post=self.test_post,
            user=self.test_user
        )


class PostContentTests(PostCreateMixin, TestCase):

    def test_post_body(self):
        self.assertEqual(self.test_post.author, self.test_user)
        self.assertEqual(self.test_post.body, 'content')


class PostLikeTests(PostCreateMixin, TestCase):

    def test_post_like(self):
        self.assertEqual(self.post_like.user, self.test_user)
        self.assertEqual(self.post_like.post, self.test_post)

