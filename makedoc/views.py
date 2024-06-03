from django.http import HttpResponse

from makedoc.services import Documents


def create_docs(request):
    docs = Documents()
    docs.update_documents(["auto", "rw", "sluz", "sopr_list"])

    if docs.auto:
        docs.form_auto_document(request)
    if docs.rw:
        docs.form_rw_document(request)

    return HttpResponse("Документы сохранены")
