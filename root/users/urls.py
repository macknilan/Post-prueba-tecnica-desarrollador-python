""" Users / Templates URL's """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from root.users.api.views import UserViewSet

# from root.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )

router = DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet, basename="users")
app_name = "users"

urlpatterns = [
    # API
    path("", include(router.urls)),
    # TEMPLATE
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
