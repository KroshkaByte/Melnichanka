from datetime import datetime
import pytest
from logistics.models import City, RailwayStations
from clients.models import Clients


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
def clients_object(destination_city_object, railway_station_object):
    return Clients.objects.create(
        id=100,
        client_name="name_client",
        contract_number="contract_number",
        contract_date=datetime.strptime("2023-02-22", "%Y-%m-%d").date(),
        director_position="director_position",
        director_name="director_name",
        destination_city=destination_city_object,
        railway_station=railway_station_object,
        receiver_name="receiver_name",
        receiver_id=10000,
        receiver_okpo=11111,
        receiver_adress="receiver_adress",
        special_marks="special_marks",
        last_application_number="last_application_number",
    )
