import os
from datetime import date, timedelta

import babel.dates as bd
import openpyxl
import pymorphy3

from clients.models import Client
from goods.models import Factory, Product
from logistics.models import RailwayStation
from users.models import CustomUser

morph = pymorphy3.MorphAnalyzer()


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

    # Открытие файла шаблона
    template_path = "makedoc/excel-templates/auto.xlsx"
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
    ws.cell(row=caret, column=3, value=str(Factory.objects.first()))
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
    rw = get_rw(request)

    # Открытие файла шаблона
    template_path = "makedoc/excel-templates/rw.xlsx"
    workbook = openpyxl.load_workbook(template_path)
    worksheet = workbook.active

    # Форматирование даты договора
    formatted_contract_date = client.contract_date.strftime("%d.%m.%Y")

    # Разьеденить ячейки
    worksheet.unmerge_cells("A1:F1")
    worksheet.unmerge_cells("A2:F2")
    worksheet.unmerge_cells("A4:F4")
    worksheet.unmerge_cells("A26:F26")
    worksheet.unmerge_cells("A49:F49")
    worksheet.unmerge_cells("A50:F50")

    # Записать значений в ячейки
    worksheet["A1"] = f"Приложение № {client.last_application_number}"
    worksheet["A2"] = (
        f"к договору поставки № {client.contract_number} от {formatted_contract_date}г."
    )
    worksheet["A4"] = f"ООО  (ИП, АО)  «{client.client_name}»"
    worksheet["F6"] = get_formatted_date_agreement()
    worksheet[
        "A26"
    ] = f"▪Настоящее приложение составлено и подписано в двух экземплярах, имеющих одинаковую \
            юридическую силу, по одному для каждой из сторон, вступает в силу с момента \
                подписания и является неотъемлемой частью договора № {client.contract_number} \
                    от {formatted_contract_date}г."
    worksheet["C16"] = get_formatted_date_shipment()
    worksheet["C19"] = rw.station_name
    worksheet["C20"] = rw.station_id
    worksheet["C21"] = f"ООО  (ИП, АО) {client.receiver_name}"
    worksheet["C22"] = client.receiver_id
    worksheet["C23"] = client.receiver_okpo
    worksheet["C24"] = client.receiver_adress
    worksheet["A42"] = f"{client.director_position}"
    worksheet["A43"] = client.client_name
    worksheet["F43"] = client.director_name
    worksheet["A49"] = f"Ваш персональный менеджер: {user.full_name}"
    worksheet["A50"] = f"Тел. {user.phone_number_personal}, моб. {user.phone_number_work}"

    # Объединить ячейки
    worksheet.merge_cells("A1:F1")
    worksheet.merge_cells("A2:F2")
    worksheet.merge_cells("A4:F4")
    worksheet.merge_cells("A26:F26")
    worksheet.merge_cells("A49:F49")
    worksheet.merge_cells("A50:F50")

    # Создать структуру каталогов
    directory = os.path.join(
        "makedoc", get_current_date().strftime("%d.%m.%Y"), user.full_name.split()[0]
    )
    os.makedirs(directory, exist_ok=True)

    # Сохранить файл
    new_file_path = os.path.join(
        directory, f"rw_{user.full_name.split()[0]}_{get_current_date().strftime('%d.%m.%Y')}.xlsx"
    )
    workbook.save(new_file_path)


def write_to_excel_sluzebnyi(request):
    user = get_user(request)

    # Открытие файла шаблона
    template_path = "makedoc/excel-templates/sluz.xlsx"
    workbook = openpyxl.load_workbook(template_path)
    worksheet = workbook.active

    # Разьеденить ячейки
    worksheet.unmerge_cells("A19:H19")

    # Записка
    worksheet["A15"] = f"{get_formatted_date_agreement()} № 12/2.2/23/3-"
    worksheet["A19"] = ""

    # Объединить ячейки
    worksheet.merge_cells("A19:H19")

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
    workbook.save(new_file_path)
