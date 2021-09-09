from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AcmeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "root.Acme"
    verbose_name = _("Acme")
