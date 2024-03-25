import pytest


@pytest.mark.django_db
def test__clients__return_valid_str(clients_object):
    assert str(clients_object) == "name_client"
