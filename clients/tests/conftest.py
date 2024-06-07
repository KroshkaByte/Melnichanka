import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from clients.models import Client, DirectorPosition
from logistics.models import City, RailwayStation
from users.models import CustomUser


@pytest.fixture
def director_position_object(faker):
    return DirectorPosition.objects.create(director_position=faker.word())


@pytest.fixture
def destination_city_object(faker):
    return City.objects.create(city=faker.city(), region=faker.word())


@pytest.fixture
def railway_station_object(faker):
    return RailwayStation.objects.create(station_name=faker.word(), station_branch=faker.word(),
                                         station_id=faker.random_int())


@pytest.fixture
def clients_object(director_position_object, destination_city_object, railway_station_object, user,
                   faker):
    return Client.objects.create(
        client_name=faker.company(),
        contract_number=faker.word(),
        contract_date=faker.date(),
        director_position=director_position_object,
        director_name=faker.last_name(),
        destination_city=destination_city_object,
        railway_station=railway_station_object,
        receiver_name=faker.company(),
        receiver_id=faker.random_int(),
        receiver_okpo=faker.random_int(),
        receiver_adress=faker.address(),
        special_marks=faker.text(),
        last_application_number=faker.word(),
        user=user,
    )


@pytest.fixture
def user(faker):
    return CustomUser.objects.create_user(email=faker.email(), full_name=faker.name(),
                                          password=faker.password())


@pytest.fixture
def authorized_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}")
    return client
