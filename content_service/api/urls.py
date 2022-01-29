# Django imports
from django.urls import path

# Project imports
from api.views import BookAPI, BookDetailAPI, NewContentAPI

urlpatterns = [
    path("books/", BookAPI.as_view(), name="Book API"),
    path("books/<int:pk>", BookDetailAPI.as_view(), name="Book Detail API"),
    path("books/new", NewContentAPI.as_view(), name="Book Detail API"),
]
