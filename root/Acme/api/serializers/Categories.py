"""Serializer of the categories"""

# DRF
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from root.Acme.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Acme categories model serializer."""

    name = serializers.CharField(
        required=True,
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=Category.objects.all(),
                message="The category name must be unique ⚠️",
            )
        ],
    )

    class Meta:
        """Meta class"""

        model = Category
        fields = ["name", "description"]
        read_only_fields = [
            "id",
        ]
