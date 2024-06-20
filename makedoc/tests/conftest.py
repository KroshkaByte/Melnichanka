import pytest
from faker import Faker
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser

fake = Faker()


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
def test_data():
    return {
        "delivery_type": fake.random_element(elements=("auto", "manual")),
        "client_id": fake.random_int(min=1, max=100),
        "items": [
            {"product_id": fake.random_int(min=1, max=100),
             "quantity": fake.random_int(min=1, max=10),
             "discount": fake.random_int(min=0, max=50)},
            {"product_id": fake.random_int(min=1, max=100),
             "quantity": fake.random_int(min=1, max=10),
             "discount": fake.random_int(min=0, max=50)},
        ],
        "factory_id": fake.random_int(min=1, max=100),
        "destination": fake.city(),
        "delivery_cost": fake.random_int(min=100, max=2000),
    }
