from datetime import date, timedelta

import babel.dates as bd
import pymorphy3

morph = pymorphy3.MorphAnalyzer()


def format_date_case(date_object, case):
    # case - падеж, https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#russian-cases
    return morph.parse(str(date_object))[0].inflect({case}).word


def format_month_ru_locale(date_object):
    return bd.format_date(date_object, "MMMM", locale="ru_RU")


def get_formatted_date_agreement():
    return bd.format_date(date.today(), "«d» MMMM y г.", locale="ru_RU")


def get_formatted_date_shipment(case):
    current_date = date.today()
    next_month_date = (current_date.replace(day=1) + timedelta(days=31)).replace(day=1)
    raw_current_month = format_month_ru_locale(current_date)
    raw_next_month = format_month_ru_locale(next_month_date)
    current_month = format_date_case(raw_current_month, case)
    next_month = format_date_case(raw_next_month, case)
    if current_date.year == next_month_date.year:
        return f"{current_month}-{next_month} {current_date.year} г."
    else:
        return f"{current_month} {current_date.year} г.-{next_month} {next_month_date.year} г."
