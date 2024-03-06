from django.db import models
from logistics.models import RailwayStations, City


class Clients(models.Model):
    # Основная информация
    client_name = models.CharField(
        max_length=100, verbose_name="Наименование организации"
    )
    contract_number = models.CharField(max_length=50, verbose_name="Номер договора")
    contract_date = models.DateField(verbose_name="Дата заключения договора")
    director_position = models.CharField(
        max_length=100, verbose_name="Должность директора"
    )
    director_name = models.CharField(max_length=100, verbose_name="ФИО директора")
    destination_city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="Город доставки"
    )
    # ЖД реквизиты
    railway_station = models.ForeignKey(
        RailwayStations,
        on_delete=models.PROTECT,
        verbose_name="ЖД станция",
        related_name="clients",
        blank=True,
        null=True,
    )
    # Остальные данные
    receiver_name = models.CharField(
        max_length=100, blank=True, verbose_name="Имя получателя"
    )
    receiver_id = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Номер получателя"
    )
    receiver_okpo = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="ОКПО"
    )
    receiver_adress = models.CharField(
        max_length=200, blank=True, verbose_name="Адрес получателя"
    )
    special_marks = models.CharField(
        max_length=200, blank=True, verbose_name="Особые отметки"
    )
    # Номер приложения
    last_application_number = models.CharField(
        max_length=50, blank=True, verbose_name="Номер приложения"
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        unique_together = ("client_name", "contract_number")

    def __str__(self):
        return self.client_name
