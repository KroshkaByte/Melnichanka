from rest_framework import serializers
from .models import Product


class GoodsSerializer(serializers.ModelSerializer):
    flour_name = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    package = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = "__all__"
