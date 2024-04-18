from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Client, Director_position
from .serializers import ClientSerializer, DirectorpositionSerializer
from .services import BaseView


# Базовый класс  для получения данных по записям клиентов
class ClientAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)


# Изменение данных записи клиента
class ClientAPIUpdateView(BaseView, generics.RetrieveUpdateAPIView):
    pass


# Удаление данных записи клиента
class ClientAPIDeleteView(BaseView, generics.DestroyAPIView):
    pass


# Передача списка позиций директора для фронтенда
class DirectorPositionListView(generics.ListAPIView):
    queryset = Director_position.objects.all()
    serializer_class = DirectorpositionSerializer
