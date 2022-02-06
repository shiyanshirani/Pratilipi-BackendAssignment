# Project imports
from api.models import User

# Django imports
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, get_user_model

# DRF imports
from rest_framework import authentication
from rest_framework import exceptions


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.data["email"]
        password = request.data["password"]
        if not email:
            return None
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) is True:
                return (user, None)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")

        # return (user, None)
        return None
