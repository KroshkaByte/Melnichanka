import pytest
from clients.views import ClientsViewSet
from django.test import RequestFactory
from rest_framework.test import force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser


@pytest.mark.django_db
def test__clientsviewset__list_object_valid(clients_object):
    user = CustomUser.objects.create_user(
        email="testuser@test.com", full_name="Test User", password="testpass"
    )
    refresh = RefreshToken.for_user(user)
    factory = RequestFactory()
    request = factory.get("/")
    force_authenticate(request, user=user, token=refresh)
    response = ClientsViewSet.as_view({"get": "retrieve"})(
        request, pk=clients_object.pk
    )
    assert response.status_code == 200
