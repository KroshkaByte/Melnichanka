from django.db import models

from .constants import BRANDS, FLOUR_NAME


class Factory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Фабрика"
        verbose_name_plural = "Фабрики"

    def __str__(self):
        return self.name


class Goods(models.Model):
    brand = models.CharField(max_length=100, choices=BRANDS, verbose_name="Брэнд")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"{self.brand}"


class Package(models.Model):
    flour_name = models.CharField(
        max_length=255, blank=False, verbose_name="Сорт муки", choices=FLOUR_NAME
    )
    unit_weight = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Вес единицы"
    )
    group_quantity = models.PositiveIntegerField(
        verbose_name="Количество штук в упаковке"
    )
    factory = models.ForeignKey(
        Factory, on_delete=models.DO_NOTHING, verbose_name="Изготовитель"
    )
    pallet_weight = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Вес на паллете"
    )

    class Meta:
        verbose_name = "Упаковка"
        verbose_name_plural = "Упаковка"

    def __str__(self):
        return f"{self.flour_name} {self.unit_weight}"
