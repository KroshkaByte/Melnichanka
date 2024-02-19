from django.db import models

from .constants import BRANDS, FLOUR_NAME, GROUP_QUANTITY, PACKAGE, PALLET_WEIGHT


class Goods(models.Model):
    flour_name = models.CharField(
        max_length=255, blank=False, verbose_name="Сорт муки", choices=FLOUR_NAME
    )
    brand = models.CharField(max_length=100, choices=BRANDS, verbose_name="Брэнд", blank=True)
    package = models.IntegerField(choices=PACKAGE, verbose_name="Тара")
    group_quantity = models.PositiveIntegerField(choices=GROUP_QUANTITY,
        verbose_name="Количество штук в упаковке"
    )
    factory = models.CharField(
        choices=(("Курск", "Курск"), ("Оскол", "Оскол"), ("Волгоград", "Волгоград")),
        verbose_name="Изготовитель",
    )
    pallet_weight = models.IntegerField(
        choices=PALLET_WEIGHT, verbose_name="Вес на паллете"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена, руб./тн"
    )

    class Meta:
        verbose_name = "Упаковка"
        verbose_name_plural = "Упаковка"
        ordering = ["flour_name", "brand"]
        unique_together = [("flour_name", "brand", "package", "price")]

    def __str__(self):
        return f"{self.flour_name}, т/м {self.brand}, {self.package} кг"
