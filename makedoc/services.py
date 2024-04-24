import locale
import os
import openpyxl
import pymorphy3


from datetime import date, timedelta
from clients.models import Client
from logistics.models import RailwayStation
from users.models import CustomUser


morph = pymorphy3.MorphAnalyzer()
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


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


def get_current_date():
    # Сегодняшняя дата
    current_date = date.today()
    return current_date


def get_formatted_date_agreement():
    formatted_date_agreement = (
        f'«{get_current_date().day}» '
        f'{get_current_date().strftime("%B")} {get_current_date().year} г.'
    )
    return formatted_date_agreement


def get_formatted_date_shipment():
    current_date = get_current_date()
    next_month_date = current_date + timedelta(days=30)
    if next_month_date.month == current_date.month:
        formatted_date_shipment = (
            f"{morph.parse(current_date.strftime('%B'))[0].inflect({'nomn'}).word} "
            f"{current_date.year} г."
        )
    else:
        formatted_date_shipment = (
            f"{morph.parse(current_date.strftime('%B'))[0].inflect({'nomn'}).word}-"
            f"{morph.parse(next_month_date.strftime('%B'))[0].inflect({'nomn'}).word} "
            f"{current_date.year} г."
        )
    return formatted_date_shipment


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
