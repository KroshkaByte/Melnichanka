import os
from datetime import date, timedelta

import babel.dates as bd
import openpyxl
import pymorphy3

from clients.models import Client
from goods.models import Factory, Product
from logistics.models import City, RailwayStation
from users.models import CustomUser

morph = pymorphy3.MorphAnalyzer()


def get_region(request):
    return City.objects.first()


def get_factory(request):
    return Factory.objects.first()


def get_rw(request):
    return RailwayStation.objects.first()


def get_client(request):
    return Client.objects.all().first()


def get_user(request):
    return CustomUser.objects.first()


def get_logistics(request):
    pass


def get_product(request):
    return Product.objects.first()


def get_current_date():
    # Сегодняшняя дата
    return date.today()


def format_date_nomn_case(date_object):
    # Приводим дату к именительному падежу
    return morph.parse(date_object)[0].inflect({"nomn"}).word


def format_month_ru_locale(date_object):
    # Форматируем месяц  согласно русской локали
    return bd.format_date(date_object, "MMMM", locale="ru_RU")


def get_formatted_date_agreement():
    # Форматируем текущую дату согласно русской локали
    return bd.format_date(get_current_date(), "«d» MMMM y г.", locale="ru_RU")


def get_formatted_date_shipment():
    current_date = get_current_date()
    next_month_date = current_date.replace(day=1) + timedelta(days=31)
    raw_current_month = format_month_ru_locale(current_date)
    raw_next_month = format_month_ru_locale(next_month_date)
    current_month = format_date_nomn_case(raw_current_month)
    next_month = format_date_nomn_case(raw_next_month)
    if current_date.year == next_month_date.year:
        return f"{current_month}-{next_month} {current_date.year} г."
    else:
        return f"{current_month} {current_date.year} г.-{next_month} {next_month_date.year} г."


def write_to_excel_auto(request):
    user = get_user(request)
    client = get_client(request)
    product = get_product(request)
    factory = get_factory(request)

    # Открытие файла шаблона
    template_path = "makedoc/excel-templates/spec.xlsx"
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active

    # Форматирование даты договора
    formatted_contract_date = client.contract_date.strftime("%d.%m.%Y")

    # Номер приложения
    ws.cell(row=1, column=1, value=f"Приложение № {client.last_application_number}")

    # Номер договора
    ws.cell(
        row=2,
        column=1,
        value=f"к договору поставки № {client.contract_number} от {formatted_contract_date}г.",
    )
    ws.cell(row=4, column=1, value=client.client_name)
    ws.cell(row=6, column=6, value=get_formatted_date_agreement())

    # Значение строки для стартовой подвижной ячейки
    caret = 10

    # Берем количество товаров из реквеста
    goods_quantity = 3

    # Наполняем таблицу товарами
    for _ in range(goods_quantity):
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=3)
        ws.cell(row=caret, column=1, value=f"{str(product.flour_name)} {product.brand}")
        ws.cell(row=caret, column=4, value=product.package.package)
        # Берем из  реквеста (рефакторинг)
        ws.cell(row=caret, column=5, value=20)
        #  Возможно применить скидку тут
        ws.cell(row=caret, column=6, value=str(product.price))
        caret += 1

    caret += 1

    # Комбинат-грузоотправитель
    # Берем из реквеста (рефакторинг)
    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=2)
    ws.cell(row=caret, column=1, value="Грузоотправитель:")
    ws.cell(row=caret, column=3, value=factory.full_name)
    caret += 1

    # Автоуслуги
    # Проверка стоимости доставки в реквесте (рефакторинг)
    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=2)
    ws.cell(row=caret, column=1, value="Автотранспортные услуги:")
    ws.cell(
        row=caret,
        column=3,
        value="не входят в стоимость товара" if 0 else "входят в стоимость товара",
    )
    caret += 1

    # Срок отгрузки
    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=2)
    ws.cell(row=caret, column=1, value="Срок отгрузки:")

    ws.cell(row=caret, column=3, value=get_formatted_date_shipment())
    caret += 2

    # Право по дебиторской задолженности
    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)

    pdz = "▪Продавец имеет право не осуществлять отгрузку товара до полного погашения Покупателем \
просроченной дебиторской задолженности."
    ws.cell(row=caret, column=1, value=pdz)
    caret += 1

    # Юридическая информация
    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)

    contract_option = f"▪Настоящее приложение составлено и подписано в двух экземплярах, имеющих \
одинаковую юридическую силу, по одному для каждой из сторон, вступает в силу с момента \
подписания и является неотъемлемой частью договора № \
{client.contract_number} от {formatted_contract_date}г."
    ws.cell(row=caret, column=1, value=contract_option)
    caret += 4

    # Подписант продавца
    ws.cell(row=caret, column=1, value="Генеральный директор")
    caret += 1
    ws.cell(row=caret, column=1, value="ООО  «Торговый дом «Оскольская мука»")
    ws.cell(row=caret, column=6, value="С.А. Годизов")
    caret += 8

    # Подписант покупателя
    ws.cell(row=caret, column=1, value=str(client.director_position))
    caret += 1
    ws.cell(row=caret, column=1, value=client.client_name)
    # Нужно спарсить имя директора и вывести в сокращенном виде
    ws.cell(row=caret, column=6, value=client.director_name)

    caret = 49
    # Контакты менеджера
    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)
    ws.cell(row=caret, column=1, value=f"Ваш персональный менеджер: {user.full_name}")
    caret += 1

    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)
    ws.cell(
        row=caret,
        column=1,
        value=f"Тел. {user.phone_number_personal}, моб. {user.phone_number_work}",
    )

    # Тут предлагаю тоже отрефакторить, сделать отдельную функцию для сохранения объекта
    # Создать структуру каталогов
    directory = os.path.join(
        "makedoc", get_current_date().strftime("%d.%m.%Y"), user.full_name.split()[0]
    )
    os.makedirs(directory, exist_ok=True)

    # Сохранить файл
    new_file_path = os.path.join(
        directory,
        f"auto_{user.full_name.split()[0]}_{get_current_date().strftime('%d.%m.%Y')}.xlsx",
    )
    wb.save(new_file_path)


def write_to_excel_rw(request):
    user = get_user(request)
    client = get_client(request)
    product = get_product(request)
    rw = get_rw(request)
    factory = get_factory(request)

    # Открытие файла шаблона
    template_path = "makedoc/excel-templates/spec.xlsx"
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active

    # Форматирование даты договора
    formatted_contract_date = client.contract_date.strftime("%d.%m.%Y")

    # Номер приложения
    ws.cell(row=1, column=1, value=f"Приложение № {client.last_application_number}")

    # Номер договора
    ws.cell(
        row=2,
        column=1,
        value=f"к договору поставки № {client.contract_number} от {formatted_contract_date}г.",
    )
    ws.cell(row=4, column=1, value=client.client_name)
    ws.cell(row=6, column=6, value=get_formatted_date_agreement())

    # Значение строки для стартовой подвижной ячейки
    caret = 10

    # Берем количество товаров из реквеста
    goods_quantity = 3

    ws.cell(row=4, column=1, value=client.client_name)
    ws.cell(row=6, column=6, value=get_formatted_date_agreement())

    # Наполняем таблицу товарами
    for _ in range(goods_quantity):
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=3)
        ws.cell(row=caret, column=1, value=f"{str(product.flour_name)} {product.brand}")
        ws.cell(row=caret, column=4, value=product.package.package)
        # Берем из  реквеста (рефакторинг)
        ws.cell(row=caret, column=5, value=20)
        #  Возможно применить скидку тут
        ws.cell(row=caret, column=6, value=str(product.price))
        caret += 1

    caret += 1

    ws.cell(row=caret, column=1, value="Поставка осуществляется:")
    ws.cell(row=caret, column=3, value="ж/д транспортом")

    caret += 1

    # Станция назначения
    ws.cell(row=caret, column=1, value="Станция отправления:")
    ws.cell(row=caret, column=3, value=rw.station_name)

    caret += 1

    # Грузоотправитель
    ws.cell(row=caret, column=1, value="Грузоотправитель:")
    ws.cell(row=caret, column=3, value=factory.full_name)

    caret += 1

    # Условия поставки
    ws.cell(row=caret, column=1, value="Условия поставки")
    ws.cell(
        row=caret,
        column=3,
        value="франко-вагон станция отправления" if 0 else "франко-вагон станция назначения",
    )

    caret += 1

    # Срок отгрузки
    ws.cell(row=caret, column=1, value="Срок отгрузки:")
    ws.cell(row=caret, column=3, value=get_formatted_date_shipment())

    caret += 2

    # Отгрузочные реквизиты
    ws.cell(row=caret, column=1, value="Отгрузочные реквизиты:")

    caret += 1

    ws.cell(row=caret, column=1, value="Станция назначения:")
    ws.cell(row=caret, column=3, value=client.railway_station.station_name)

    caret += 1

    # Код станции
    ws.cell(row=caret, column=1, value="Код станции:")
    ws.cell(row=caret, column=3, value=client.railway_station.station_id)

    caret += 1

    # Получатель
    ws.cell(row=caret, column=1, value="Получатель:")
    ws.cell(row=caret, column=3, value=client.receiver_name)

    caret += 1

    # Код получателя
    ws.cell(row=caret, column=1, value="Код получателя:")
    ws.cell(row=caret, column=3, value=client.receiver_id)

    caret += 1

    # ОКПО
    ws.cell(row=caret, column=1, value="ОКПО:")
    ws.cell(row=caret, column=3, value=client.receiver_okpo)

    caret += 1

    # Адрес
    ws.cell(row=caret, column=1, value="Адрес:")
    ws.cell(row=caret, column=3, value=client.receiver_adress)

    caret += 2

    contract_option = f"▪Настоящее приложение составлено и подписано в двух экземплярах, имеющих \
одинаковую юридическую силу, по одному для каждой из сторон, вступает в силу с момента \
подписания и является неотъемлемой частью договора № \
{client.contract_number} от {formatted_contract_date}г."
    ws.cell(row=caret, column=1, value=contract_option)
    caret += 4

    # Подписант продавца
    ws.cell(row=caret, column=1, value="Генеральный директор")
    caret += 1
    ws.cell(row=caret, column=1, value="ООО  «Торговый дом «Оскольская мука»")
    ws.cell(row=caret, column=6, value="С.А. Годизов")
    caret += 8

    # Подписант покупателя
    ws.cell(row=caret, column=1, value=str(client.director_position))
    caret += 1
    ws.cell(row=caret, column=1, value=client.client_name)
    # Нужно спарсить имя директора и вывести в сокращенном виде
    ws.cell(row=caret, column=6, value=client.director_name)

    caret = 49
    # Контакты менеджера
    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)
    ws.cell(row=caret, column=1, value=f"Ваш персональный менеджер: {user.full_name}")
    caret += 1

    ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)
    ws.cell(
        row=caret,
        column=1,
        value=f"Тел. {user.phone_number_personal}, моб. {user.phone_number_work}",
    )

    # Создать структуру каталогов
    directory = os.path.join(
        "makedoc", get_current_date().strftime("%d.%m.%Y"), user.full_name.split()[0]
    )
    os.makedirs(directory, exist_ok=True)

    # Сохранить файл
    new_file_path = os.path.join(
        directory, f"rw_{user.full_name.split()[0]}_{get_current_date().strftime('%d.%m.%Y')}.xlsx"
    )
    wb.save(new_file_path)


def write_to_excel_sluzebnyi(request):
    user = get_user(request)
    city = get_region(request)
    client = get_client(request)

    # Принимаем с фронта макс размер скидки (пока хардкод)
    discount = 15

    # Открытие файла шаблона
    template_path = "makedoc/excel-templates/sluz.xlsx"
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active

    # Записка
    ws.cell(row=15, column=1, value=f"{get_formatted_date_agreement()} № 12/2.2/23/3-")
    text = f"В целях увеличения объема продаж на территории {city.region} прошу Вашего \
согласования применить скидку для контрагента {client.client_name} (г. {city.city}) до {discount}%\
в {get_formatted_date_shipment} на продукцию следующего ассортимента: "
    ws.cell(row=19, column=1, value=text)

    # Создать структуру каталогов
    directory = os.path.join(
        "makedoc", get_current_date().strftime("%d.%m.%Y"), user.full_name.split()[0]
    )
    os.makedirs(directory, exist_ok=True)

    # Сохранить файл
    new_file_path = os.path.join(
        directory,
        f"sluz_{user.full_name.split()[0]}_{get_current_date().strftime('%d.%m.%Y')}.xlsx",
    )
    wb.save(new_file_path)
