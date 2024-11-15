import pytest, uuid

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.management import call_command
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client():
    User.objects.create_user(username="auth-tester", password="password")
    client = APIClient()
    client.login(username="auth-tester", password="password")
    return client


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user

    return make_auto_login
