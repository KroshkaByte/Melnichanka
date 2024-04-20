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
