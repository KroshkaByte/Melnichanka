# from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .services import BaseView
from .models import Clients
from .serializers import ClientSerializer


class ClientsAPIView(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)


class ClientAPIUpdateView(BaseView, generics.RetrieveUpdateAPIView):
    pass


class ClientAPIDeleteView(BaseView, generics.DestroyAPIView):
    pass
