"""User model."""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

# Utilities
from root.utils.models import RootBaseModel


class User(RootBaseModel, AbstractUser):
    """User model.

    - Extend from Django's Abstract User, change the username field
    to email to make it unique.

    - The required fields are now username, first_name, last_name

    - The field phone_number is formatted by means of regular expressions

    - The new field is created is_client

    - The new field is created and by defauld is_verfied is set to
    false until it is verified by mail
    """

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )

    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message=_(
            "Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
        ),
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    is_public = models.BooleanField(
        default=True, help_text=_("Public profiles show all information about users.")
    )

    is_verified = models.BooleanField(
        _("verified"),
        default=False,
        help_text=_(
            "Determine if an user has a verified account. "
            "Set to true when user verified its email address."
        ),
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Function is overwritten and return username. Instead of first_name"""
        return self.username
