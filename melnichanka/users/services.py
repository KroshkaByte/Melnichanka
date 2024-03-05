from rest_framework import generics, permissions


# Базовый класс get_object для действий с пользвателем
class UserRelatedView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
