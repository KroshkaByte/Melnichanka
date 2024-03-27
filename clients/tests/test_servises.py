import pytest

from clients.models import Clients
from clients.views import BaseView


@pytest.mark.django_db
def test__base_view__queryset(clients_object):
    view = BaseView()
    clients = view.queryset
    assert isinstance(clients, type(Clients.objects.all()))
    assert clients.count() == 1
    assert clients.first().client_name == "name_client"
    assert clients.filter(client_name="name_client2").count() == 0
