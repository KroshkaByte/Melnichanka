from clients.models import Client
from goods.models import Product
from logistics.models import Factory, RailwayStation


class DataService:
    @staticmethod
    def get_delivery_type(validated_data):
        delivery_type = validated_data.get("delivery_type")
        if delivery_type is None:
            raise Exception("Type delivery not found")
        return delivery_type

    @staticmethod
    def get_client(validated_data):
        try:
            client_id = validated_data.get("client_id")
            client = Client.objects.get(id=client_id)
            return client
        except Client.DoesNotExist:
            raise Exception("Client not found")

    @staticmethod
    def get_products(validated_data):
        try:
            products_data = validated_data.get("items")
            results = []
            for item in products_data:
                product_id = item.get("product_id")
                product_quantity = item.get("quantity")
                product_discount = item.get("discount")
                product = Product.objects.get(id=product_id)
                results.append(product)
                results.append(product_quantity)
                results.append(product_discount)
            return results
        except Product.DoesNotExist:
            raise Exception("Product not found")

    @staticmethod
    def get_factory(validated_data):
        try:
            factory_id = validated_data.get("factory_id")
            factory = Factory.objects.get(id=factory_id)
            return factory
        except Factory.DoesNotExist:
            raise Exception("Factory not found")

    @staticmethod
    def get_delivery_cost(validated_data):
        delivery_cost = validated_data.get("delivery_cost")
        if delivery_cost is None:
            raise Exception("Delivery cost not found")
        return delivery_cost

    @staticmethod
    def get_city(validated_data):
        city = validated_data.get("destination")
        if city is None:
            raise Exception("City not found")
        return city

    @staticmethod
    def get_rw(validated_data):
        try:
            rw_id = validated_data.get("destination")
            rw = RailwayStation.objects.get(id=rw_id)
            return rw
        except RailwayStation.DoesNotExist:
            raise Exception("Railway station not found")

    @staticmethod
    def get_user(request):
        user = request.user
        if user:
            return user
        else:
            raise Exception("User is not authenticated")
