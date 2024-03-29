from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Test Authentication page using React Js and Django!"}
        return Response(content)
