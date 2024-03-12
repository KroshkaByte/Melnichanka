import pytest
from clients.views import ClientsViewSet


@pytest.mark.django_db
def test__clientsviewset__list_object_valid(clients_object):
    response = ClientsViewSet.as_view({"get": "list"})()
    assert response.status_code == 200
    assert response.data == [{"id": clients_object.id}]


@pytest.mark.django_db
def test__clientsviewset__retrieve_object_valid(clients_object):
    response = ClientsViewSet.as_view({"get": "retrieve"})()
    assert response.status_code == 200
    assert response.data == {"id": clients_object.id}
