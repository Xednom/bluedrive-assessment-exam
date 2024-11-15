from rest_framework import serializers
from rest_framework.generics import CreateAPIView, get_object_or_404


from apps.api.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["content", "created_at"]


class CreatePostComment(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.select_related("post").all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get("id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(post=post)
