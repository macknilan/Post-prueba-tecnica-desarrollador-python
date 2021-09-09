""" View for the products in api """

from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from root.Acme.api.permissions import IsManagerAdmin

# Models
from django.db.models import RestrictedError
from root.Acme.models import Category, Product
from root.Acme.api.serializers import ProductSerializer, ProductModelSerializer


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    """Class to do CRUD in the products."""

    serializer_class = ProductModelSerializer
    lookup_field = "id"

    def get_permissions(self):
        """Assign permissions based on actions."""

        if self.action in ["list", "retrieve"]:
            permissions = [AllowAny]
        elif self.action in ["create" "update", "partial_update" "destroy"]:
            permissions = [IsManagerAdmin]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """List all products without filters."""
        queryset = Product.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        """handle the creationa product with its category."""

        serializer = ProductSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        data = ProductModelSerializer(post).data
        return Response(data, status=status.HTTP_201_CREATED)
