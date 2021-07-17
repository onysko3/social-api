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
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/likes/', PostLikeList.as_view()),
    path('posts/likes/analytics/from=<str:from>&to=<str:to>', PostLikeAnalitycs.as_view()),
    path('posts/likes/<int:pk>/', PostLikeDetail.as_view()),

    # Users
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users/', UserList.as_view()),

    # Schema
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]