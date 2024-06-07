from django.contrib import admin

from .models import Brand, Flour, Package, Product


@admin.register(Product)
class GoodsAdmin(admin.ModelAdmin):
    list_display = [
        "flour_name",
        "brand",
        "package",
        "price",
    ]
    list_display_links = [
        "flour_name",
        "brand",
        "package",
        "price",
    ]
    ordering = ["flour_name"]
    list_per_page = 10
    search_fields = ["flour_name", "brand", "package"]

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["flour_name", "brand"]
        unique_together = [("flour_name", "brand", "package")]


@admin.register(Flour)
class FlourAdmin(admin.ModelAdmin):
    list_display = ["flour_name"]
    list_display_links = ["flour_name"]
    ordering = ["flour_name"]
    list_per_page = 10
    search_fields = ["flour_name"]

    class Meta:
        verbose_name = "Мука"
        verbose_name_plural = "Мука"
        ordering = ["flour_name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["brand"]
    list_display_links = ["brand"]
    ordering = ["brand"]
    list_per_page = 10
    search_fields = ["brand"]

    class Meta:
        verbose_name = "Брэнд"
        verbose_name_plural = "Брэнды"
        ordering = ["brand"]


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ["package", "factory", "pallet_weight"]
    list_display_links = ["package", "factory", "pallet_weight"]
    ordering = ["package", "factory"]
    list_per_page = 10
    search_fields = ["package", "factory", "pallet_weight"]

    class Meta:
        verbose_name = "Упаковка"
        verbose_name_plural = "Упаковка"
        ordering = ["package", "factory"]
        unique_together = [("package", "factory", "pallet_weight")]
