from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post


class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

        test_post = Post.objects.create(
            body='content',
            author=test_user
        )

    def test_post_body(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(body, 'content')
