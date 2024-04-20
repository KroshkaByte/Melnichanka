from rest_framework import generics, permissions

from users.models import CustomUser


# Базовый класс get_object для действий с пользвателем
class UserRelatedView(generics.RetrieveUpdateAPIView[CustomUser]):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
