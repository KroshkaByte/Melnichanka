from django.db import models


class Factory(models.Model):
    class FactoryFlourName(models.TextChoices):
        KKHP = "Курск", "АО Курский Комбинат Хлебопродуктов"
        KHPS = "Оскол", "АО Комбинат Хлебопродуктов Старооскольский"
        GKHP = "Волгоград", "АО Городищенский Комбинат Хлебопродуктов"

    class FactoryFlourShort(models.TextChoices):
        KKHP = "Курск", "ККХП"
        KHPS = "Оскол", "КХПС"
        GKHP = "Волгоград", "ГКХП"

    class FactoryFlourAddress(models.TextChoices):
        KKHP = "Курск", "305025, г. Курск, проезд Магистральный, 22Г "
        KHPS = (
            "Оскол",
            "309506, Белгородская обл., г. Старый Оскол, ул. Первой Конной Армии",
        )
        GKHP = (
            "Волгоград",
            "403020, Волгоградская обл., р.п. Новый Рогачик, ул. Ленина, 75",
        )

    class FactoryFlourCity(models.TextChoices):
        KKHP = "Курск", "Курск"
        KHPS = "Оскол", "Старый Оскол"
        GKHP = "Волгоград", "Новый Рогачик"

    class FactoryFlourBranch(models.TextChoices):
        KKHP = "Курск", "Московская железная дорога"
        KHPS = "Оскол", "Юго-Восточная железная дорога"
        GKHP = "Волгоград", "Приволжская железная дорога"

    class FactoryFlourBranchId(models.TextChoices):
        KKHP = "Курск", "208108"
        KHPS = "Оскол", "438506"
        GKHP = "Волгоград", "615904"

    full_name = models.CharField(
        max_length=100,
        blank=False,
        # choices=FactoryFlourName.choices
    )
    short_name = models.CharField(
        max_length=50,
        blank=False,
        # choices=FactoryFlourShort.choices
    )
    full_address = models.CharField(
        max_length=255,
        blank=False,
        # choices=FactoryFlourAddress.choices
    )
    departure_city = models.CharField(
        max_length=50,
        blank=False,
        # choices=FactoryFlourCity.choices
    )
    departure_station_branch = models.CharField(
        max_length=9,
        blank=False,
        # choices=FactoryFlourBranch.choices
    )
    departure_station_id = models.CharField(
        max_length=9,
        blank=False,
        # choices=FactoryFlourBranchId.choices
    )

    class Meta:
        verbose_name = "Комбинат"
        verbose_name_plural = "Комбинаты"
        ordering = ["full_name"]


# Данные по логистике авто
class LogisticsAuto(models.Model):
    departure_city = models.CharField(
        max_length=100, blank=False, verbose_name="Комбинат грузоотправитель"
    )
    destination_city = models.CharField(
        max_length=100, blank=False, verbose_name="Город назначения"
    )
    cost_per_tonn_auto = models.PositiveIntegerField(
        verbose_name="Цена за рейс, руб./тн"
    )

    class Meta:
        verbose_name = "Логистика авто"
        verbose_name_plural = "Логистика авто"
        ordering = ["departure_city", "destination_city"]
        unique_together = ["departure_city", "destination_city"]

    def __str__(self):
        return f"{self.departure_city} - {self.destination_city}: {self.cost_per_tonn_auto} руб./тн"


# Данные по логистике жд
class LogisticsRailwayStations(models.Model):
    class FactoryFlour(models.TextChoices):
        KKHP = "Рышково", "АО Курский Комбинат Хлебопродуктов"
        KHPS = "Старый Оскол", "АО Комбинат Хлебопродуктов Старооскольский"
        GKHP = "Карповская", "АО Городищенский Комбинат Хлебопродуктов"

    class RailwayBranch(models.TextChoices):
        OZD = "ОЖД", "Октябрьская железная дорога"
        KaZD = "КаЖД", "Калининградская железная дорога"
        MZD = "МЖД", "Московская железная дорога"
        GZD = "ГЖД", "Горьковская железная дорога"
        SeZD = "СеЖД", "Северная железная дорога"
        SKZD = "СКЖД", "Северо-Кавказская железная дорога"
        YVZD = "ЮВЖД", "Юго-Восточная железная дорога"
        PZD = "ПЖД", "Приволжская железная дорога"
        KUZD = "КуЖД", "Куйбышевская железная дорога"
        SvZD = "СвЖД", "Свердловская железная дорога"
        YUZD = "ЮУЖД", "Южно-Уральская железная дорога"
        ZSZD = "ЗСЖД", "Западно-Сибирская железная дорога"
        KZD = "КЖД", "Красноярская железная дорога"
        VSZD = "ВСЖД", "Восточно-Сибирская железная дорога"
        ZZD = "ЗЖД", "Забайкальская железная дорога"
        DVZD = "ДВЖД", "Дальневосточная железная дорога"

    departure_station_name = models.CharField(
        max_length=12,
        choices=FactoryFlour.choices,
        blank=False,
        verbose_name="Комбинат грузоотправитель",
    )

    departure_station_id = models.PositiveIntegerField()
    departure_station_branch = models.CharField(
        max_length=4,
        choices=RailwayBranch.choices,
    )
    destination_station_name = models.CharField(max_length=100)
    destination_station_id = models.PositiveIntegerField()
    destination_station_branch = models.CharField(
        max_length=4,
        choices=RailwayBranch.choices,
    )
    cost_per_tonn_rw = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Логистика ж/д"
        verbose_name_plural = "Логистика ж/д"
        ordering = ["departure_station_name", "destination_station_name"]
        unique_together = ["departure_station_name", "destination_station_name"]

    def __str__(self):
        return f"{self.departure_station_name} - {self.destination_station_name}: {self.cost_per_tonn_rw} руб./тн"
