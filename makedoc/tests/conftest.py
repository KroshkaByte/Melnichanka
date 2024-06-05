import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser


@pytest.fixture
def user(django_user_model):
    return CustomUser.objects.create_user(email='test@example.com', full_name='Test User',
                                          password='testpassword')


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}")
    return client
