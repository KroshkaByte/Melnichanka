import pytest


@pytest.mark.django_db
def test__clients__return_valid_str(clients_object):
    assert str(clients_object) == clients_object.client_name


@pytest.mark.django_db
def test__director_position__return_valid_str(director_position_object):
    assert str(director_position_object) == director_position_object.director_position
