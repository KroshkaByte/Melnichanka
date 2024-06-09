import json
from typing import Any

from django.core.cache import cache
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from makedoc.services import Documents
from .serializers import DataDocSerializer, DocumentsSimpleSerializer


class CreateDocsView(APIView):
    serializer_class = DocumentsSimpleSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cache_key = f"validated_data_{request.user.id}"
        validated_data = cache.get(cache_key)

        if validated_data is None:
            return Response(
                {"error": "No data found in cache"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validated_data = json.loads(validated_data)
        except json.JSONDecodeError:
            return Response({"error": "Invalid data in cache"}, status=status.HTTP_400_BAD_REQUEST)

        docs = Documents(validated_data)
        docs.update_documents()
        if docs.auto:
            docs.form_auto_document(request)
        if docs.rw:
            docs.form_rw_document(request)
        if docs.service_note:
            docs.form_service_note(request)
        if docs.transport_sheet:
            docs.form_transport_sheet(request)

        return Response(
            {"message": "Документы сохранены", "data": validated_data}, status=status.HTTP_200_OK
        )


class DataDocView(generics.GenericAPIView[Any]):
    serializer_class = DataDocSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        # Use a more unique cache key
        cache_key = f"validated_data_{request.user.id}"
        cache.set(cache_key, json.dumps(validated_data), 120)

        return Response({"success": True, "data": validated_data}, status=status.HTTP_200_OK)
