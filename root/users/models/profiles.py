"""Profile model."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utilities
from root.utils.models import RootBaseModel


class Profile(RootBaseModel):
    """Profile model.

    User profile data
    A profile holds a user's public data like biography, picture,
    """

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    picture = models.ImageField(_("profile picture"), upload_to="users/pictures/", blank=True, null=True)
    biography = models.TextField(
        _("About your profile"),
        max_length=500,
        blank=True,
        help_text=_("A small biography about the user"),
    )

    initial_balance = models.DecimalField(
        _("Initial balance"),
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False,
        help_text="Opening balance to buy or sell",
        default=1000,
    )

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
