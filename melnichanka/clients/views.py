from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Clients
from .serializers import ClientSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
