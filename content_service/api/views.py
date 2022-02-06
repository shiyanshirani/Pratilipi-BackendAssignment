# Package imports
import pandas as pd

# Django imports
from django.http import Http404, HttpResponseNotFound

# DRF Imports
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# Project imports
from api.models import Book
from api.tasks import csv_to_db
from api.serializers import BookUploadSerializer
from api.serializers import (
    BookDetailSerializer,
    NewContentSerializer,
    TopContentSerializer,
)


REQUIRED_COLUMNS = ["title", "story", "user_id"]

# Create your views here.


class TopContentAPI(APIView):
    """
    API to return list of Book on their 'like' and 'read' order.
    """

    def get(self, request):
        books = Book.objects.all()
        serializer = TopContentSerializer(books, many=True)
        return Response(serializer.data)


class NewContentAPI(APIView):
    """
    API to return the latest content
    """

    def get(self, request):
        books = Book.objects.all()
        serializer = NewContentSerializer(books, many=True)
        return Response(serializer.data)


class BookAPI(APIView):
    """
    API to POST and GET Book
    """

    def post(self, request):
        serializer = BookUploadSerializer(data=request.data)
        if serializer.is_valid():
            csv_file = serializer.validated_data["input_file"]  # Data ingestion of csv
            csv_to_db(csv_file)
            return Response({"Success": "Content added."})

        return Response({"Detail": "Error"})

    def get(self, request):
        books = Book.objects.all()
        serializer = BookDetailSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailAPI(APIView):
    """
    RETRIEVE, UPDATE or DELETE a Book instance.
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


class BookLikeAPI(APIView):
    """
    API to trigger 'Like' endpoint
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return HttpResponseNotFound

    def post(self, request, format=None):
        book_id = request.data["book_id"]
        book = self.get_object(pk=book_id)
        try:
            book.like_count += 1
            book.save()
            return Response({"Detail": "Success"})

        except Exception as e:
            return HttpResponseNotFound


class BookReadAPI(APIView):
    """
    API to trigger 'Read' endpoint
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return HttpResponseNotFound

    def post(self, request, format=None):
        book_id = request.data["book_id"]
        book = self.get_object(pk=book_id)
        try:
            book.read_count += 1
            book.save()
            return Response({"Detail": "Success"})

        except Exception as e:
            return HttpResponseNotFound
