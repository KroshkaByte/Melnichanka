import json

from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.dispatch import receiver
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import generics, permissions

from melnichanka.settings import EMAIL_HOST_USER

from .models import CustomUser, Department, Position
from .serializers import (
    CustomUserSerializer,
    DepartmentSerializer,
    PositionSerializer,
    UserUpdatePasswordSerializer,
    UserUpdateSerializer,
)


# Аутентификация пользователя
@require_POST
def login_view(request):
    data = json.loads(request.body)
    email = data.get("email")
    password = data.get("password")

    if email is None or password is None:
        return JsonResponse(
            {"detail": " Пожалуйста, укажите имя пользователя и пароль."}, status=400
        )

    user = authenticate(email=email, password=password)

    if user is None:
        return JsonResponse({"detail": " Неверные учетные данные."}, status=400)

    login(request, user)
    return JsonResponse({"detail": " Успешно авторизован."})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": " Вы не вошли в систему."}, status=400)

    logout(request)
    return JsonResponse({"detail": " Успешный выход из системы."})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})

    return JsonResponse({"isAuthenticated": True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": False})

    return JsonResponse({"username": request.user.username})


# Действия с пользователем
class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# Действия с пользователем
class UserUpdatePasswordView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# Класс регистрации пользователя
class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


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
