from typing import Any

from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from makedoc.services import Documents
from .data_service import DataService
from .serializers import DataDocSerializer


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


class DataDocView(generics.GenericAPIView[Any]):
    serializer_class = DataDocSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        processed_data = DataService.process_data(validated_data)

        return Response(processed_data, status=status.HTTP_200_OK)
