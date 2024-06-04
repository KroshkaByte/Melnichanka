from django.core.cache import cache
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Client, DirectorPosition
from .permissions import ClientAccessPermission
from .serializers import ClientSerializer, DirectorPositionSerializer


# Базовый класс  для получения данных по записям клиентов
class ClientAPIView(generics.ListCreateAPIView[Client]):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        cached_clients = cache.get("clients_list")
        if cached_clients:
            return cached_clients
        else:
            clients = super().get_queryset()
            cache.set("clients_list", clients, 60 * 15)
            return clients


# Изменение данных записи клиента
class ClientAPIUpdateView(generics.RetrieveUpdateAPIView[Client]):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (ClientAccessPermission,)


# Удаление данных записи клиента
class ClientAPIDeleteView(generics.DestroyAPIView[Client]):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (ClientAccessPermission,)


# Передача списка позиций директора для фронтенда
class DirectorPositionListView(generics.ListAPIView[DirectorPosition]):
    queryset = DirectorPosition.objects.all()
    serializer_class = DirectorPositionSerializer
    permission_classes = (IsAuthenticated,)
