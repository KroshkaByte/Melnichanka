import os
from datetime import date, timedelta

import babel.dates as bd
import openpyxl
import pymorphy3

from clients.models import Client
from logistics.models import RailwayStation
from users.models import CustomUser


def get_rw(request):
    rw = RailwayStation.objects.get(id=1)
    return rw


def get_client(request):
    client = Client.objects.all().first()
    return client


def get_user(request):
    user = CustomUser.objects.get(id=1)
    return user


def get_logistics(request):
    pass


morph = pymorphy3.MorphAnalyzer()


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

    # Открытие файла шаблона
    template_path = "exel-templates/auto.xlsx"
    workbook = openpyxl.load_workbook(template_path)
    worksheet = workbook.active

    # Форматирование даты договора
    formatted_contract_date = client.contract_date.strftime("%d.%m.%Y")

    # Разьеденить ячейки
    worksheet.unmerge_cells("A1:F1")
    worksheet.unmerge_cells("A2:F2")
    worksheet.unmerge_cells("A4:F4")
    worksheet.unmerge_cells("A17:F17")
    worksheet.unmerge_cells("A49:F49")
    worksheet.unmerge_cells("A50:F50")

    # Записать значений в ячейки
    worksheet["A1"] = f"Приложение № {client.last_application_number}"
    worksheet["A2"] = (
        f"к договору поставки № {client.contract_number} от {formatted_contract_date}г."
    )
    worksheet["A4"] = f"ООО  (ИП, АО)  «{client.client_name}»"
    worksheet["F6"] = get_formatted_date_agreement()
    worksheet["A17"] = (
        f"▪Настоящее приложение составлено и подписано в двух экземплярах, имеющих одинаковую "
        f"юридическую силу, по одному для каждой из сторон, вступает в силу с момента "
        f"подписания и является неотъемлемой частью договора № {client.contract_number} "
        f"от {formatted_contract_date}г."
    )
    worksheet["C14"] = get_formatted_date_shipment()
    worksheet["A35"] = f"{client.director_position}"
    worksheet["A36"] = client.client_name
    worksheet["F36"] = client.director_name
    worksheet["A49"] = f"Ваш персональный менеджер: {user.full_name}"
    worksheet["A50"] = f"Тел. {user.phone_number_personal}, моб. {user.phone_number_work}"

    # Объединить ячейки
    worksheet.merge_cells("A1:F1")
    worksheet.merge_cells("A2:F2")
    worksheet.merge_cells("A4:F4")
    worksheet.merge_cells("A17:F17")
    worksheet.merge_cells("A49:F49")
    worksheet.merge_cells("A50:F50")

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
    workbook.save(new_file_path)


def write_to_excel_rw(request):
    user = get_user(request)
    client = get_client(request)
    rw = get_rw(request)

    # Открытие файла шаблона
    template_path = "exel-templates/rw.xlsx"
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
    template_path = "exel-templates/sluz.xlsx"
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
