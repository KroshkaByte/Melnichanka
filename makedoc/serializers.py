from typing import Any

from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer[Any]):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    discount = serializers.IntegerField(required=False, default=0)


class DataDocSerializer(serializers.Serializer[Any]):
    client_id = serializers.IntegerField()
    items = serializers.ListField(child=OrderItemSerializer())
    factory_id = serializers.IntegerField()
    destination = serializers.CharField()
    delivery_cost = serializers.IntegerField()
