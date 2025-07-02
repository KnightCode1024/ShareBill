from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class Hello(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"msg": "Hello"})
