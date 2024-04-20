from rest_framework import serializers

from .models import Product


class GoodsSerializer(serializers.ModelSerializer[Product]):
    class Meta:
        model = Product
        fields = "__all__"
