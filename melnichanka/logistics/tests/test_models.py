import pytest


@pytest.mark.django_db
def test__tripsauto__return_valid_str(tripsauto_object):
    assert (
        str(tripsauto_object)
        == "name_city, name_region - name_city_second, name_region_second: 10000 руб./тн"
    )


@pytest.mark.django_db
def test__railway_station__return_valid_str(railwaystation_object):
    assert str(railwaystation_object) == "name_station, name_branch"


@pytest.mark.django_db
def test__tripsrailway__return_valid_str(tripsrailway_object):
    assert (
        str(tripsrailway_object)
        == "name_station, name_branch - name_station_second, name_branch_second: 10000 руб./тн"
    )
