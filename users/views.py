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
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response(
                {"detail": "Пожалуйста, укажите email и пароль."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            return super().post(request, *args, **kwargs)
        except Exception:
            return Response(
                {"detail": "Неверные учетные данные."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            refresh_token = serializer.validated_data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Класс регистрации пользователя
class UserCreateView(generics.CreateAPIView[CustomUser]):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Изменение данных пользователя
class UserUpdateView(UserRelatedView):
    serializer_class = UserUpdateSerializer


# Изменение пароля пользователя
class UserUpdatePasswordView(UserRelatedView):
    serializer_class = UserUpdatePasswordSerializer


# Сброс пароля
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    send_reset_email.delay(reset_password_token.user.email, reset_password_token.key)


# Передача списка департаментов для фронтенда
class DepartmentListView(generics.ListAPIView[Department]):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# Передача списка позиций для фронтенда
class PositionListView(generics.ListAPIView[Position]):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
