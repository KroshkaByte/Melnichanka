import pytest

from clients.models import Client
from clients.views import BaseView


@pytest.mark.django_db
def test__base_view__queryset(clients_object):
    view = BaseView()
    clients = view.queryset
    assert isinstance(clients, type(Client.objects.all()))
    assert clients.count() == 1
    assert clients.first().client_name == clients_object.client_name
    assert clients.filter(client_name="non-existent name").count() == 0
