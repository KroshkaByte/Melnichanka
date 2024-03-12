import pytest
from logistics.models import City, RailwayStations, TripsAuto, TripsRailway


@pytest.mark.django_db
def test__city__create_object_valid(city_object):
    assert city_object.city == "name_city"
    assert city_object.region == "name_region"
    assert city_object.federal_district == "name_federal_district"


@pytest.mark.django_db
def test__city__get_object_valid(city_object):
    retrieved_city = City.objects.get(id=city_object.id)
    assert retrieved_city.city == city_object.city
    assert retrieved_city.region == city_object.region
    assert retrieved_city.federal_district == city_object.federal_district


@pytest.mark.django_db
def test__city__return_valid_str(city_object):
    assert str(city_object) == "name_city, name_region"


@pytest.mark.django_db
def test__tripsauto__create_object_valid(
    tripsauto_object, city_object, city_object_second
):
    assert tripsauto_object.departure_city == city_object
    assert tripsauto_object.destination_city == city_object_second
    assert tripsauto_object.cost_per_tonn_auto == 10000


@pytest.mark.django_db
def test__tripsauto__get_object_valid(tripsauto_object):
    retrieved_tripsauto = TripsAuto.objects.get(id=tripsauto_object.id)
    assert retrieved_tripsauto.departure_city == tripsauto_object.departure_city
    assert retrieved_tripsauto.destination_city == tripsauto_object.destination_city
    assert retrieved_tripsauto.cost_per_tonn_auto == tripsauto_object.cost_per_tonn_auto


@pytest.mark.django_db
def test__tripsauto__return_valid_str(tripsauto_object):
    assert (
        str(tripsauto_object)
        == "name_city, name_region - name_city_second, name_region_second: 10000 руб./тн"
    )


@pytest.mark.django_db
def test__railway_station__create_object_valid(railwaystation_object):
    assert railwaystation_object.station_name == "name_station"
    assert railwaystation_object.station_id == 1000
    assert railwaystation_object.station_branch == "name_branch"


@pytest.mark.django_db
def test__railway_station__get_object_valid(railwaystation_object):
    retrieved_railwaystation = RailwayStations.objects.get(id=railwaystation_object.id)
    assert retrieved_railwaystation.station_name == railwaystation_object.station_name
    assert retrieved_railwaystation.station_id == railwaystation_object.station_id
    assert (
        retrieved_railwaystation.station_branch == railwaystation_object.station_branch
    )


@pytest.mark.django_db
def test__railway_station__return_valid_str(railwaystation_object):
    assert str(railwaystation_object) == "name_station, name_branch"


@pytest.mark.django_db
def test__tripsrailway__create_object_valid(
    tripsrailway_object, railwaystation_object, railwaystation_object_second
):
    assert tripsrailway_object.departure_station_name == railwaystation_object
    assert tripsrailway_object.destination_station_name == railwaystation_object_second
    assert tripsrailway_object.cost_per_tonn_rw == 10000


@pytest.mark.django_db
def test__tripsrailway__get_object_valid(tripsrailway_object):
    retrieved_tripsrailway = TripsRailway.objects.get(id=tripsrailway_object.id)
    assert (
        retrieved_tripsrailway.departure_station_name
        == tripsrailway_object.departure_station_name
    )
    assert (
        retrieved_tripsrailway.destination_station_name
        == tripsrailway_object.destination_station_name
    )
    assert (
        retrieved_tripsrailway.cost_per_tonn_rw == tripsrailway_object.cost_per_tonn_rw
    )


@pytest.mark.django_db
def test__tripsrailway__return_valid_str(tripsrailway_object):
    assert (
        str(tripsrailway_object)
        == "name_station, name_branch - name_station_second, name_branch_second: 10000 руб./тн"
    )
