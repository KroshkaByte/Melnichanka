from clients.models import Client
from logistics.models import RailwayStation
from users.models import CustomUser


def get_rw(request):
    rw = RailwayStation.objects.get(id=1)
    return rw


def get_client(request):
    client = Client.objects.all().first()
    return client


def get_client_rw(request):
    client = Client.objects.get(id=5)
    return client


def get_user(request):
    user = CustomUser.objects.get(id=1)
    return user
