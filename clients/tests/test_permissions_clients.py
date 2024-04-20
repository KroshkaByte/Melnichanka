import pytest
from django.test import RequestFactory
from rest_framework.exceptions import PermissionDenied

from clients.permissions import ClientAccessPermission
from users.models import CustomUser


@pytest.mark.django_db
def test__client_access_permission__has_permission_authenticated_user():
    user = CustomUser.objects.create_user(
        email="user@test.com", full_name="Test User", password="testpass"
    )
    permission = ClientAccessPermission()
    factory = RequestFactory()
    request = factory.get("/")
    request.user = user

    assert permission.has_permission(request, view=None)


@pytest.mark.django_db
def test__client_access_permission__has_object_permission(clients_object):
    user = clients_object.user
    permission = ClientAccessPermission()
    factory = RequestFactory()
    request = factory.get("/")
    request.user = user

    assert permission.has_object_permission(request, view=None, obj=clients_object)


@pytest.mark.django_db
def test__client_access_permission__has_object_permission_other_user(clients_object):
    other_user = CustomUser.objects.create_user(
        email="otheruser@test.com", full_name="Other User", password="testpass"
    )
    permission = ClientAccessPermission()
    factory = RequestFactory()
    request = factory.get("/")
    request.user = other_user

    with pytest.raises(PermissionDenied):
        permission.has_object_permission(request, view=None, obj=clients_object)
