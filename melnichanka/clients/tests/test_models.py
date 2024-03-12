from datetime import datetime
import pytest
from clients.models import Clients


@pytest.mark.django_db
def test__clients__create_object_valid(
    clients_object, destination_city_object, railway_station_object
):
    assert clients_object.client_name == "name_client"
    assert clients_object.contract_number == "contract_number"
    assert (
        clients_object.contract_date
        == datetime.strptime("2023-02-22", "%Y-%m-%d").date()
    )
    assert clients_object.director_position == "director_position"
    assert clients_object.director_name == "director_name"
    assert clients_object.destination_city == destination_city_object
    assert clients_object.railway_station == railway_station_object
    assert clients_object.receiver_name == "receiver_name"
    assert clients_object.receiver_id == 10000
    assert clients_object.receiver_okpo == 11111
    assert clients_object.receiver_adress == "receiver_adress"
    assert clients_object.special_marks == "special_marks"
    assert clients_object.last_application_number == "last_application_number"


@pytest.mark.django_db
def test__clients__get_object_valid(clients_object):
    retrieved_clients = Clients.objects.get(id=clients_object.id)
    assert retrieved_clients.client_name == clients_object.client_name
    assert retrieved_clients.contract_number == clients_object.contract_number
    assert retrieved_clients.contract_date == clients_object.contract_date
    assert retrieved_clients.director_position == clients_object.director_position
    assert retrieved_clients.director_name == clients_object.director_name
    assert retrieved_clients.destination_city == clients_object.destination_city
    assert retrieved_clients.railway_station == clients_object.railway_station
    assert retrieved_clients.receiver_name == clients_object.receiver_name
    assert retrieved_clients.receiver_id == clients_object.receiver_id
    assert retrieved_clients.receiver_okpo == clients_object.receiver_okpo
    assert retrieved_clients.receiver_adress == clients_object.receiver_adress
    assert retrieved_clients.special_marks == clients_object.special_marks
    assert (
        retrieved_clients.last_application_number
        == clients_object.last_application_number
    )


@pytest.mark.django_db
def test__clients__return_valid_str(clients_object):
    assert str(clients_object) == "name_client"
