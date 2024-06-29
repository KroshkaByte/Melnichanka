from django.db import models

from logistics.models import City, RailwayStation
from users.models import CustomUser


class DirectorPosition(models.Model):
    """
    Model representing a director's position.
    """
    director_position = models.CharField(max_length=40, verbose_name="Должность директора")

    class Meta:
        verbose_name = "Должность директора"
        verbose_name_plural = "Должность директора"

    def __str__(self) -> str:
        return self.director_position


class Client(models.Model):
    """
    Model representing a client organization.
    """
    # Main Information
    client_name = models.CharField(
        max_length=100, verbose_name="Наименование организации", db_index=True
    )
    contract_number = models.CharField(max_length=50, verbose_name="Номер договора", db_index=True)
    contract_date = models.DateField(verbose_name="Дата заключения договора")
    director_position = models.ForeignKey(
        DirectorPosition,
        on_delete=models.PROTECT,
        verbose_name="Должность директора",
    )
    director_name = models.CharField(max_length=100, verbose_name="ФИО директора")
    destination_city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="Город доставки", db_index=True
    )
    # Railway Details
    railway_station = models.ForeignKey(
        RailwayStation,
        on_delete=models.PROTECT,
        verbose_name="ЖД станция",
        related_name="clients",
        blank=True,
        null=True,
    )
    # Other Data
    receiver_name = models.CharField(max_length=100, blank=True, verbose_name="Имя получателя")
    receiver_id = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Номер получателя"
    )
    receiver_okpo = models.PositiveIntegerField(blank=True, null=True, verbose_name="ОКПО")
    receiver_adress = models.CharField(max_length=200, blank=True, verbose_name="Адрес получателя")
    special_marks = models.CharField(max_length=200, blank=True, verbose_name="Особые отметки")
    # Application Number
    last_application_number = models.CharField(
        max_length=50, blank=True, verbose_name="Номер приложения"
    )
    # User who created the record
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        unique_together = ("client_name", "contract_number")

    def __str__(self) -> str:
        return self.client_name
