from typing import Any

from rest_framework import serializers


class DocumentsSimpleSerializer(serializers.Serializer[Any]):
    pass


class OrderItemSerializer(serializers.Serializer[Any]):
    product_id = serializers.IntegerField()
    quantity = serializers.FloatField(min_value=0.001)
    discount = serializers.IntegerField(required=False, default=0, max_value=100)


class DataDocSerializer(serializers.Serializer[Any]):
    delivery_type = serializers.CharField()
    client_id = serializers.IntegerField()
    items = serializers.ListField(child=OrderItemSerializer())
    factory_id = serializers.IntegerField()
    destination = serializers.CharField()
    delivery_cost = serializers.IntegerField(min_value=0)


class FileNameSerializer(serializers.Serializer[Any]):
    file_name = serializers.CharField(required=False, allow_blank=True)
