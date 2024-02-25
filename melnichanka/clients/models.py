from django.db import models
from logistics.models import RailwayStations


class Clients(models.Model):
    # Основная информация
    client_name = models.CharField(
        max_length=100, blank=True, verbose_name="Наименование организации"
    )
    contract_number = models.CharField(
        max_length=50, blank=True, verbose_name="Номер договора", unique=True
    )
    contract_date = models.DateField(verbose_name="Дата заключения договора")
    director_position = models.CharField(
        max_length=100, verbose_name="Должность директора"
    )
    director_name = models.CharField(max_length=100, verbose_name="ФИО директора")
    # ЖД реквизиты
    destination_city = models.ForeignKey(
        RailwayStations,
        on_delete=models.PROTECT,
        verbose_name="ЖД станция",
        related_name="clients",
    )
    # Остальные данные
    receiver_name = models.CharField(max_length=100, verbose_name="Имя получателя")
    receiver_id = models.PositiveIntegerField(verbose_name="Номер получателя")
    receiver_okpo = models.PositiveIntegerField(verbose_name="ОКПО")
    receiver_adress = models.CharField(max_length=200, verbose_name="Адрес получателя")
    special_marks = models.CharField(max_length=200, verbose_name="Особые отметки")
    # Номер приложения
    last_application_number = models.CharField(
        max_length=50, verbose_name="Номер приложения"
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.client_name
