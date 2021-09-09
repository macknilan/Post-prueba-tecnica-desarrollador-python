"""Serializer of the orders"""

# DRF
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from root.Acme.models import OrderRequest


class OrdersSerializer(serializers.ModelSerializer):
    """Acme orders model serializer."""

    name = serializers.CharField(
        required=True,
        min_length=5,
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=OrderRequest.objects.all(),
                message="The order name must be unique ⚠️",
            )
        ],
    )

    class Meta:
        """Meta class"""

        model = OrderRequest
        fields = ["name", "description"]
        read_only_fields = [
            "id",
        ]
