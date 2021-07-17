from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Post(models.Model):
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:50]


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_like'),
        ]


@receiver(pre_save, sender=PostLike)
def add_profile_slug(sender, instance, *args, **kwargs):
    try:
        like = PostLike.objects.get(post=instance.post, user=instance.user)
        like.delete()
    except ObjectDoesNotExist:
        pass
