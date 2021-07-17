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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Social Network API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    # Posts
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/likes/', PostLikeList.as_view(), name='like_list'),
    path('posts/likes/analytics/from=<str:from>&to=<str:to>', PostLikeAnalitycs.as_view(), name='like_analytics'),
    path('posts/likes/<int:pk>/', PostLikeDetail.as_view(), name='like_detail'),

    # Users
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('users/', UserList.as_view(), name='user_list'),

    # Schema
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]