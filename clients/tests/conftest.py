import pytest

from datetime import datetime
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from logistics.models import City, RailwayStations
from clients.models import Clients, Director_position
from users.models import CustomUser


@pytest.fixture
def director_position_object():
    return Director_position.objects.create(id=100, director_position="director_position")


@pytest.fixture
def destination_city_object():
    return City.objects.create(
        id=100,
        city="name_destination_city",
        region="name_region",
        federal_district="name_federal_district",
    )


@pytest.fixture
def railway_station_object():
    return RailwayStations.objects.create(
        id=100,
        station_name="name_station",
        station_id=1000,
        station_branch="name_branch",
    )


@pytest.fixture
def clients_object(
    director_position_object, destination_city_object, railway_station_object, user
):
    return Clients.objects.create(
        id=100,
        client_name="name_client",
        contract_number="contract_number",
        contract_date=datetime.strptime("2023-02-22", "%Y-%m-%d").date(),
        director_position=director_position_object,
        director_name="director_name",
        destination_city=destination_city_object,
        railway_station=railway_station_object,
        receiver_name="receiver_name",
        receiver_id=10000,
        receiver_okpo=11111,
        receiver_adress="receiver_adress",
        special_marks="special_marks",
        last_application_number="last_application_number",
        user=user,
    )


@pytest.fixture
def user():
    return CustomUser.objects.create_user(
        email="testclientuser@test.com", full_name="Test User", password="testpass"
    )


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}")
    return client
