from rest_framework import routers

from django.urls import include, path


router = routers.DefaultRouter()

app_name = "auth"

urlpatterns = [
    path("", include(router.urls)),
]
