from django.urls import path
from .views import (
    PostList,
    PostDetail,
    UserList,
    UserDetail,
)


urlpatterns = [
    # Posts
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/', PostList.as_view()),

    # Users
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/', UserList.as_view()),
]