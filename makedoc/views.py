from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import write_to_excel_auto, write_to_excel_rw, write_to_excel_sluzebnyi


def create_docs(request):
    write_to_excel_auto(request)
    write_to_excel_rw(request)
    write_to_excel_sluzebnyi(request)
    return HttpResponse("Документы сохранены")


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Test Authentication page using React Js and Django!"}
        return Response(content)
