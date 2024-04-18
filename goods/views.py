from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet[Product]):
    queryset = Product.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticated,)
