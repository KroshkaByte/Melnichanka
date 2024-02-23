from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ClientSerializer
from .models import Clients


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
