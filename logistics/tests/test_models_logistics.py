import pytest


@pytest.mark.django_db
def test__tripsauto__return_valid_str(tripsauto_object):
    assert (
        str(tripsauto_object)
        == f"{tripsauto_object.departure_city} - {tripsauto_object.destination_city}: {tripsauto_object.cost_per_tonn_auto} руб./тн"
    )


@pytest.mark.django_db
def test__railway_station__return_valid_str(railwaystation_object):
    assert (
        str(railwaystation_object)
        == f"{railwaystation_object.station_name}, {railwaystation_object.station_branch}, {railwaystation_object.station_id}"
    )


@pytest.mark.django_db
def test__tripsrailway__return_valid_str(tripsrailway_object):
    assert (
        str(tripsrailway_object)
        == f"{tripsrailway_object.departure_station_name} - {tripsrailway_object.destination_station_name}: {tripsrailway_object.cost_per_tonn_rw} руб./тн"
    )


@pytest.mark.django_db
def test__city__return_valid_str(city_object):
    assert str(city_object) == f"{city_object.city}, {city_object.region}"
