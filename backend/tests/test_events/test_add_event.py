import pytest
from django.urls import reverse
from rest_framework import status

uri = reverse("events:add")


@pytest.mark.django_db
class TestAddEventView:
    def test_auth_user_add_event(self, client, user):
        client.force_authenticate(user=user)
        response = client.post(uri, dict(name="test event name"))
        assert response.status_code == status.HTTP_201_CREATED

    def test_not_auth_user_not_add_event(self, client):
        response = client.post(uri, dict(name="test event name"))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_auth_user_not_add_event(self, client, user):
        client.force_authenticate(user=user)
        response = client.post(uri)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
