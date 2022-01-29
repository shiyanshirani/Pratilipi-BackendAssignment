# Package imports
import pandas as pd

# DRF Imports
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# Project imports
from api.models import Book
from api.tasks import csv_to_db
from api.serializers import BookSerializer
from api.serializers import BookDetailSerializer


REQUIRED_COLUMNS = ["title", "story", "user_id"]

# Create your views here.


class NewContentAPI(APIView):
    def get(self, request):
        books = Book.objects.order_by("-date_published")
        result = []
        for book in books:
            item = {
                "id": book.id,
                "title": book.title,
                "story": book.story,
                "date_published": book.date_published,
                "user_id": book.user_id,
            }
            result.append(item)

        return Response(result)


class BookAPI(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            csv_file = serializer.validated_data["input_file"]
            csv_to_db(csv_file)
            return Response({"Success": "Content added."})

        return Response({"Detail": "Error"})

    def get(self, request):
        books = Book.objects.all()
        result = []
        for book in books:
            item = {
                "id": book.id,
                "title": book.title,
                "story": book.story,
                "date_published": book.date_published,
                "user_id": book.user_id,
            }
            result.append(item)

        return Response(result)


class BookDetailAPI(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"Detail": "DoesNotExist"})

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        result = {
            "id": book.id,
            "title": book.title,
            "story": book.story,
            "date_published": book.date_published,
            "user_id": book.user_id,
        }
        return Response(result)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookDetailSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response({"Detail": "Deleted"})
