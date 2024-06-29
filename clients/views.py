from django.core.cache import cache
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Client, DirectorPosition
from .permissions import ClientAccessPermission
from .serializers import ClientSerializer, DirectorPositionSerializer


class ClientAPIView(generics.ListCreateAPIView[Client]):
    """
    API view for retrieving a list of clients and creating a new client record.

    Retrieves a list of clients with related director position, destination city,
    and railway station. Caches the client list for 15 minutes if not already cached.
    """

    queryset = Client.objects.select_related(
        "director_position", "destination_city", "railway_station"
    ).all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Get the queryset of clients. If cached, return cached data; otherwise, fetch from database
        and cache for 15 minutes.
        """
        cached_clients = cache.get("clients_list")
        if cached_clients:
            return cached_clients
        else:
            clients = super().get_queryset()
            cache.set("clients_list", clients, 60 * 15)
            return clients


class ClientAPIUpdateView(generics.RetrieveUpdateAPIView[Client]):
    """
    API view for updating a client record.

    Retrieves and updates a specific client record based on its primary key.
    Requires ClientAccessPermission for authorization.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (ClientAccessPermission,)


class ClientAPIDeleteView(generics.DestroyAPIView[Client]):
    """
    API view for deleting a client record.

    Deletes a specific client record based on its primary key.
    Requires ClientAccessPermission for authorization.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (ClientAccessPermission,)


class DirectorPositionListView(generics.ListAPIView[DirectorPosition]):
    """
    API view for retrieving a list of director positions.

    Retrieves a list of all available director positions.
    Requires authentication (IsAuthenticated).
    """

    queryset = DirectorPosition.objects.all()
    serializer_class = DirectorPositionSerializer
    permission_classes = (IsAuthenticated,)
