# Packages imports
import requests

# Django imports
from django.shortcuts import render

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserInteractionAPI(APIView):
    def get(self, request):
        response = requests.get(url="http://localhost:8000/api/books/")
        return Response(response.json())

    def post(self, request):
        
