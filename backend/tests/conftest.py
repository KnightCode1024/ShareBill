import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from api.v1.events.models import EventGroup, Event


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        username="test_user", password="QwErty123#", email="test@example.com"
    )


@pytest.fixture
def token(user):
    return Token.objects.create(user=user)


@pytest.fixture
def auth_client(client, token):
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return client


@pytest.fixture
def organizer_user():
    return get_user_model().objects.create_user(
        username="organizer",
        password="testpass123",
        email="organizer@example.com",
    )


@pytest.fixture
def regular_user():
    return get_user_model().objects.create_user(
        username="regular",
        password="testpass123",
        email="regular@example.com",
    )


@pytest.fixture
def event_group(organizer_user):
    group = EventGroup.objects.create(name="Test Group")
    group.participants.add(organizer_user)
    return group


@pytest.fixture
def event(organizer_user, event_group):
    return Event.objects.create(
        title="Test Event",
        description="Test Description",
        organizer=organizer_user,
        group=event_group,
    )
