""" Acme models admin """

from django.contrib import admin

# Models
from root.Acme.models import Category, Product, OrderRequest, OperationDetail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "quantity", "category_id"]


@admin.register(OrderRequest)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]


@admin.register(OperationDetail)
class OperationDetailAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "category_id",
        "user_id",
        "product_id",
        "quantity_total",
        "type_operation_id",
        "total_charge",
    ]
