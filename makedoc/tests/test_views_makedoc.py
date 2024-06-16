import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test__data_doc_view__unauthorized_user_cannot_post_data() -> None:
    client = APIClient()
    url = reverse("data")
    data = {
        "delivery_type": "auto",
        "client_id": 1,
        "items": [
            {"product_id": 1, "quantity": 2, "discount": 10},
            {"product_id": 2, "quantity": 5, "discount": 4},
        ],
        "factory_id": 1,
        "destination": "New York",
        "delivery_cost": 1500,
    }
    response = client.post(url, data, format="json")
    assert response.status_code == 401  # Unauthorized


@pytest.mark.django_db
def test__data_doc_view__authorized_user_can_post_data(authorized_client) -> None:
    url = reverse("data")
    data = {
        "delivery_type": "auto",
        "client_id": 1,
        "items": [
            {"product_id": 1, "quantity": 2, "discount": 10},
            {"product_id": 2, "quantity": 5, "discount": 4},
        ],
        "factory_id": 1,
        "destination": "New York",
        "delivery_cost": 1500,
    }
    response = authorized_client.post(url, data, format="json")
    assert response.status_code == 200


@pytest.mark.django_db
def test__data_doc_view__authorized_user_post_data_response_is_correct(authorized_client) -> None:
    url = reverse("data")
    data = {
        "delivery_type": "auto",
        "client_id": 1,
        "items": [
            {"product_id": 1, "quantity": 2, "discount": 10},
            {"product_id": 2, "quantity": 5, "discount": 4},
        ],
        "factory_id": 1,
        "destination": "New York",
        "delivery_cost": 1500,
    }
    response = authorized_client.post(url, data, format="json")
    assert response.json() == {"success": True, "data": data}
