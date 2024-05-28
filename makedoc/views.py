from django.http import HttpResponse

from .services import write_to_excel_auto, write_to_excel_rw, write_to_excel_sluzebnyi


def create_docs(request):
    write_to_excel_auto(request)
    write_to_excel_rw(request)
    # Если применяется скидка, пишем служебную записку
    write_to_excel_sluzebnyi(request) if 0 else None
    return HttpResponse("Документы сохранены")
