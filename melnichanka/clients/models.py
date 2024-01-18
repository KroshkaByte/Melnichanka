from django.db import models


class Clients(models.Model):
    # Основная информация
    client_name = models.CharField(
        max_length=100, blank=True, verbose_name="Название предприятия"
    )
    contract_number = models.CharField(
        max_length=50, blank=True, verbose_name="Номер договора", unique=True
    )
    contract_date = models.DateField(verbose_name="Дата заключения договора")
    director_position = models.CharField(
        max_length=100, verbose_name="Должность директора"
    )
    director_name = models.CharField(max_length=100, verbose_name="Имя директора")
    special_marks = models.CharField(
        max_length=200, verbose_name="Специальнные отметки"
    )

    # ЖД реквизиты
    destination_station_name = models.CharField(
        max_length=100, verbose_name="Имя ЖД станции"
    )
    destination_station_id = models.PositiveIntegerField(
        verbose_name="Номер ЖД станции"
    )
    receiver_name = models.CharField(max_length=100, verbose_name="Имя получателя")
    receiver_id = models.PositiveIntegerField(verbose_name="Номер получателя")
    receiver_okpo = models.PositiveIntegerField(verbose_name="ОКПО")
    receiver_adress = models.CharField(max_length=200, verbose_name="Адрес получателя")

    # Номер приложения
    last_application_number = models.CharField(
        max_length=50, verbose_name="Номер приложения"
    )

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.client_name
