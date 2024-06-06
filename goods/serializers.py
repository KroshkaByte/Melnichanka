from rest_framework import serializers

from .models import Product, Factory


class GoodsSerializer(serializers.ModelSerializer[Product]):
    flour_name: serializers.CharField = serializers.CharField()
    brand: serializers.CharField = serializers.CharField()
    package: serializers.CharField = serializers.CharField()

    class Meta:
        model = Product
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer[Factory]):
    class Meta:
        model = Factory
        fields = "__all__"
