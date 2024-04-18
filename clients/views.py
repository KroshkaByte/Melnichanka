from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Client, DirectorPosition
from .serializers import ClientSerializer, DirectorpositionSerializer
from .permissions import ClientAccessPermission


# Базовый класс  для получения данных по записям клиентов
class ClientAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)


# Изменение данных записи клиента
class ClientAPIUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (ClientAccessPermission,)


# Удаление данных записи клиента
class ClientAPIDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (ClientAccessPermission,)


# Передача списка позиций директора для фронтенда
class DirectorPositionListView(generics.ListAPIView):
    queryset = DirectorPosition.objects.all()
    serializer_class = DirectorpositionSerializer
    permission_classes = (IsAuthenticated,)
