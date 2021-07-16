from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.body[:50]