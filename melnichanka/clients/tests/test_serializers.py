import pytest
from clients.serializers import ClientSerializer


@pytest.mark.django_db
def test__clientserializer__create_object_valid(
    clients_object, destination_city_object, railway_station_object
):
    assert ClientSerializer(clients_object).data == {
        "id": clients_object.id,
        "client_name": "name_client",
        "contract_number": "contract_number",
        "contract_date": "2023-02-22",
        "director_position": "director_position",
        "director_name": "director_name",
        "destination_city": destination_city_object.id,
        "railway_station": railway_station_object.id,
        "receiver_name": "receiver_name",
        "receiver_id": 10000,
        "receiver_okpo": 11111,
        "receiver_adress": "receiver_adress",
        "special_marks": "special_marks",
        "last_application_number": "last_application_number",
    }
