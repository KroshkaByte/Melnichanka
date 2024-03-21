import pytest


@pytest.mark.django_db
def test__tripsauto__return_valid_str(tripsauto_object):
    assert (
        str(tripsauto_object)
        == "name_city, name_region - name_city, name_region: 10000 руб./тн"
    )


@pytest.mark.django_db
def test__railway_station__return_valid_str(railwaystation_object):
    assert str(railwaystation_object) == "name_station, name_branch"


@pytest.mark.django_db
def test__tripsrailway__return_valid_str(tripsrailway_object):
    assert (
        str(tripsrailway_object)
        == "name_station, name_branch - name_station, name_branch: 10000 руб./тн"
    )
