from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import permissions, exceptions, generics


from melnichanka.settings import EMAIL_HOST_USER
from .models import CustomUser, Department, Position
from .serializers import (
    CustomUserSerializer,
    DepartmentSerializer,
    PositionSerializer,
    UserUpdateSerializer,
)


# Действия с пользователем
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj:
            raise exceptions.PermissionDenied(
                "Вы не можете редактировать данные другого пользователя"
            )
        return obj


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
