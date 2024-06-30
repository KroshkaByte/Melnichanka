from rest_framework import serializers

from .models import Product


class GoodsSerializer(serializers.ModelSerializer[Product]):
    """
    Serializer for serializing/deserializing Product objects.
    """

    flour_name: serializers.CharField = serializers.CharField()
    brand: serializers.CharField = serializers.CharField()
    package: serializers.CharField = serializers.CharField()

    class Meta:
        model = Product
        fields = "__all__"
