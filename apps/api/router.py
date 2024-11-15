from django.urls import include, path
from rest_framework import routers

from apps.api.views.post import PostView, PostDetailView, CommentCreateView

router = routers.DefaultRouter()


app_name = "api"

urlpatterns = [
    path("v1/", include(router.urls), name="api"),
    path("post/", PostView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("comment/<int:post>/", CommentCreateView.as_view(), name="comment_create")
]
