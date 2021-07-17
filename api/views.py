from django.contrib.auth import get_user_model
from django.db.models import Count
from django.utils import timezone
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, PostLikeSerializer, UserSerializer
from posts.models import Post, PostLike



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostLikeList(generics.ListCreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer


class PostLikeDetail(generics.RetrieveDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer


class PostLikeAnalitycs(generics.ListAPIView):
    serializer_class = PostLikeSerializer

    def get_queryset(self):
        start_date = self.kwargs.get('from')
        end_date = self.kwargs.get('to')
        return PostLike.objects.filter(created__gte=start_date, created__lte=end_date).values(
            'created__date').annotate(likes_count=Count('user')).order_by('created__date')


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

