import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestHelloView:
    def test_unauthenticated_request(self, client):
        response = client.get(reverse("users:hello"))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_authenticated_request(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(reverse("users:hello"))
        assert response.status_code == status.HTTP_200_OK

    def test_request_contain_correct_data(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(reverse("users:hello"))
        assert response.data == {"msg": "Hello"}

    def test_authenticated_with_token(self, client, token):
        client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        response = client.get(reverse("users:hello"))
        assert response.status_code == status.HTTP_200_OK
