import pytest

from clients.serializers import ClientSerializer


@pytest.mark.django_db
def test__client_serializer__create_object_valid_id(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["id"] == clients_object.id


@pytest.mark.django_db
def test__client_serializer__create_object_valid_client_name(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["client_name"] == clients_object.client_name


@pytest.mark.django_db
def test__client_serializer__create_object_valid_contract_number(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["contract_number"] == clients_object.contract_number


@pytest.mark.django_db
def test__client_serializer__create_object_valid_contract_date(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["contract_date"] == clients_object.contract_date


@pytest.mark.django_db
def test__client_serializer__create_object_valid_director_position(
    director_position_object,
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["director_position"] == director_position_object.id


@pytest.mark.django_db
def test__client_serializer__create_object_valid_director_name(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["director_name"] == clients_object.director_name


@pytest.mark.django_db
def test__client_serializer__create_object_valid_destination_city(
    clients_object,
    destination_city_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["destination_city"] == destination_city_object.id


@pytest.mark.django_db
def test__client_serializer__create_object_valid_railway_station(
    clients_object,
    railway_station_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["railway_station"] == railway_station_object.id


@pytest.mark.django_db
def test__client_serializer__create_object_valid_receiver_name(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["receiver_name"] == clients_object.receiver_name


@pytest.mark.django_db
def test__client_serializer__create_object_valid_receiver_id(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["receiver_id"] == clients_object.receiver_id


@pytest.mark.django_db
def test__client_serializer__create_object_valid_receiver_okpo(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["receiver_okpo"] == clients_object.receiver_okpo


@pytest.mark.django_db
def test__client_serializer__create_object_valid_receiver_adress(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["receiver_adress"] == clients_object.receiver_adress


@pytest.mark.django_db
def test__client_serializer__create_object_valid_special_marks(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["special_marks"] == clients_object.special_marks


@pytest.mark.django_db
def test__client_serializer__create_object_valid_last_application_number(
    clients_object,
):
    serializer_data = ClientSerializer(clients_object).data
    assert serializer_data["last_application_number"] == clients_object.last_application_number
