# Django imports
from django.urls import path

# Project imports
from api.views import UserInteractionLike, UserInteractionRead

urlpatterns = [
    path("like", UserInteractionLike.as_view(), name="Like-event-API"),
    path("read", UserInteractionRead.as_view(), name="Read-event-API"),
]
