from django.core.cache import cache

from clients.models import Client
from goods.models import Product
from logistics.models import Factory


class DataService:
    """
    Service class providing methods to retrieve and validate data related to delivery,
    clients, products, factories, delivery costs, destination cities, and authenticated users.
    """

    @staticmethod
    def get_delivery_type(validated_data):
        """
        Retrieves the delivery type from validated data.
        """
        delivery_type = validated_data.get("delivery_type")
        if delivery_type is None:
            raise Exception("Delivery type not found")
        return delivery_type

    @staticmethod
    def get_client(validated_data):
        """
        Retrieves the client object based on the client ID from validated data.
        """
        try:
            client_id = validated_data.get("client_id")
            client = Client.objects.get(id=client_id)
            return client
        except Client.DoesNotExist:
            raise Exception("Client not found")

    @staticmethod
    def get_products(validated_data):
        """
        Retrieves a list of products with quantities, discounts,
        and prices based on product IDs from validated data.
        """
        products_data = validated_data.get("items")
        results = []
        cached_goods = cache.get("goods_list")
        if cached_goods is None:
            cached_goods = Product.objects.select_related("flour_name", "brand", "package").all()
        for item in products_data:
            product_id = item.get("product_id")
            product_quantity = item.get("quantity")
            product_discount = item.get("discount")
            for product in cached_goods:
                if product.id == product_id:
                    results.append(
                        {
                            "product": product,
                            "quantity": product_quantity,
                            "discount": product_discount,
                            "price": product.price,
                        }
                    )
                    break
        return results

    @staticmethod
    def get_factory(validated_data):
        """
        Retrieves the factory object based on the factory ID from validated data.
        """
        try:
            factory_id = validated_data.get("factory_id")
            cached_factories = cache.get("factories_list")
            if cached_factories:
                for factory in cached_factories:
                    if factory.id == factory_id:
                        return factory
            factory = Factory.objects.get(id=factory_id)
            return factory
        except Factory.DoesNotExist:
            raise Exception("Factory not found")

    @staticmethod
    def get_delivery_cost(validated_data):
        """
        Retrieves the delivery cost from validated data.
        """
        delivery_cost = validated_data.get("delivery_cost")
        if delivery_cost is None:
            raise Exception("Delivery cost not found")
        return delivery_cost

    @staticmethod
    def get_destination(validated_data):
        """
        Retrieves the destination city from validated data.
        """
        destination = validated_data.get("destination")
        if destination is None:
            raise Exception("City not found")
        return destination

    @staticmethod
    def get_user(request):
        """
        Retrieves the authenticated user from the request object.
        """
        user = request.user
        if user:
            return user
        else:
            raise Exception("User is not authenticated")
