from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Goods
from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticated,)
