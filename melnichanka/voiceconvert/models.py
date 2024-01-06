from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=150)
    phone_number_work = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number_personal = PhoneNumberField(null=False, blank=False, unique=True)

    USERNAME_FIELD = "username"

    class Meta:
        ordering = ["username"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username


class Factory(models.Model):
    factory_full_name = models.CharField(max_length=100, unique=True)
    factory_short_name = models.CharField(max_length=50)
    factory_city = models.CharField(max_length=50)
    factory_adress = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.factory_full_name
