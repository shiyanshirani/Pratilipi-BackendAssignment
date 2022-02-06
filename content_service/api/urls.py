# Django imports
from django.urls import path

# Project imports
from api.views import (
    BookAPI,
    BookDetailAPI,
    NewContentAPI,
    BookLikeAPI,
    BookReadAPI,
    TopContentAPI,
)

urlpatterns = [
    path("books", BookAPI.as_view(), name="Book API"),
    path("books/new", NewContentAPI.as_view(), name="Book Detail API"),
    path("books/<int:pk>", BookDetailAPI.as_view(), name="Book Detail API"),
    path(
        "book/like",
        BookLikeAPI.as_view(),
        name="Book LIKE EVENT",
    ),
    path(
        "book/read",
        BookReadAPI.as_view(),
        name="Book READ Event",
    ),
    path("books/top", TopContentAPI.as_view(), name="Top content list"),
]
