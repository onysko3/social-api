from django.urls import path
from .views import (
    PostList,
    PostDetail,
    PostLikeList,
    PostLikeDetail,
    PostLikeAnalitycs,
    UserList,
    UserDetail,
)


urlpatterns = [
    # Posts
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/likes/', PostLikeList.as_view()),
    path('posts/likes/analytics/from=<str:from>&to=<str:to>', PostLikeAnalitycs.as_view()),
    path('posts/likes/<int:pk>/', PostLikeDetail.as_view()),

    # Users
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/', UserList.as_view()),
]