import os
from datetime import date, timedelta

import babel.dates as bd
import openpyxl
import pymorphy3
from openpyxl.styles import Alignment, Border, Font, Side

from clients.models import Client
from goods.models import Factory, Product
from logistics.models import City, RailwayStation
from users.models import CustomUser

morph = pymorphy3.MorphAnalyzer()


def get_current_date():
    return date.today()


def format_date_case(date_object, case):
    # case - падеж
    return morph.parse(str(date_object))[0].inflect({case}).word


def format_month_ru_locale(date_object):
    return bd.format_date(date_object, "MMMM", locale="ru_RU")


def get_formatted_date_agreement():
    return bd.format_date(get_current_date(), "«d» MMMM y г.", locale="ru_RU")


def get_formatted_date_shipment(case):
    current_date = get_current_date()
    next_month_date = (current_date.replace(day=1) + timedelta(days=31)).replace(day=1)
    raw_current_month = format_month_ru_locale(current_date)
    raw_next_month = format_month_ru_locale(next_month_date)
    current_month = format_date_case(raw_current_month, case)
    next_month = format_date_case(raw_next_month, case)
    if current_date.year == next_month_date.year:
        return f"{current_month}-{next_month} {current_date.year} г."
    else:
        return f"{current_month} {current_date.year} г.-{next_month} {next_month_date.year} г."


class Documents:
    def __init__(self):
        self.auto = 0
        self.rw = 0
        self.service_note = 0
        self.transport_sheet = 0

    def update_documents(self, documents_list):
        if "auto" in documents_list:
            self.auto = 1
        if "rw" in documents_list:
            self.rw = 1
        if "service_note" in documents_list:
            self.service_note = 1
        if "transport_sheet" in documents_list:
            self.transport_sheet = 1

    def form_auto_document(self, request):
        self.docname = "auto"
        try:
            user = self.get_user(request)
            client = self.get_client(request)
            product = self.get_product(request)
            factory = self.get_factory(request)
            logistics = self.get_logistics(request)
        except Exception as e:
            return f"Error fetching data: {e}"

        template_path = "makedoc/excel-templates/spec.xlsx"
        wb = openpyxl.load_workbook(template_path)
        ws = wb.active

        self.fill_contract_info(ws, client)
        self.fill_product_info(ws, product, logistics, 10)
        self.fill_factory_info(ws, factory)
        self.fill_auto_services(ws, logistics)
        self.fill_debt_info(ws)
        self.fill_legal_info(ws, client)
        self.fill_signatures(ws, client)
        self.fill_manager_contact(ws, user)

        self.apply_styles(ws)

        self.save_workbook(wb, user)

    def fill_contract_info(self, ws, client):
        formatted_contract_date = client.contract_date.strftime("%d.%m.%Y")
        title = ws.cell(row=1, column=1, value=f"Приложение № {client.last_application_number}")
        title.font = Font(bold=True)
        ws.cell(
            row=2,
            column=1,
            value=f"к договору поставки № {client.contract_number} от {formatted_contract_date}г.",
        )
        ws.cell(row=4, column=1, value=client.client_name)
        ws.cell(row=6, column=6, value=get_formatted_date_agreement())

    def fill_product_info(self, ws, product, logistics, caret):
        goods_quantity = 7
        thin_border = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin"),
        )

        for _ in range(goods_quantity):
            ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=3)
            ws.cell(row=caret, column=1, value=f"{str(product.flour_name)} {product.brand}")
            ws.cell(row=caret, column=4, value=product.package.package)
            ws.cell(row=caret, column=5, value=20)
            ws.cell(row=caret, column=6, value=str(product.price))
            ws.cell(row=caret, column=7, value=logistics)
            ws.cell(row=caret, column=8, value=product.price - logistics)

            for col_num in range(1, 9):
                cell = ws.cell(row=caret, column=col_num)
                cell.border = thin_border
                if cell.column > 2:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
            caret += 1
        self.caret_product = caret + 1

    def fill_factory_info(self, ws, factory):
        caret = self.caret_product
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=2)
        ws.cell(row=caret, column=1, value="Грузоотправитель:")
        ws.cell(row=caret, column=3, value=factory.full_name)
        self.caret_factory = caret + 1

    def fill_auto_services(self, ws, logistics):
        caret = self.caret_factory
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=2)
        ws.cell(row=caret, column=1, value="Автотранспортные услуги:")
        ws.cell(
            row=caret,
            column=3,
            value="не входят в стоимость товара"
            if logistics != 0
            else "входят в стоимость товара",
        )
        self.caret_services = caret + 1

    def fill_debt_info(self, ws):
        caret = self.caret_services
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=2)
        ws.cell(row=caret, column=1, value="Срок отгрузки:")
        ws.cell(row=caret, column=3, value=get_formatted_date_shipment("nomn"))
        ws.merge_cells(start_row=caret + 1, start_column=1, end_row=caret + 1, end_column=6)
        pdz = "▪Продавец имеет право не осуществлять отгрузку товара до полного погашения \
Покупателем просроченной дебиторской задолженности."
        debt = ws.cell(row=caret + 1, column=1, value=pdz)
        debt.alignment = Alignment(wrap_text=True, horizontal="justify", vertical="center")
        ws.row_dimensions[caret + 1].height = 30
        self.caret_debt = caret + 2

    def fill_legal_info(self, ws, client):
        caret = self.caret_debt
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)
        formatted_contract_date = client.contract_date.strftime("%d.%m.%Y")
        contract_option = f"▪Настоящее приложение составлено и подписано в двух экземплярах, \
имеющих одинаковую юридическую силу, по одному для каждой из сторон, вступает в силу с момента \
подписания и является неотъемлемой частью договора № {client.contract_number} от \
{formatted_contract_date}г."
        legal = ws.cell(row=caret, column=1, value=contract_option)
        legal.alignment = Alignment(wrap_text=True, horizontal="justify", vertical="center")
        ws.row_dimensions[caret].height = 40
        self.caret_legal = caret + 4

    def fill_signatures(self, ws, client):
        caret = self.caret_legal
        ws.cell(row=caret, column=1, value="Генеральный директор")
        ws.cell(row=caret + 1, column=1, value="ООО  «Торговый дом «Оскольская мука»")
        ws.cell(row=caret + 1, column=6, value="С.А. Годизов")
        ws.cell(row=caret + 9, column=1, value=str(client.director_position))
        ws.cell(row=caret + 10, column=1, value=client.client_name)
        ws.cell(row=caret + 10, column=6, value=client.director_name)
        self.caret_signatures = caret + 11

    def fill_manager_contact(self, ws, user):
        caret = 59
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=6)
        manager = ws.cell(
            row=caret, column=1, value=f"Ваш персональный менеджер: {user.full_name}"
        )
        manager.alignment = Alignment(horizontal="center", vertical="center")
        ws.merge_cells(start_row=caret + 1, start_column=1, end_row=caret + 1, end_column=6)
        phone = ws.cell(
            row=caret + 1,
            column=1,
            value=f"Тел. {user.phone_number_personal}, моб. {user.phone_number_work}",
        )
        phone.alignment = Alignment(horizontal="center", vertical="center")

    def save_workbook(self, wb, user):
        directory = os.path.join(
            "makedoc",
            "tempdoc",
            get_current_date().strftime("%d.%m.%Y"),
            user.full_name.split()[0],
        )
        os.makedirs(directory, exist_ok=True)
        new_file_path = os.path.join(
            directory,
            f"{self.docname}_{user.full_name.split()[0]}_\
{get_current_date().strftime('%d.%m.%Y')}.xlsx",
        )
        wb.save(new_file_path)

    def apply_styles(self, ws):
        for row in ws.iter_rows():
            for cell in row:
                if cell.value is not None:
                    cell.font = Font(name="Times New Roman", size=12)

        for row_num in [1, 9]:
            for cell in ws[row_num]:
                if cell.value is not None:
                    cell.font = Font(bold=True, size=12)

    def get_user(self, request):
        try:
            return CustomUser.objects.first()
        except CustomUser.DoesNotExist:
            raise Exception("User not found")

    def get_client(self, request):
        try:
            return Client.objects.all().first()
        except Client.DoesNotExist:
            raise Exception("Client not found")

    def get_product(self, request):
        try:
            return Product.objects.first()
        except Product.DoesNotExist:
            raise Exception("Product not found")

    def get_factory(self, request):
        try:
            return Factory.objects.first()
        except Factory.DoesNotExist:
            raise Exception("Factory not found")

    def get_rw(self, request):
        try:
            return RailwayStation.objects.all().first()
        except RailwayStation.DoesNotExist:
            raise Exception("Railway station not found")

    def get_discount(self, request):
        return 15

    def get_city(self, request):
        try:
            return City.objects.all().first()
        except City.DoesNotExist:
            raise Exception("City not found")

    def get_logistics(self, request):
        return 2500

    def form_rw_document(self, request):
        self.docname = "rw"
        try:
            user = self.get_user(request)
            client = self.get_client(request)
            product = self.get_product(request)
            rw = self.get_rw(request)
            factory = self.get_factory(request)
            logistics = self.get_logistics(request)
        except Exception as e:
            return f"Error fetching data: {e}"

        template_path = "makedoc/excel-templates/spec.xlsx"
        wb = openpyxl.load_workbook(template_path)
        ws = wb.active

        self.fill_contract_info(ws, client)
        self.fill_product_info(ws, product, logistics, 10)
        self.fill_factory_info(ws, factory)
        self.fill_rw_services(ws, rw, factory, client)
        self.fill_debt_info(ws)
        self.fill_legal_info(ws, client)
        self.fill_signatures(ws, client)
        self.fill_manager_contact(ws, user)

        self.apply_styles(ws)

        self.save_workbook(wb, user)

    def fill_rw_services(self, ws, rw, factory, client):
        caret = self.caret_factory
        ws.merge_cells(start_row=caret, start_column=1, end_row=caret, end_column=2)
        ws.cell(row=caret, column=1, value="Поставка осуществляется:")
        ws.cell(row=caret, column=3, value="ж/д транспортом")
        caret += 1

        ws.cell(row=caret, column=1, value="Станция отправления:")
        ws.cell(row=caret, column=3, value=rw.station_name)
        caret += 1

        ws.cell(row=caret, column=1, value="Грузоотправитель:")
        ws.cell(row=caret, column=3, value=factory.full_name)
        caret += 1

        ws.cell(row=caret, column=1, value="Условия поставки")
        ws.cell(
            row=caret,
            column=3,
            value="франко-вагон станция отправления" if 0 else "франко-вагон станция назначения",
        )
        caret += 2

        ws.cell(row=caret, column=1, value="Отгрузочные реквизиты:")
        caret += 1

        ws.cell(row=caret, column=1, value="Станция назначения:")
        ws.cell(row=caret, column=3, value=client.railway_station.station_name)
        caret += 1

        ws.cell(row=caret, column=1, value="Код станции:")
        station_code_value = ws.cell(row=caret, column=3, value=client.railway_station.station_id)
        station_code_value.alignment = Alignment(horizontal="left")
        caret += 1

        ws.cell(row=caret, column=1, value="Получатель:")
        ws.cell(row=caret, column=3, value=client.receiver_name)
        caret += 1

        ws.cell(row=caret, column=1, value="Код получателя:")
        receiver_code_value = ws.cell(row=caret, column=3, value=client.receiver_id)
        receiver_code_value.alignment = Alignment(horizontal="left")
        caret += 1

        ws.cell(row=caret, column=1, value="ОКПО:")
        okpo_value = ws.cell(row=caret, column=3, value=client.receiver_okpo)
        okpo_value.alignment = Alignment(horizontal="left")
        caret += 1

        ws.cell(row=caret, column=1, value="Адрес:")
        ws.cell(row=caret, column=3, value=client.receiver_adress)
        caret += 1

        self.caret_services = caret + 1

    def form_service_note(self, request):
        self.docname = "service_note"
        try:
            client = self.get_client(request)
            discount = self.get_discount(request)
            city = self.get_city(request)
            user = self.get_user(request)
            product = self.get_product(request)
            logistics = self.get_logistics(request)
        except Exception as e:
            return f"Error fetching data: {e}"

        # Открытие файла шаблона
        template_path = "makedoc/excel-templates/service_note.xlsx"
        wb = openpyxl.load_workbook(template_path, keep_vba=True)
        ws = wb.active

        self.fill_text_note(ws, client, discount, city)
        self.fill_product_info(ws, product, logistics, 22)
        self.apply_styles(ws)

        self.save_workbook(wb, user)

    def fill_text_note(self, ws, client, discount, city):
        ws.cell(row=15, column=1, value=f"{get_formatted_date_agreement()} № 12/2.2/23/3-")
        text = f"    В целях увеличения объема продаж на территории {city.region} прошу Вашего \
согласования применить скидку для контрагента {client.client_name} (г. {city.city}) до {discount}%\
 в {get_formatted_date_shipment("loct")} на продукцию следующего ассортимента: "
        ws.cell(row=19, column=1, value=text)

    def form_transport_sheet(self, request):
        self.docname = "transport_sheet"
        try:
            user = self.get_user(request)
            product = self.get_product(request)
            client = self.get_client(request)
            logistics = self.get_logistics(request)
            factory = self.get_factory(request)
        except Exception as e:
            return f"Error fetching data: {e}"

        template_path = "makedoc/excel-templates/transport_sheet.xlsx"
        wb = openpyxl.load_workbook(template_path, keep_vba=True)
        ws = wb.active

        self.fill_contract_info_transport_sheet(ws, client)
        self.fill_product_info(ws, product, logistics, 11)

        self.fill_factory_info(ws, factory)
        self.fill_auto_services(ws, logistics)
        self.fill_debt_info(ws)
        self.fill_legal_info(ws, client)
        self.fill_signatures(ws, client)
        self.fill_manager_contact(ws, user)

        self.apply_styles(ws)

        self.save_workbook(wb, user)

    def fill_contract_info_transport_sheet(self, ws, client):
        formatted_contract_date = client.contract_date.strftime("%d.%m.%Y")
        ws.cell(row=1, column=1, value="СОПРОВОДИТЕЛЬНЫЙ ЛИСТ к")
        title = ws.cell(row=2, column=1, value=f"Приложению № {client.last_application_number}")
        title.font = Font(bold=True)
        ws.cell(
            row=3,
            column=1,
            value=f"к договору поставки № {client.contract_number} от {formatted_contract_date}г.",
        )
        ws.cell(row=5, column=1, value=client.client_name)
        ws.cell(row=7, column=8, value=get_formatted_date_agreement())
