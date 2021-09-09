""" Model for Acme store """

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

# Utilities
from root.utils.models import RootBaseModel

# Models
from root.users.models.users import User


class Category(models.Model):
    """Category model"""

    name = models.CharField(
        _("category name"), max_length=100, unique=True, null=False, blank=False, help_text=_("Category name")
    )
    description = models.CharField(
        _("Description category"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Description category"),
    )

    class Meta:
        """Meta class"""

        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return "{}".format(self.name)


class Product(RootBaseModel):
    """Model for the products"""

    name = models.CharField(_("Product name"), max_length=100, null=False, blank=False)
    description = models.CharField(_("Description product"), max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    category_id = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.RESTRICT, db_column="category_id"
    )

    class Meta:
        """Meta class"""

        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return "{}".format(self.name)


class OrderRequest(models.Model):
    """OrderRequest model if it is purchase or sale"""

    name = models.CharField(
        _("order name"), max_length=100, unique=True, null=False, blank=False, help_text=_("Order name")
    )
    description = models.CharField(
        _("Description order"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Description order request"),
    )

    class Meta:
        """Meta class"""

        verbose_name = "order_request"
        verbose_name_plural = "order_requests"

    def __str__(self):
        return "{}".format(self.name)


class OperationDetail(RootBaseModel):
    """Table that stores the operation log"""

    category_id = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL, db_column="category_id"
    )
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, db_column="user_id")
    product_id = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL, db_column="product_id")
    type_operation_id = models.ForeignKey(
        OrderRequest, null=True, blank=True, on_delete=models.SET_NULL, db_column="type_operation_id"
    )
    quantity_total = models.IntegerField(
        _("Total quantity"), null=False, blank=False, help_text=_("Items sold/bought")
    )
    total_charge = models.DecimalField(
        _("Total charge"),
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False,
        help_text="Total amount of movement",
    )

    class Meta:
        """Meta class"""

        verbose_name = "operation_details"
        verbose_name_plural = "detail_operations"

    def __str__(self):
        return "{}".format(self.total_charge)
