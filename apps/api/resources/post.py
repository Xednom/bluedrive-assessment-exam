from rest_framework import serializers, permissions, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.api.models import Post


class PostFilter(filters.FilterSet):
    author_name = filters.CharFilter(field_name="author__name", lookup_expr="icontains")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Post
        fields = ["title", "author_name", "published_date"]


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "published_date", "author_name"]


class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
