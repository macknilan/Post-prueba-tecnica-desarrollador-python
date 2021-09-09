"""Serializer of the operations details"""

# DRF
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from root.Acme.models import Category, Product, OrderRequest, OperationDetail
from root.users.models import User, Profile


class OperationsModelSerializer(serializers.ModelSerializer):
    """Acme operations details model serializer."""

    class Meta:
        """Meta class"""

        model = OperationDetail
        fields = ["category_id", "user_id", "product_id", "type_operation_id", "quantity_total", "total_charge"]
        read_only_fields = [
            "id",
        ]


class CreateOperationsSerializer(serializers.ModelSerializer):
    """Handle the creation of operation record"""

    category_id = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)
    product_id = serializers.CharField(required=True)
    type_operation_id = serializers.CharField(required=True)
    quantity_total = serializers.IntegerField(required=True)

    class Meta:
        """Meta class."""

        model = OperationDetail
        fields = ["category_id", "user_id", "product_id", "type_operation_id", "quantity_total"]
        read_only_fields = ["id", "total_charge"]

    def validate_category_id(self, data):
        """Validate that the category to be assigned exists"""

        try:
            cat = Category.objects.get(id=data)
        except Category.DoesNotExist:
            raise serializers.ValidationError("🚨 The category does not exist with that name. 🚨")
        return data

    def validate_user_id(self, data):
        """Validate that the user to be assigned exists"""

        try:
            usr = User.objects.get(id=data)
        except User.DoesNotExist:
            raise serializers.ValidationError("🚨 The user does not exist. 🚨")
        return data

    def validate_product_id(self, data):
        """Validate that the product to be assigned exists"""

        try:
            produc = Product.objects.get(id=data)
        except Product.DoesNotExist:
            raise serializers.ValidationError("🚨 The product does not exist with that name. 🚨")
        return data

    def validate_type_operation_id(self, data):
        """Validate that the order request to be assigned exists"""

        try:
            ord = OrderRequest.objects.get(id=data)
        except OrderRequest.DoesNotExist:
            raise serializers.ValidationError("🚨 The order request does not exist with that name. 🚨")
        return data

    def validate(self, data):
        """Validate the existence of sufficient items for the transaction

        Validate that there are sufficient funds for the transaction.
        """
        pro = Product.objects.get(id=data["product_id"])
        price_total = pro.price * data["quantity_total"]

        if data["quantity_total"] > Product.objects.get(id=data["product_id"]).quantity:
            raise serializers.ValidationError("🚨 There are not enough items to make the transaction. 🚨")
        if price_total > Profile.objects.get(id=data["user_id"]).initial_balance:
            raise serializers.ValidationError("🚨 There are not enough funds to carry out the transaction. 🚨")
        return data

    def create(self, data):
        """Create operation and update stats."""

        _category = Category.objects.get(id=data["category_id"])
        _user = User.objects.get(id=data["user_id"])
        _produc = Product.objects.get(id=data["product_id"])
        _order_rqst = OrderRequest.objects.get(id=data["type_operation_id"])

        _produc.quantity = _produc.quantity - data["quantity_total"]
        _total_charge = _produc.price * data["quantity_total"]

        # import ipdb; ipdb.set_trace()
        # breakpoint()

        op_detail = OperationDetail.objects.create(
            category_id=_category,
            user_id=_user,
            product_id=_produc,
            type_operation_id=_order_rqst,
            quantity_total=data["quantity_total"],
            total_charge=_total_charge,
        )
        profile = Profile.objects.get(id=data["user_id"])
        profile.initial_balance -= _total_charge
        profile.save()

        return op_detail
