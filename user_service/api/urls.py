# Django imports
from django.urls import path

# Project imports
from api.views import UserAPI, UserDetailAPI

urlpatterns = [
    path("users/", UserAPI.as_view(), name="User POST API"),
    path("users/<int:pk>", UserDetailAPI.as_view(), name="User RUD API"),
]
