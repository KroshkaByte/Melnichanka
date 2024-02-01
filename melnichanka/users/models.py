from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Информация о заводах-производителях
class Factory(models.Model):
    class FactoryFlour(models.TextChoices):
        KKHP = "ККХП", 'АО "Курский Комбинат Хлебопродуктов'
        KHPS = "КХПС", 'АО "Комбинат Хлебопродуктов Старооскольский'
        GKHP = "ГКХП", 'АО "Городищенский Комбинат Хлебопродуктов'

    factory_name = models.CharField(
        max_length=4, choices=FactoryFlour.choices, default=FactoryFlour.KKHP
    )
    factory_city = models.CharField(max_length=50)
    factory_adress = models.CharField(max_length=150)

    def __str__(self):
        return f"Производитель: {self.factory_name}"


# Информация о контрагенте
class Client(models.Model):
    # Основная информация
    company_name = models.CharField(max_length=100)
    contract_number = models.CharField(max_length=50, unique=True)
    contract_date = models.DateField()
    director_position = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)

    # ЖД реквизиты
    destination_station_name = models.CharField(max_length=100)
    destination_station_id = models.PositiveIntegerField()
    receiver_name = models.CharField(max_length=100)
    receiver_id = models.PositiveIntegerField()
    receiver_okpo = models.PositiveIntegerField()
    receiver_adress = models.CharField(max_length=200)
    special_marks = models.CharField(max_length=200)

    # Номер приложения
    last_application_number = models.CharField(max_length=50)


# Информация о пользователе приложения
class User(AbstractUser):
    username = models.CharField(
        max_length=50, unique=True, verbose_name="Имя пользователя"
    )
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    position = models.CharField(
        max_length=50, verbose_name="Должность"
    )  # Можно сделать выпадающий список
    department = models.CharField(
        max_length=50, verbose_name="Отдел"
    )  # Можно сделать выпадающий список
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
