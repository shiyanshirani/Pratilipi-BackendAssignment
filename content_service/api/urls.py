# Django imports
from django.urls import path

# Project imports
from api.views import BookAPI, BookDetailAPI, NewContentAPI, UserInteractionServiceAPI

urlpatterns = [
    path("books/", BookAPI.as_view(), name="Book API"),
    path("books/new", NewContentAPI.as_view(), name="Book Detail API"),
    path("books/<int:pk>", BookDetailAPI.as_view(), name="Book Detail API"),
    path(
        "interaction/<int:pk>",
        UserInteractionServiceAPI.as_view(),
        name="user interaction coincide",
    ),
]
