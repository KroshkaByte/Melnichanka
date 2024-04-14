import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from clients.models import Client, Director_position
from logistics.models import City, RailwayStation
from users.models import CustomUser


@pytest.fixture
def director_position_object(faker):
    return Director_position.objects.create(id=faker.pyint(), director_position=faker.pystr())


@pytest.fixture
def destination_city_object(faker):
    return City.objects.create(
        id=faker.pyint(),
        city=faker.city(),
        region=faker.pystr(),
        federal_district=faker.pystr(),
    )


@pytest.fixture
def railway_station_object(faker):
    return RailwayStation.objects.create(
        id=faker.pyint(),
        station_name=faker.pystr(),
        station_id=faker.pyint(),
        station_branch=faker.pystr(),
    )


@pytest.fixture
def clients_object(
    director_position_object, destination_city_object, railway_station_object, user, faker
):
    return Client.objects.create(
        id=faker.pyint(),
        client_name=faker.company(),
        contract_number=faker.pystr(),
        contract_date=faker.date(),
        director_position=director_position_object,
        director_name=faker.last_name(),
        destination_city=destination_city_object,
        railway_station=railway_station_object,
        receiver_name=faker.company(),
        receiver_id=faker.pyint(),
        receiver_okpo=faker.pyint(),
        receiver_adress=faker.address(),
        special_marks=faker.pystr(),
        last_application_number=faker.pystr(),
        user=user,
    )


@pytest.fixture
def user(faker):
    return CustomUser.objects.create_user(
        email=faker.email(), full_name=faker.name(), password=faker.password()
    )


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}")
    return client
