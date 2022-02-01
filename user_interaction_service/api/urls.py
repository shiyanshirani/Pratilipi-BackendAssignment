# Django imports
from django.urls import path

# Project imports
from api.views import UserInteractionAPI

urlpatterns = [path("", UserInteractionAPI.as_view(), name="content get list")]
