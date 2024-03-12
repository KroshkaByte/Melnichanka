import pytest
from logistics.models import City, RailwayStations, TripsAuto, TripsRailway


@pytest.fixture
def city_object():
    return City.objects.create(
        city="name_city", region="name_region", federal_district="name_federal_district"
    )


@pytest.fixture
def city_object_second():
    return City.objects.create(
        city="name_city_second",
        region="name_region_second",
        federal_district="name_federal_district_second",
    )


@pytest.fixture
def tripsauto_object(city_object, city_object_second):
    return TripsAuto.objects.create(
        departure_city=city_object,
        destination_city=city_object_second,
        cost_per_tonn_auto=10000,
    )


@pytest.fixture
def railwaystation_object():
    return RailwayStations.objects.create(
        station_name="name_station",
        station_id=1000,
        station_branch="name_branch",
    )


@pytest.fixture
def railwaystation_object_second():
    return RailwayStations.objects.create(
        station_name="name_station_second",
        station_id=1000,
        station_branch="name_branch_second",
    )


@pytest.fixture
def tripsrailway_object(railwaystation_object, railwaystation_object_second):
    return TripsRailway.objects.create(
        departure_station_name=railwaystation_object,
        destination_station_name=railwaystation_object_second,
        cost_per_tonn_rw=10000,
    )
