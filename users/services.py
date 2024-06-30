from rest_framework import generics, permissions

from users.models import CustomUser


class UserRelatedView(generics.RetrieveUpdateAPIView[CustomUser]):
    """
    Base class for operations related to the current user.
    Used for retrieving and updating data of the current authenticated user.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieves the current authenticated user object.
        """
        return self.request.user
