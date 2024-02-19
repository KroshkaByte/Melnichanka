from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Информация о пользователе приложения
class User(AbstractUser):
    username = models.CharField(
        max_length=50, unique=True, verbose_name="Имя пользователя"
    )
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    position = models.CharField(max_length=50, verbose_name="Должность")
    department = models.CharField(max_length=50, verbose_name="Отдел")
    email = models.EmailField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=150)
    phone_number_work = PhoneNumberField(verbose_name="Личный телефон")
    phone_number_personal = PhoneNumberField(verbose_name="Рабочий телефон")

    USERNAME_FIELD = "username"

    class Meta:
        ordering = ["username"]
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь {self.username}"
