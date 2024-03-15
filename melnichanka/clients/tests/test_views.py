import pytest

from django.test import RequestFactory
from rest_framework.test import force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from clients.views import ClientsAPIView, ClientAPIUpdateView, ClientAPIDeleteView
from users.models import CustomUser


@pytest.mark.django_db
def test__client_api_view__list_object_valid(clients_object):
    user = CustomUser.objects.create_user(
        email="testuser@test.com", full_name="Test User", password="testpass"
    )
    refresh = RefreshToken.for_user(user)
    factory = RequestFactory()
    request = factory.get("/")
    force_authenticate(request, user=user, token=refresh)
    response = ClientsAPIView.as_view()(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test__client_api_view__update_object_valid(clients_object, user):
    refresh = RefreshToken.for_user(user)
    factory = RequestFactory()
    request = factory.get("/")
    force_authenticate(request, user=user, token=refresh)
    response = ClientAPIUpdateView.as_view()(request, pk=clients_object.pk)
    assert response.status_code == 200


@pytest.mark.django_db
def test__client_api_view__delete_object_valid(clients_object, user):
    refresh = RefreshToken.for_user(user)
    factory = RequestFactory()
    request = factory.delete("/")
    force_authenticate(request, user=user, token=refresh)
    response = ClientAPIDeleteView.as_view()(request, pk=clients_object.pk)
    assert response.status_code == 204
