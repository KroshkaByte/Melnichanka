from django.db import models

from logistics.models import Factory


class Product(models.Model):
    flour_name = models.ForeignKey(
        "Flour", on_delete=models.PROTECT, related_name="flour_goods", db_index=True
    )
    brand = models.ForeignKey(
        "Brand", on_delete=models.PROTECT, related_name="brand_goods", db_index=True
    )
    package = models.ForeignKey("Package", on_delete=models.PROTECT, related_name="package_goods")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена, руб./тн")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["flour_name", "brand"]
        unique_together = [("flour_name", "brand", "package", "price")]

    def __str__(self) -> str:
        return f"{self.flour_name}, т/м {self.brand}, {self.package} кг"


class Flour(models.Model):
    flour_name = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = "Мука"
        verbose_name_plural = "Мука"
        ordering = ["flour_name"]

    def __str__(self) -> str:
        return self.flour_name


class Brand(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Брэнд", blank=True)

    class Meta:
        verbose_name = "Брэнд"
        verbose_name_plural = "Брэнды"
        ordering = ["brand"]

    def __str__(self) -> str:
        return self.brand


class Package(models.Model):
    package = models.IntegerField(verbose_name="Тара")
    factory = models.ForeignKey(Factory, on_delete=models.PROTECT)
    pallet_weight = models.PositiveIntegerField(verbose_name="Вес на паллете")

    class Meta:
        verbose_name = "Упаковка"
        verbose_name_plural = "Упаковка"
        ordering = ["package", "factory"]
        unique_together = [("package", "factory", "pallet_weight")]

    def __str__(self) -> str:
        return f"{self.package}"
