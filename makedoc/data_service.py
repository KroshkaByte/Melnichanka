from clients.models import Client


class DataService:
    @staticmethod
    def process_data(data):
        processed_data = data
        return processed_data

    @staticmethod
    def get_client(processed_data):
        try:
            client_id = processed_data.get("client_id")
            client = Client.objects.get(id=client_id)
            client_data = {
                "client_name": str(client.client_name),
                "contract_number": str(client.contract_number),
                "contract_date": str(client.contract_date),
                "director_position": str(client.director_position),
                "director_name": str(client.director_name),
                "destination_city": str(client.destination_city),
                "railway_station": str(client.railway_station),
                "receiver_name": str(client.receiver_name),
                "receiver_id": int(client.receiver_id),
                "receiver_okpo": int(client.receiver_okpo),
                "receiver_adress": str(client.receiver_adress),
                "special_marks": str(client.special_marks),
                "last_application_number": str(client.last_application_number),
            }

            return client_data
        except Client.DoesNotExist:
            raise Exception("Client not found")
