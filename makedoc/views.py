from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import DataDocSerializer
from .services import write_to_excel_auto, write_to_excel_rw, write_to_excel_sluzebnyi


def create_docs(request):
    write_to_excel_auto(request)
    write_to_excel_rw(request)
    # Если применяется скидка, пишем служебную записку
    write_to_excel_sluzebnyi(request) if 0 else None
    return HttpResponse("Документы сохранены")


class DataDocView(generics.GenericAPIView):  # type: ignore
    serializer_class = DataDocSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        return Response(validated_data, status=status.HTTP_200_OK)
