from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

# Получение модели пользователя
User = get_user_model()


# Базовый класс get_object
class UserRelatedView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
