import babel.dates
from datetime import date, timedelta


def get_current_date():
    # Сегодняшняя дата
    current_date = date.today()
    return current_date


def get_formatted_date_agreement():
    # Форматируем дату согласно русской локали
    formatted_date_agreement = babel.dates.format_date(
        get_current_date(), "«d» MMMM y г.", locale="ru_RU"
    )
    return formatted_date_agreement


def get_formatted_date_shipment():
    current_date = get_current_date()
    next_month_date = current_date + timedelta(days=30)
    if next_month_date.month == current_date.month:
        formatted_date_shipment = babel.dates.format_date(
            current_date, "MMMM y г.", locale="ru_RU"
        )
    else:
        formatted_date_shipment = (
            f"{babel.dates.format_date(current_date, 'MMMM', locale='ru_RU')}-"
            f"{babel.dates.format_date(next_month_date, 'MMMM', locale='ru_RU')} "
            f"{current_date.year} г."
        )
    return formatted_date_shipment


print(get_formatted_date_agreement())
print(get_formatted_date_shipment())
