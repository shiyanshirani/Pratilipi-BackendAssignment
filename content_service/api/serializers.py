# DRF imports
from rest_framework import serializers

# Project imports
from api.models import Book


class BookUploadSerializer(serializers.Serializer):
    input_file = serializers.FileField(
        required=True,
        allow_null=False,
        error_messages={
            "required": "Input fill is required.",
            "null": "Input fille cannot be null.",
        },
    )


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "story", "date_published", "user_id"]


class TopContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        order_by = ["-like_count", "-read_count"]


class NewContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        order_by = ["-date_published"]
