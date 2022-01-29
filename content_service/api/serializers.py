# DRF imports
from rest_framework import serializers

# Project imports
from api.models import Book


class BookSerializer(serializers.Serializer):
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
