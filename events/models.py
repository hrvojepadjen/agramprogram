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


class Category(models.Model):
    """
    Represents a category to classify events (e.g., Music, Art, Sports).
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Category Name"),
        help_text=_("The name of the category.")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class AgeGroup(models.Model):
    """
    Represents an age group category for events (e.g., Children, Adults, All Ages).
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Age Group Name"),
        help_text=_("The name of the age group.")
    )

    class Meta:
        verbose_name = _("Age Group")
        verbose_name_plural = _("Age Groups")

    def __str__(self):
        return self.name
