from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Client, DirectorPosition
from .serializers import ClientSerializer, DirectorpositionSerializer
from .services import BaseView


# Базовый класс  для получения данных по записям клиентов
class ClientAPIView(generics.ListCreateAPIView[Client]):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)


# Изменение данных записи клиента
class ClientAPIUpdateView(BaseView, generics.RetrieveUpdateAPIView[Client]):
    pass


# Удаление данных записи клиента
class ClientAPIDeleteView(BaseView, generics.DestroyAPIView[Client]):
    pass


# Передача списка позиций директора для фронтенда
class DirectorPositionListView(generics.ListAPIView[DirectorPosition]):
    queryset = DirectorPosition.objects.all()
    serializer_class = DirectorpositionSerializer
