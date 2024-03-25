# from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .services import BaseView
from .models import Clients, Director_position
from .serializers import ClientSerializer, DirectorpositionSerializer


# Базовый класс  для получения данных по записям клиентов
class ClientsAPIView(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
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
