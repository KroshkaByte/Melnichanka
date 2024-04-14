from .models import Client
from .permissions import ClientAccessPermission
from .serializers import ClientSerializer


class BaseView:
    """
    Базовый класс для API-запросов изменения и удаления клиентов.
    Определяет общие атрибуты и методы, которые используются в API-запросах изменения и удаления клиентов.
    Включает в себя набор данных, используемый сериализатор и классы разрешений.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (ClientAccessPermission,)
