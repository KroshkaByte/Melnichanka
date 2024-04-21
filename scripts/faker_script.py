from faker import Faker
from clients.models import Client, DirectorPosition
from logistics.models import City, RailwayStation, TripAuto, TripRailway
from users.models import CustomUser, Department, Position
from goods.models import Product, Factory, Flour, Package, Brand
from random import choice

fake = Faker("ru_RU")


# Скрипт создан для преднаполнения базы данных в целях демонстрации работы приложения


# Создаем позиции из заданого списка
def create_positions():
    positions = ["Менеджер", "Сотрудник продажи"]
    for position in positions:
        Position.objects.create(position=position)


# Создаем департаменты из заданного списка
def create_departments():
    departments = ["Департамент продажи", "Департамент заказчика"]
    for department in departments:
        Department.objects.create(department=department)


# Создаем суперпользователя со случайными данными
def create_superuser():
    CustomUser.objects.create_superuser(
        email="admin@admin.com",
        full_name="Админов Админ Админович",
        password="Melnichanka123",
        position=choice(Position.objects.all()),
        department=choice(Department.objects.all()),
        phone_number_work=fake.phone_number(),
        phone_number_personal=fake.phone_number(),
        is_staff=True,
        is_active=True,
    )


# Создаем пользователей со случайными данными
def create_user(n):
    for _ in range(n):
        CustomUser.objects.create(
            email=fake.email(),
            full_name=f"{fake.first_name()} {fake.last_name()}",
            position=choice(Position.objects.all()),
            department=choice(Department.objects.all()),
            phone_number_work=fake.phone_number(),
            phone_number_personal=fake.phone_number(),
        )


# Создаем позиции директоров из заданного списка
def create_director_position():
    director_positions = ["Директор", "Генеральный директор", "Исполнительный директор"]
    for director_position in director_positions:
        DirectorPosition.objects.create(director_position=director_position)


# Создаем случайные названия городов
def create_city(n):
    federal_districts = [
        "Центральный федеральный округ",
        "Северо-Западный федеральный округ",
        "Южный федеральный округ",
        "Северо-Кавказский федеральный округ",
        "Приволжский федеральный округ",
        "Уральский федеральный округ",
        "Сибирский федеральный округ",
        "Дальневосточный федеральный округ",
    ]
    for _ in range(n):
        City.objects.create(
            city=fake.city(),
            region=fake.region(),
            federal_district=choice(federal_districts),
        )


# Создаем случайные названия жд станций
def create_railway_station(n):
    for _ in range(n):
        RailwayStation.objects.create(
            station_name=fake.street_name(),
            station_id=fake.random_int(),
            station_branch=fake.word(ext_word_list=["Северный", "Южный", "Западный", "Восточный"]),
        )


# Создаем случайные автотранспортные поездки
def create_trip_auto(n):
    for _ in range(n):
        departure_city = choice(City.objects.all())
        destination_city = choice(City.objects.all())
        while departure_city == destination_city:
            destination_city = choice(City.objects.all())
        if not TripAuto.objects.filter(
            departure_city=departure_city, destination_city=destination_city
        ).exists():
            TripAuto.objects.create(
                departure_city=departure_city,
                destination_city=destination_city,
                cost_per_tonn_auto=fake.random_int(min=1000, max=5000),
            )


# Создаем случайные жд поездки
def create_trip_railway(n):
    for _ in range(n):
        departure_station = choice(RailwayStation.objects.all())
        destination_station = choice(RailwayStation.objects.all())
        while departure_station == destination_station:
            destination_station = choice(RailwayStation.objects.all())
        # Проверяем, существует ли уже такая поездка
        if not TripRailway.objects.filter(
            departure_station_name=departure_station, destination_station_name=destination_station
        ).exists():
            TripRailway.objects.create(
                departure_station_name=departure_station,
                destination_station_name=destination_station,
                cost_per_tonn_rw=fake.random_int(min=1000, max=5000),
            )


# Создаем клиентов со случайными данными
def create_client(n):
    user = choice(CustomUser.objects.all())
    for _ in range(n):
        Client.objects.create(
            client_name=fake.company(),
            contract_number=fake.bothify(text="???-######", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            contract_date=fake.date(),
            director_position=choice(DirectorPosition.objects.all()),
            director_name=f"{fake.first_name()} {fake.last_name()}",
            destination_city=choice(City.objects.all()),
            railway_station=choice(RailwayStation.objects.all()),
            receiver_name=fake.company(),
            receiver_id=fake.random_int(),
            receiver_okpo=fake.random_int(),
            receiver_adress=fake.address(),
            special_marks=fake.sentence(),
            last_application_number=fake.bothify(
                text="???-######", letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            ),
            user=user,
        )


# Создаем сорта муки из заданного списка
def create_flour():
    flour_names = ["Пшеничная", "Ржаная", "Овсяная"]
    for flour_name in flour_names:
        Flour.objects.create(flour_name=flour_name)


# Создаем бренды муки из заданного списка
def create_brand():
    brands = [
        ("Бело-Нежная", "Бело-Нежная"),
        ("Славна", "Славна"),
        ("Старооскольская", "Старооскольская"),
    ]
    for brand in brands:
        Brand.objects.create(brand=brand)


# Создаем случайный вес
def create_package(n):
    for _ in range(n):
        factory = choice(Factory.objects.all())
        Package.objects.create(
            package=fake.random_int(min=1, max=100),
            factory=factory,
            pallet_weight=fake.random_int(min=100, max=1000),
        )


# Создаем фабрики на основе случайных данных
def create_factory(n):
    for _ in range(n):
        Factory.objects.create(
            full_name=fake.company(),
            short_name=fake.company_suffix(),
            full_address=fake.address(),
            departure_city=fake.city(),
            departure_station_branch=fake.word(
                ext_word_list=["Северный", "Южный", "Западный", "Восточный"]
            ),
            departure_station_id=fake.random_int(),
            departure_station_name=fake.street_name(),
        )


# Создаем продукты из заранее созданных случайных данных
def create_product(n):
    for _ in range(n):
        flour_name = choice(Flour.objects.all())
        brand = choice(Brand.objects.all())
        package = choice(Package.objects.all())
        Product.objects.create(
            flour_name=flour_name,
            brand=brand,
            package=package,
            price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        )


# Выполняем все созданные функции
def run():
    create_positions()
    create_departments()
    create_superuser()
    create_user(2)
    create_director_position(3)
    create_city(3)
    create_railway_station(3)
    create_trip_auto(3)
    create_trip_railway(3)
    create_client(5)
    create_flour(3)
    create_brand()
    create_factory(3)
    create_package(3)
    create_product(5)
