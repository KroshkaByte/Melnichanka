import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_data_doc_view_status_code(api_client: APIClient) -> None:
    url = reverse('data')
    data = {
        "client_id": 123,
        "items": [
            {"product_id": 1, "quantity": 2, "discount": 10},
            {"product_id": 2, "quantity": 5, "discount": 4}
        ],
        "factory_id": 1,
        "destination": "New York"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 401  # Unauthorized


@pytest.mark.django_db
def test_data_doc_view_response_data(authorized_client) -> None:
    url = reverse('data')
    data = {
        "client_id": 123,
        "items": [
            {"product_id": 1, "quantity": 2, "discount": 10},
            {"product_id": 2, "quantity": 5, "discount": 4}
        ],
        "factory_id": 1,
        "destination": "New York"
    }
    response = authorized_client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.json() == data
