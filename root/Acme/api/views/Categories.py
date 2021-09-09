""" View for the categories in api """

from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from root.Acme.api.permissions import IsManagerAdmin

# Models
from django.db.models import RestrictedError
from root.Acme.models import Category
from root.Acme.api.serializers import CategorySerializer


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    """Class to do CRUD in the categories."""

    serializer_class = CategorySerializer
    lookup_field = "name"

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
        """List all categories without filters."""
        queryset = Category.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        """Verify that when a category is deleted it is not related to any products."""

        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except RestrictedError:
            data = {"message": "🛑 Can not delete: this  category has products! (parent has a child) ة_ة"}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)
