from django.urls import include, path
from rest_framework import routers

from apps.api.resources.post import PostAPIView


router = routers.DefaultRouter()

urlpatterns = [
    path("v1/", include(router.urls), name="api"),
    path("post/", PostAPIView.as_view(), name="post_list"),
]
