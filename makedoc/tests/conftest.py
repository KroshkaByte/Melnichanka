import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser


@pytest.fixture
def user(django_user_model):
    return CustomUser.objects.create_user(
        email="test@example.com", full_name="Test User", password="testpassword"
    )


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}")
    client.user = user
    return client


@pytest.fixture
def make_test_data(faker):
    return {
        "delivery_type": faker.random_element(elements=("auto", "rw", "self-delivery")),
        "client_id": faker.random_int(min=1, max=100),
        "items": [
            {
                "product_id": faker.random_int(min=1, max=100),
                "quantity": faker.random_int(min=1, max=10),
                "discount": faker.random_int(min=0, max=100),
            },
            {
                "product_id": faker.random_int(min=1, max=100),
                "quantity": faker.random_int(min=1, max=10),
                "discount": faker.random_int(min=0, max=100),
            },
        ],
        "factory_id": faker.random_int(min=1, max=100),
        "destination": faker.city(),
        "delivery_cost": faker.random_int(min=0, max=5000),
    }
