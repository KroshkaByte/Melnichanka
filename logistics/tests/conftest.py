import pytest

from logistics.models import City, RailwayStation, TripAuto, TripRailway


@pytest.fixture
def tripsauto_object(city_object, faker):
    return TripAuto.objects.create(
        departure_city=city_object,
        destination_city=city_object,
        cost_per_tonn_auto=faker.pyint(),
    )


@pytest.fixture
def railwaystation_object(faker):
    return RailwayStation.objects.create(
        station_name=faker.pystr(),
        station_id=faker.pyint(),
        station_branch=faker.pystr(),
    )


@pytest.fixture
def tripsrailway_object(railwaystation_object, faker):
    return TripRailway.objects.create(
        departure_station_name=railwaystation_object,
        destination_station_name=railwaystation_object,
        cost_per_tonn_rw=faker.pyint(),
    )


@pytest.fixture
def city_object(faker):
    return City.objects.create(
        city=faker.pystr(), region=faker.pystr(), federal_district=faker.pystr()
    )
