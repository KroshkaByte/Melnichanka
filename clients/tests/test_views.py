import pytest


@pytest.mark.django_db
def test__client_api_view__list_object_valid(authorized_client, clients_object):
    response = authorized_client.get("/api/v1/clients/")
    assert response.status_code == 200


@pytest.mark.django_db
def test__client_api_view__update_object_valid(authorized_client, clients_object):
    response = authorized_client.get(f"/api/v1/clients/{clients_object.pk}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test__client_api_view__delete_object_valid(authorized_client, clients_object):
    response = authorized_client.delete(f"/api/v1/clients/delete/{clients_object.pk}/")
    assert response.status_code == 204
