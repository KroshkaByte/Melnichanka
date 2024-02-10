# Generated by Django 4.2 on 2024-02-10 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(choices=[('Курск', 'АО Курский Комбинат Хлебопродуктов'), ('Оскол', 'АО Комбинат Хлебопродуктов Старооскольский'), ('Волгоград', 'АО Городищенский Комбинат Хлебопродуктов')], max_length=100)),
                ('short_name', models.CharField(choices=[('Курск', 'ККХП'), ('Оскол', 'КХПС'), ('Волгоград', 'ГКХП')], max_length=50)),
                ('full_address', models.CharField(choices=[('Курск', '305025, г. Курск, проезд Магистральный, 22Г'), ('Оскол', '309506, Белгородская обл., г. Старый Оскол, ул. Первой Конной Армии'), ('Волгоград', '403020, Волгоградская обл., р.п. Новый Рогачик, ул. Ленина, 75')], max_length=255)),
                ('departure_city', models.CharField(choices=[('Курск', 'Курск'), ('Оскол', 'Старый Оскол'), ('Волгоград', 'Новый Рогачик')], max_length=50)),
                ('departure_station_branch', models.CharField(choices=[('Курск', 'Московская ж/д'), ('Оскол', 'Юго-Восточная ж/д'), ('Волгоград', 'Приволжская ж/д')], max_length=9)),
                ('departure_station_id', models.CharField(choices=[('Курск', '208108'), ('Оскол', '438506'), ('Волгоград', '615904')], max_length=9)),
            ],
            options={
                'verbose_name': 'Комбинат',
                'verbose_name_plural': 'Комбинаты',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='LogisticsCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Населенный пункт')),
                ('region', models.CharField(max_length=100, verbose_name='Субъект федерации')),
                ('federal_district', models.CharField(choices=[('ЦФО', 'Центральный федеральный округ'), ('СЗФО', 'Северо-Западный федеральный округ'), ('ЮФО', 'Южный федеральный округ'), ('ПФО', 'Приволжский федеральный округ'), ('УФО', 'Уральский федеральный округ'), ('СФО', 'Сибирский федеральный округ'), ('ДВФО', 'Дальневосточный федеральный округ')], max_length=100, verbose_name='Федеральный округ')),
            ],
            options={
                'verbose_name': 'Населенный пункт',
                'verbose_name_plural': 'Населенные пункты',
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='RailwayStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(choices=[('Курск', 'Рышково'), ('Оскол', 'Старый Оскол'), ('Волгоград', 'Карповская')], max_length=100, verbose_name='Станция')),
                ('station_id', models.PositiveIntegerField()),
                ('station_branch', models.CharField(choices=[('ОЖД', 'Октябрьская ж/д'), ('КаЖД', 'Калининградская ж/д'), ('МЖД', 'Московская ж/д'), ('ГЖД', 'Горьковская ж/д'), ('СеЖД', 'Северная ж/д'), ('СКЖД', 'Северо-Кавказская ж/д'), ('ЮВЖД', 'Юго-Восточная ж/д'), ('ПЖД', 'Приволжская ж/д'), ('КуЖД', 'Куйбышевская ж/д'), ('СвЖД', 'Свердловская ж/д'), ('ЮУЖД', 'Южно-Уральская ж/д'), ('ЗСЖД', 'Западно-Сибирская ж/д'), ('КЖД', 'Красноярская ж/д'), ('ВСЖД', 'Восточно-Сибирская ж/д'), ('ЗЖД', 'Забайкальская ж/д'), ('ДВЖД', 'Дальневосточная ж/д')], max_length=255)),
            ],
            options={
                'verbose_name': 'Ж/д станция',
                'verbose_name_plural': 'Ж/д станции',
                'ordering': ['station_name'],
            },
        ),
        migrations.CreateModel(
            name='LogisticsRailwayStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_per_tonn_rw', models.PositiveIntegerField()),
                ('departure_station_name', models.ForeignKey(db_column='departure_station_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='departure_station_name', to='logistics.railwaystations')),
                ('destination_station_name', models.ForeignKey(db_column='destination_station_name', on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination_station_name', to='logistics.railwaystations')),
            ],
            options={
                'verbose_name': 'Логистика ж/д',
                'verbose_name_plural': 'Логистика ж/д',
                'ordering': ['departure_station_name', 'destination_station_name'],
                'unique_together': {('departure_station_name', 'destination_station_name')},
            },
        ),
        migrations.CreateModel(
            name='LogisticsAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_per_tonn_auto', models.PositiveIntegerField(verbose_name='Цена за рейс, руб./тн')),
                ('departure_city', models.ForeignKey(db_column='departure_city', on_delete=django.db.models.deletion.DO_NOTHING, related_name='departure_city', to='logistics.logisticscity')),
                ('destination_city', models.ForeignKey(db_column='destination_city', on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination_city', to='logistics.logisticscity')),
            ],
            options={
                'verbose_name': 'Логистика авто',
                'verbose_name_plural': 'Логистика авто',
                'ordering': ['departure_city', 'destination_city'],
                'unique_together': {('departure_city', 'destination_city')},
            },
        ),
    ]
