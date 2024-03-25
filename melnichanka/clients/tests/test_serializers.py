import pytest

from clients.serializers import ClientSerializer


@pytest.mark.django_db
def test__client_serializer__create_object_valid(
    director_position_object,
    clients_object,
    destination_city_object,
    railway_station_object,
    user,
):
    serializer_data = ClientSerializer(clients_object).data

    assert serializer_data["id"] == clients_object.id
    assert serializer_data["client_name"] == "name_client"
    assert serializer_data["contract_number"] == "contract_number"
    assert serializer_data["contract_date"] == "2023-02-22"
    assert serializer_data["director_position"] == director_position_object.id
    assert serializer_data["director_name"] == "director_name"
    assert serializer_data["destination_city"] == destination_city_object.id
    assert serializer_data["railway_station"] == railway_station_object.id
    assert serializer_data["receiver_name"] == "receiver_name"
    assert serializer_data["receiver_id"] == 10000
    assert serializer_data["receiver_okpo"] == 11111
    assert serializer_data["receiver_adress"] == "receiver_adress"
    assert serializer_data["special_marks"] == "special_marks"
    assert serializer_data["last_application_number"] == "last_application_number"
