from rest_framework import viewsets, permissions, exceptions
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj:
            raise exceptions.PermissionDenied(
                "Вы не можете редактировать данные другого пользователя"
            )
        return obj
