from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from django.utils.decorators import method_decorator
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from melnichanka.settings import EMAIL_HOST_USER
from .models import CustomUser, Department, Position
from .serializers import (
    CustomUserSerializer,
    DepartmentSerializer,
    PositionSerializer,
    UserUpdatePasswordSerializer,
    UserUpdateSerializer,
)
from .services import User, UserRelatedView


# Аутентификация пользователя
class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response(
                {"detail": "Пожалуйста, укажите email и пароль."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(email=email, password=password)

        if user is None:
            return Response(
                {"detail": "Неверные учетные данные."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, user)
        return Response({"detail": "Успешно авторизован."})


class LogoutView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            raise ValidationError("Вы не вошли в систему.")

        logout(request)
        return Response({"detail": "Успешный выход из системы."})


@method_decorator(ensure_csrf_cookie, name="dispatch")
class SessionView(APIView):
    def get(self, request):
        return Response({"isAuthenticated": request.user.is_authenticated})


class WhoAmIView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"isAuthenticated": False})

        return Response({"username": request.user.username})


# Класс регистрации пользователя
class UserCreateView(generics.CreateAPIView):
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
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    email_plaintext_message = "Для сброса пароля перейдите по ссылке: http://127.0.0.1:8000{}?token={}".format(
        reverse("password_reset:reset-password-confirm"), reset_password_token.key
    )

    send_mail(
        # title:
        "Сброс пароля для: {title}".format(title="EDO website"),
        # message:
        email_plaintext_message,
        # from:
        EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
    )


# Передача списка департаментов для фронтенда
class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# Передача списка позиций для фронтенда
class PositionListView(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
