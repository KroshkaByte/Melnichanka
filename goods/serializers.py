from rest_framework import serializers

from .models import Product


class GoodsSerializer(serializers.ModelSerializer[Product]):
    flour_name: serializers.CharField = serializers.CharField()
    brand: serializers.CharField = serializers.CharField()
    package: serializers.CharField = serializers.CharField()

    class Meta:
        model = Product
        fields = "__all__"
