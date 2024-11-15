from django.urls import include, path
from rest_framework import routers

from apps.api.resources.post import PostAPIView, PostDetailView


router = routers.DefaultRouter()

urlpatterns = [
    path("v1/", include(router.urls), name="api"),
    path("post/", PostAPIView.as_view(), name="post_list"),
    path("post/<int:id>/", PostDetailView.as_view(), name="post_detail"),
]
