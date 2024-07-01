from typing import Any

from rest_framework import serializers


class EmailInputSerializer(serializers.Serializer[Any]):
    """
    Serializer for validating email input.
    """

    email = serializers.EmailField()


class DocumentsSimpleSerializer(serializers.Serializer[Any]):
    """
    A simple serializer for document data.
    """

    pass


class OrderItemSerializer(serializers.Serializer[Any]):
    """
    A serializer for order items.
    """

    product_id = serializers.IntegerField()
    quantity = serializers.FloatField(min_value=0.001)
    discount = serializers.IntegerField(required=False, default=0, max_value=100)


class DataDocSerializer(serializers.Serializer[Any]):
    """
    A serializer for document data.
    """

    delivery_type = serializers.CharField()
    client_id = serializers.IntegerField()
    items = serializers.ListField(child=OrderItemSerializer())
    factory_id = serializers.IntegerField()
    destination = serializers.CharField()
    delivery_cost = serializers.IntegerField(min_value=0)


class FileNameSerializer(serializers.Serializer[Any]):
    """
    A serializer for file names.
    """

    file_name = serializers.CharField(required=False, allow_blank=True)
