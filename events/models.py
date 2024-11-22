from django.db import models
from django.utils.translation import gettext_lazy as _


class EventType(models.Model):
    """
    Represents the type of an event (e.g., Workshop, Play, Concert).
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Event Type Name"),
        help_text=_("The name of the event type.")
    )

    class Meta:
        verbose_name = _("Event Type")
        verbose_name_plural = _("Event Types")

    def __str__(self):
        return self.name
