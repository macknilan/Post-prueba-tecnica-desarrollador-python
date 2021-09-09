# Django
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Serializers
from root.users.api.serializers.users import (
    UserModelSerializer,
    UserSignUpSerializer,
    UserLoginSerializer,
    AccountVerificationSerializer,
)
from root.users.api.serializers.profiles import ProfileModelSerializer

# Permissions
# https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.permissions import AllowAny, IsAuthenticated
from root.users.api.permissions import IsAccountOwner

# Models
from root.users.models.users import User


class UserViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """User view set.

    Handle sign up, login and account verification.
    """

    # Make query of active users
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    # Instead of doing the search by the ID/PK,
    # the search is made by the username in the URL
    lookup_field = "username"

    def get_permissions(self):
        """Assign permissions based on action.

        If the action is retrieve, custom permission is added
        so that only the same User can be edited and viewed
        """
        if self.action in ["login", "signup", "verify"]:
            permissions = [AllowAny]
        elif self.action in [
            "profile",
            "retrieve",
            "update",
            "partial_update",
        ]:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=["POST"])
    def login(self, request):
        """User sign in."""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        # breakpoint()
        data = {
            "user": UserModelSerializer(user).data,
            # 'access_token': token
            "token": str(token.access_token),
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def signup(self, request):
        """User sign up."""

        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["POST"])
    def verify(self, request):
        """Account verification."""

        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"message": "\,,/(^_^)\,,/  Congrats! u r verified"}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["PUT", "PATCH"])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""

        user = self.get_object()
        profile = user.profile
        partial = request.method == "PATCH"
        serializer = ProfileModelSerializer(profile, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        print(data)
        return Response(data)
