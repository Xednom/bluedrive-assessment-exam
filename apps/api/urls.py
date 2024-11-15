from django.urls import include, path

from apps.api.views.post import PostView, PostDetailView, CommentCreateView

app_name = "api"

urlpatterns = [
    path("post/", PostView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:post>/comment/", CommentCreateView.as_view(), name="comment_create")
]