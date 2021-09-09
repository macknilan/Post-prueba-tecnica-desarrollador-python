"""Serializer of the products"""

# DRF
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from root.Acme.models import Product, Category


class ProductModelSerializer(serializers.ModelSerializer):
    """Acme products model serializer."""

    class Meta:
        """Meta class"""

        model = Product
        fields = ["name", "description", "price", "quantity", "category_id"]
        read_only_fields = [
            "id",
        ]


class ProductSerializer(serializers.ModelSerializer):
    """Handle the products model serializer."""

    name = serializers.CharField(
        required=True,
        min_length=10,
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=Product.objects.all(),
                message="The product name must be unique ⚠️",
            )
        ],
    )
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)
    quantity = serializers.IntegerField(max_value=100000, min_value=1, required=True)
    category_id = serializers.IntegerField(required=True)

    class Meta:
        """Meta class"""

        model = Product
        fields = ["name", "description", "price", "quantity", "category_id"]
        read_only_fields = ["id"]

    def validate_category_id(self, data):
        """Validate that the category to be assigned exists"""

        try:
            cat = Category.objects.get(id=data)
        except Category.DoesNotExist:
            raise serializers.ValidationError("The category does not exist with that name.")
        return data

    def create(self, data):
        """Create new product."""
        cat = Category.objects.get(id=data["category_id"])
        post = Product.objects.create(
            category_id=Category.objects.get(id=cat.id),
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )
        return post

    def update(self, instance, data):
        """Update product."""

        cat = Category.objects.get(name=data["category_id"])
        instance.name = data.get("name", instance.name)
        instance.description = data.get("description", instance.description)
        instance.price = data.get("price", instance.price)
        instance.quantity = data.get("quantity", instance.quantity)
        instance.category_id = Category.objects.get(id=cat.id)
        instance.save()

        return instance
