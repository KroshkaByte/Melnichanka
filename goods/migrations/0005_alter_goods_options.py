# Generated by Django 4.2 on 2024-02-26 14:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0004_alter_goods_unique_together"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="goods",
            options={
                "ordering": ["flour_name", "brand"],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
