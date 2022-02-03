# Project imports
from api.models import User
from api.serializers import UserSerializer
from api.authentication import MyAuthentication

# Django imports
from django.contrib.auth import authenticate, login

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Django Imports

# from api.backends import MyAuthBackend

# Create your views here.
class UserAPI(APIView):
    def post(self, request):
        try:
            user = User(
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                email=request.data["email"],
                phone_number=request.data["phone_number"],
                password=request.data["password"],
            )
            user.save()

            return Response({"Success": "Profile saved."})

        except Exception as e:
            return Response({"Error": str(e)})

    def get(self, request):
        profiles = User.objects.all()
        result = []
        for profile in profiles:
            item = {
                "id": profile.id,
                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "email": profile.email,
                "phone_number": profile.phone_number,
            }
            result.append(item)
        return Response(result)


class UserDetailAPI(RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserInteractionServiceAPI(APIView):
    authentication_classes = (CustomAuthentication,)

    def get(self, request, format=None):
        content = {
            "user": str(request.user),  # `django.contrib.auth.User` instance.
            "auth": str(request.auth),  # None
        }
        return Response(content)
