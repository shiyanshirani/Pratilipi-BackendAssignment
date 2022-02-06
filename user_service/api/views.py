# Project imports
from api.models import User
from api.serializers import UserSerializer
from api.authentication import CustomAuthentication

# Django imports
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password

# DRF imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
class UserAPI(APIView):
    """[User API for POST and GET request]

    Args:
        first_name: CharField
        last_name: CharField
        email: EmailField
        phone_number: CharField
        password: PasswordField
    """

    def post(self, request):
        try:
            user = User(
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                email=request.data["email"],
                phone_number=request.data["phone_number"],
                password=make_password(request.data["password"]),
            )
            user.save()

            return Response({"Success": "Profile saved."})

        except Exception as e:
            return Response({"Error": str(e)})

    def get(self, request):
        profiles = User.objects.all()
        serializer = UserSerializer(profiles, many=True)
        return Response(serializer.data)


class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    [User API - GET, UPDATE, DELETE by <id>]
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class ValidateUserAPI(APIView):
    """
    API to Validate user using their crendentials
    with a custom Basic Authentication in authentications.py
    """

    # authentication_classes = [CustomAuthentication]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        return Response(status=status.HTTP_200_OK)
