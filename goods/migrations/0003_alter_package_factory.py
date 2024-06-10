# Generated by Django 4.2 on 2024-06-07 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0003_factory'),
        ('goods', '0002_auto_20240607_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logistics.factory'),
        ),
    ]