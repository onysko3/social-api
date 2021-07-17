from django.contrib.auth import get_user_model
from rest_framework import serializers
from posts.models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('pk', 'author', 'body', 'likes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLike
        fields = ('pk', 'post', 'user', 'created')
        read_only_fields = ('created',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'last_login', 'last_activity')
