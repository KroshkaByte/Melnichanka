from clients.models import Client
from goods.models import Product
from logistics.models import Factory, RailwayStation


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

    @staticmethod
    def get_products(processed_data):
        try:
            products_data = processed_data.get("items")
            results = []
            for item in products_data:
                product_id = item.get("product_id")
                product = Product.objects.get(id=product_id)
                product_data = {
                    "product": product.id,
                    "flour_name": str(product.flour_name),
                    "brand": str(product.brand),
                    "package": str(product.package.package),
                    "price": str(product.price),
                    "quantity": item.get("quantity"),
                    "discount": item.get("discount"),
                }

                results.append(product_data)
            return results
        except Product.DoesNotExist:
            raise Exception("Product not found")

    @staticmethod
    def get_factory(processed_data):
        try:
            factory_id = processed_data.get("factory_id")
            factory = Factory.objects.get(id=factory_id)
            factory_data = {
                "id": int(factory.id),
                "full_name": str(factory.full_name),
                "short_name": str(factory.short_name),
                "full_address": str(factory.full_address),
                "departure_city": str(factory.departure_city),
                "departure_station_branch": str(factory.departure_station_branch),
                "departure_station_id": str(factory.departure_station_id),
                "departure_station_name": str(factory.departure_station_name),
            }
            return factory_data
        except Factory.DoesNotExist:
            raise Exception("Factory not found")

    @staticmethod
    def get_delivery_cost(processed_data):
        delivery_cost = processed_data.get("delivery_cost")
        if delivery_cost is None:
            raise Exception("Delivery cost not found")
        return delivery_cost

    @staticmethod
    def get_city(processed_data):
        city = processed_data.get("destination")
        if city is None:
            raise Exception("City not found")
        return city

    @staticmethod
    def get_rw(processed_data):
        try:
            rw_id = processed_data.get("destination")
            rw = RailwayStation.objects.get(id=rw_id)
            rw_data = {
                "id": int(rw.id),
                "station_name": str(rw.station_name),
                "station_id": int(rw.station_id),
                "station_branch": str(rw.station_branch),
            }
            return rw_data
        except RailwayStation.DoesNotExist:
            raise Exception("Railway station not found")
