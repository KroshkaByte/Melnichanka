import os.path

from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser, Department, Position
from .serializers import (
    CustomUserSerializer,
    DepartmentSerializer,
    PositionSerializer,
    UserUpdatePasswordSerializer,
    UserUpdateSerializer,
    LogoutSerializer,
)
from .services import UserRelatedView
from .tasks import send_reset_email


class LoginView(TokenObtainPairView):
    """
    View to obtain JSON Web Token (JWT) by posting username and password.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to obtain JWT.

        Params:
            - email: User's email address.
            - password: User's password.

        Returns:
            - JSON response with JWT or error message.
        """
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response(
                {"detail": "Please provide both email and password."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            return super().post(request, *args, **kwargs)
        except Exception:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutView(APIView):
    """
    View to blacklist JWT refresh token and logout user.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer

    def post(self, request):
        """
        Handle POST requests to logout user.

        Params:
            - refresh_token: JWT refresh token.

        Returns:
            - HTTP 205 Reset Content on success, or HTTP 400 Bad Request on failure.
        """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            refresh_token = serializer.validated_data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(generics.CreateAPIView[CustomUser]):
    """
    View to handle user registration.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserUpdateView(UserRelatedView):
    """
    View to handle updating user data.
    """

    serializer_class = UserUpdateSerializer


class UserUpdatePasswordView(UserRelatedView):
    """
    View to handle changing user password.
    """

    serializer_class = UserUpdatePasswordSerializer


class ListUserFilesAPIView(APIView):
    """
    View to list files of an authorized user.
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list user's files.

        Returns:
            - List of user's files or error message.
        """
        user_folder = os.path.join("makedoc", "tempdoc", str(request.user.id))

        if not os.path.exists(user_folder):
            return Response({"error": "User folder not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            files = os.listdir(user_folder)
        except OSError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        files_list = []
        for file_name in files:
            file_path = os.path.join(user_folder, file_name)
            if os.path.isfile(file_path):
                files_list.append(file_name)

        return Response({"files": files_list}, status=status.HTTP_200_OK)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Signal receiver function to handle password reset token creation.

    Args:
        - sender: Sender of the signal.
        - instance: Instance related to the signal.
        - reset_password_token: Password reset token object.
    """
    send_reset_email.delay(reset_password_token.user.email, reset_password_token.key)


class DepartmentListView(generics.ListAPIView[Department]):
    """
    View to list departments.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionListView(generics.ListAPIView[Position]):
    """
    View to list positions.
    """

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
