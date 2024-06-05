from django.http import HttpResponse

from makedoc.services import Documents


def create_docs(request):
    docs = Documents()
    docs.update_documents(["auto", "rw", "service_note", "transport_sheet"])
    if docs.auto:
        docs.form_auto_document(request)
    if docs.rw:
        docs.form_rw_document(request)
    if docs.service_note:
        docs.form_service_note(request)
    if docs.transport_sheet:
        docs.form_transport_sheet(request)

    return HttpResponse("Документы сохранены")
