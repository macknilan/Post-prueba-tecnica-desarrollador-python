""" Acme URL's """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from root.Acme.api.views import CategoryViewSet, ProductViewSet, OrdersViewSet, OperationsViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"orders", OrdersViewSet, basename="orders")
router.register(r"operations", OperationsViewSet, basename="operations")
app_name = "Acme"

urlpatterns = [
    # API
    path("", include(router.urls)),
]
