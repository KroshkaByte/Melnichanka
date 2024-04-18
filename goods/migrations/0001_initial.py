# Generated by Django 4.2 on 2024-04-14 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=100, verbose_name='Брэнд')),
            ],
            options={
                'verbose_name': 'Брэнд',
                'verbose_name_plural': 'Брэнды',
                'ordering': ['brand'],
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное название предприятия')),
                ('short_name', models.CharField(max_length=100, verbose_name='Краткое название предприятия')),
                ('full_address', models.CharField(max_length=100, verbose_name='Адрес предприятия')),
                ('departure_city', models.CharField(max_length=100, verbose_name='Город отправления')),
                ('departure_station_branch', models.CharField(choices=[('ОЖД', 'Октябрьская ж/д'), ('КаЖД', 'Калининградская ж/д'), ('МЖД', 'Московская ж/д'), ('ГЖД', 'Горьковская ж/д'), ('СеЖД', 'Северная ж/д'), ('СКЖД', 'Северо-Кавказская ж/д'), ('ЮВЖД', 'Юго-Восточная ж/д'), ('ПЖД', 'Приволжская ж/д'), ('КуЖД', 'Куйбышевская ж/д'), ('СвЖД', 'Свердловская ж/д'), ('ЮУЖД', 'Южно-Уральская ж/д'), ('ЗСЖД', 'Западно-Сибирская ж/д'), ('КЖД', 'Красноярская ж/д'), ('ВСЖД', 'Восточно-Сибирская ж/д'), ('ЗЖД', 'Забайкальская ж/д'), ('ДВЖД', 'Дальневосточная ж/д')], max_length=100, verbose_name='Ветка ж/д стации')),
                ('departure_station_id', models.PositiveIntegerField(verbose_name='Код ж/д стации')),
                ('departure_station_name', models.CharField(max_length=100, verbose_name='Ж/Д станция')),
            ],
            options={
                'verbose_name': 'Предприятие',
                'verbose_name_plural': 'Предприятия',
                'ordering': ['-full_name'],
                'unique_together': {('full_name', 'short_name', 'full_address')},
            },
        ),
        migrations.CreateModel(
            name='Flour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flour_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Мука',
                'verbose_name_plural': 'Мука',
                'ordering': ['flour_name'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.IntegerField(verbose_name='Тара')),
                ('pallet_weight', models.PositiveIntegerField(verbose_name='Вес на паллете')),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.factory')),
            ],
            options={
                'verbose_name': 'Упаковка',
                'verbose_name_plural': 'Упаковка',
                'ordering': ['package', 'factory'],
                'unique_together': {('package', 'factory', 'pallet_weight')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена, руб./тн')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand_goods', to='goods.brand')),
                ('flour_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flour_goods', to='goods.flour')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_goods', to='goods.package')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['flour_name', 'brand'],
                'unique_together': {('flour_name', 'brand', 'package', 'price')},
            },
        ),
    ]
