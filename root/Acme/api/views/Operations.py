""" View for the operations in api """

from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from root.Acme.api.permissions import IsManagerAdmin

# Models
from django.db.models import RestrictedError
from root.users.models import User, Profile
from root.Acme.models import OperationDetail
from root.Acme.api.serializers import OperationsModelSerializer, CreateOperationsSerializer


class OperationsViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):

    """Handle the operations for buy and sell."""

    lookup_field = "id"

    def get_permissions(self):
        """Assign permissions based on actions."""

        permissions = [IsAuthenticated]
        if self.action in ["list", "retrieve"]:
            permissions = [AllowAny]
        elif self.action in ["destroy"]:
            permissions = [IsAuthenticated, IsManagerAdmin]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == "create":
            return CreateOperationsSerializer
        return OperationsModelSerializer

    def get_queryset(self):
        """List all categories without filters."""
        queryset = OperationDetail.objects.all()
        return queryset
