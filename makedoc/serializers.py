from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer):  # type: ignore
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    discount = serializers.IntegerField(required=False, default=0)


class DataDocSerializer(serializers.Serializer):  # type: ignore
    client_id = serializers.IntegerField()
    items = serializers.ListField(child=OrderItemSerializer())
    factory_id = serializers.IntegerField()
    destination = serializers.CharField()
