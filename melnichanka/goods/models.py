from django.db import models

from .constants import BRANDS, FLOUR_NAME


class Goods(models.Model):
    flour_name = models.CharField(max_length=255, blank=False, verbose_name="Сорт муки", choices=FLOUR_NAME)
    unit_weight = models.PositiveIntegerField(verbose_name="Вес единицы")
    group_quantity = models.PositiveIntegerField(verbose_name="Количество штук в упаковке")
    pallet_weight = models.PositiveIntegerField(verbose_name="Вес на паллете")
    brand = models.CharField(max_length=255, verbose_name="Брэнд", choices=BRANDS)
    price = models.FloatField()
