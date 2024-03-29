from django.db import models
from logistics.constants import BRANCHES


class Goods(models.Model):
    flour_name = models.ForeignKey(
        "Flour", on_delete=models.PROTECT, related_name="flour_goods", db_index=True
    )
    brand = models.ForeignKey(
        "Brand", on_delete=models.PROTECT, related_name="brand_goods", db_index=True
    )
    package = models.ForeignKey(
        "Package", on_delete=models.PROTECT, related_name="package_goods"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена, руб./тн"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["flour_name", "brand"]
        unique_together = [("flour_name", "brand", "package", "price")]

    def __str__(self):
        return f"{self.flour_name}, т/м {self.brand}, {self.package} кг"


class Flour(models.Model):
    flour_name = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = "Мука"
        verbose_name_plural = "Мука"
        ordering = ["flour_name"]

    def __str__(self):
        return self.flour_name


class Brand(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Брэнд", blank=True)

    class Meta:
        verbose_name = "Брэнд"
        verbose_name_plural = "Брэнды"
        ordering = ["brand"]

    def __str__(self):
        return self.brand


class Package(models.Model):
    package = models.IntegerField(verbose_name="Тара")
    factory = models.ForeignKey("Factory", on_delete=models.PROTECT)
    pallet_weight = models.PositiveIntegerField(verbose_name="Вес на паллете")

    class Meta:
        verbose_name = "Упаковка"
        verbose_name_plural = "Упаковка"
        ordering = ["package", "factory"]
        unique_together = [("package", "factory", "pallet_weight")]

    def __str__(self):
        return f"{self.package} кг, {self.factory}"


class Factory(models.Model):
    full_name = models.CharField(
        max_length=100, blank=False, verbose_name="Полное название предприятия"
    )
    short_name = models.CharField(
        max_length=100, blank=False, verbose_name="Краткое название предприятия"
    )
    full_address = models.CharField(
        max_length=100, blank=False, verbose_name="Адрес предприятия"
    )
    departure_city = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="Город отправления",
    )
    departure_station_branch = models.CharField(
        max_length=100, blank=False, verbose_name="Ветка ж/д стации", choices=BRANCHES
    )
    departure_station_id = models.PositiveIntegerField(verbose_name="Код ж/д стации")
    departure_station_name = models.CharField(
        max_length=100, blank=False, verbose_name="Ж/Д станция"
    )

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"
        ordering = ["-full_name"]
        unique_together = [
            (
                "full_name",
                "short_name",
                "full_address",
            )
        ]

    def __str__(self):
        return self.full_name
