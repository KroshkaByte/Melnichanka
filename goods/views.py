from django.core.cache import cache
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product, Factory
from .serializers import GoodsSerializer, FactorySerializer


class GoodsViewSet(viewsets.ModelViewSet[Product]):
    queryset = Product.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        cached_goods = cache.get("goods_list")
        if cached_goods:
            return cached_goods
        else:
            goods = super().get_queryset()
            cache.set("goods_list", goods, 60 * 15)
            return goods


class FactoryListAPIView(generics.ListAPIView[Factory]):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    permission_classes = (IsAuthenticated,)
