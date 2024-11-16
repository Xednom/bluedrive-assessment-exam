import pytest
import logging


from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from apps.api.models import Post, Comment, Author

logger = logging.getLogger(__name__)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_author(db):
    return Author.objects.create(name="Mr. Author", email="author@example.com")


@pytest.fixture
def create_posts(db, create_author):
    Post.objects.create(
        title="First post",
        content={"content": "Content of the first post"},
        published_date="2024-01-01",
        author=create_author,
    )

    Post.objects.create(
        title="Second post",
        content={"content": "Content of the second post"},
        published_date="2024-01-02",
        author=create_author,
    )


@pytest.fixture
def create_post(db, create_author):
    return Post.objects.create(
        title="Single post",
        content={"content": "A post for comments"},
        published_date="2024-02-14",
        author=create_author,
    )


@pytest.mark.django_db
def test_list_posts(api_client, create_posts):
    url = reverse("post_list")
    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK, "Successful listed all posts"
    assert len(response.json()["results"]) == 2, "Correct number of posts returned"


@pytest.mark.django_db
def test_filter_posts_by_title(api_client, create_posts):
    url = reverse("post_list")
    response = api_client.get(url, {"title": "First post"})

    assert (
        response.status_code == status.HTTP_200_OK
    ), "Successfully filtered posts by title"
    results = response.json()["results"]
    assert results[0]["title"] == "First post", "Filtered post title match"


@pytest.mark.django_db
def test_fail_filter_posts_by_title(api_client, create_posts):
    url = reverse("post_list")
    response = api_client.get(url, {"title": "First Post"})

    assert response.status_code == status.HTTP_200_OK, "Failed to filter posts by title"
    assert (
        len(response.json()["results"]) == 2
    ), "Incorrect number of posts returned for title"


@pytest.mark.django_db
def test_filter_posts_by_author_name(api_client, create_posts):
    url = reverse("post_list")
    response = api_client.get(url, {"author": "Mr. Author"})
    assert (
        response.status_code == status.HTTP_200_OK
    ), "Successfully filtered posts by author name"
    assert (
        len(response.json()["results"]) == 2
    ), "Correct number of posts returned for author"


@pytest.mark.django_db
def test_fail_filter_posts_by_author_name(api_client, create_posts):
    url = reverse("post_list")
    response = api_client.get(url, {"author": "Mr. author"})
    assert (
        response.status_code == status.HTTP_200_OK
    ), "Failed to filter posts by author name"
    assert (
        len(response.json()["results"]) == 0
    ), "Incorrect number of posts returned for author"


@pytest.mark.django_db
def test_create_post(api_client, create_author):
    data = {
        "title": "New Post Title",
        "content": "Content of a new post",
        "author": create_author.id,
    }
    url = reverse("post_create")
    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_fail_create_post(api_client, create_author):
    data = {
        "title": "New Post Title",
        "content": "Content of a new post",
        "author": create_author.id,
    }
    url = reverse("post_create")
    response = api_client.post(url, data, format="json")

    assert (
        response.status_code == status.HTTP_400_BAD_REQUEST
    ), f"Expected failure for post creation, but got {response.status_code} instead"


@pytest.mark.django_db
def test_create_post_comment(api_client, create_post):
    data = {"post": create_post.id, "content": "Content of the Create Post Comment"}
    url = reverse("create_post_comment", kwargs={"id": create_post.id})
    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_fail_create_post_comment(api_client, create_post):
    data = {"post": create_post.id, "content": "Content of the Create Post Comment"}
    url = reverse("create_post_comment", kwargs={"id": create_post.id})
    response = api_client.post(url, data, format="json")

    assert (
        response.status_code == status.HTTP_400_BAD_REQUEST
    ), f"Expected failure for creating a comment in a post, but got {response.status_code} instead"
