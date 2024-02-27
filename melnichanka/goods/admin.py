from django.contrib import admin

from .models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = [
        "flour_name",
        "brand",
        "package",
        "price",
    ]
    list_display_links = ["flour_name"]
    ordering = ["flour_name"]
    list_per_page = 10
    search_fields = ["flour_name", "brand", "package"]

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["flour_name", "brand"]
        unique_together = [("flour_name", "brand", "package")]
