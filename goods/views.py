from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet[Product]):
    queryset = Product.objects.select_related("flour_name", "brand", "package").all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        cached_goods = cache.get("goods_list")
        if cached_goods:
            return cached_goods
        else:
            goods = super().get_queryset()
            cache.set("goods_list", goods, 1800)
            return goods
