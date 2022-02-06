# Django imports
from django.urls import path

# Project imports
from api.views import UserAPI, UserDetailAPI, ValidateUserAPI

urlpatterns = [
    path("users", UserAPI.as_view(), name="User POST API"),
    path("users/<int:pk>", UserDetailAPI.as_view(), name="User RUD API"),
    path("users/check", ValidateUserAPI.as_view(), name="Validate user"),
]
