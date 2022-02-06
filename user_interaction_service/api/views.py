# Packages imports
import requests
from requests.auth import HTTPBasicAuth

# Django imports
from django.shortcuts import render

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserInteractionLike(APIView):
    """[Use Interaction Service - API to validate user and trigger Like and Read event]

    Args:
        APIView ([request, pk]): [Takes in args: book[id], user's credentials for validating user]
    """

    def post(self, request):
        # Content Service API - Validate User Endpoint
        user_service_check_url = "http://localhost:8001/api/users/check"
        # User Service API - Book 'Like' Endpoint
        content_service_url = "http://localhost:8000/api/book/like"

        email = request.data["email"]
        password = request.data["password"]

        response = requests.get(
            user_service_check_url, auth=HTTPBasicAuth(email, password)
        )

        # Validates User
        if response.status_code == 200:
            book_id = request.data["book_id"]
            data = {"book_id": book_id}
            response_back = requests.post(content_service_url, data=data)
            if response_back.status_code == 200:
                return Response({"detail": f"book_id: {book_id} Liked."})
            else:
                return Response({"detail": f"book_id: {book_id} not found."})
        else:
            return Response({"Error": "Invalid credentials"})


class UserInteractionRead(APIView):
    """[Use Interaction Service - API to validate user and trigger Like and Read event]

    Args:
        APIView ([request, pk]): [Takes in args: book[id], user's credentials for validating user]
    """

    def post(self, request):
        # Content Service API - Validate User Endpoint
        user_service_check_url = "http://localhost:8001/api/users/check"
        # User Service API - Book 'Like' Endpoint
        content_service_url = "http://localhost:8000/api/book/read"

        email = request.data["email"]
        password = request.data["password"]

        response = requests.get(
            user_service_check_url, auth=HTTPBasicAuth(email, password)
        )

        # Validates User
        if response.status_code == 200:
            book_id = request.data["book_id"]
            data = {"book_id": book_id}
            response_back = requests.post(content_service_url, data=data)
            if response_back.status_code == 200:
                return Response({"detail": f"book_id: {book_id} Read."})
            else:
                return Response({"detail": f"book_id: {book_id} not found."})
        else:
            return Response({"Error": "Invalid credentials"})
