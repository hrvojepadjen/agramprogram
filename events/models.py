# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# 3rd party imports
from taggit.managers import TaggableManager

# local imports
from organizers.models import Organizer, CityDistrict


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


class Event(models.Model):
    """
    Represents an event, including details like type, category, location, and target age groups.
    """
    name = models.TextField(
        verbose_name=_("Event Name"),
        help_text=_("The name of the event.")
    )
    city_district = models.ForeignKey(
        CityDistrict,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("City District"),
        help_text=_("The district where the event is taking place.")
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("A detailed description of the event.")
    )
    description_en = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Description (English)"),
        help_text=_("A detailed description of the event in English.")
    )
    event_type = models.ForeignKey(
        EventType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Event Type"),
        help_text=_("The type of the event (e.g., Workshop, Play, Concert).")
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name=_("Categories"),
        help_text=_("The categories this event belongs to (e.g., Music, Art).")
    )
    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name=_("Organizer"),
        help_text=_("The organizer responsible for this event.")
    )
    location = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Location"),
        help_text=_("The location where the event will be held.")
    )
    start_datetime = models.DateTimeField(
        verbose_name=_("Start Date & Time"),
        help_text=_("The starting date and time of the event.")
    )
    end_datetime = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("End Date & Time"),
        help_text=_("The ending date and time of the event.")
    )
    target_age_groups = models.ManyToManyField(
        AgeGroup,
        verbose_name=_("Target Age Groups"),
        help_text=_("The age groups targeted by this event (e.g., Children, Adults).")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Price"),
        help_text=_("The price of admission (optional).")
    )
    tickets_available = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Tickets Available"),
        help_text=_("The number of tickets available for the event.")
    )
    registration_required = models.BooleanField(
        default=False,
        verbose_name=_("Registration Required"),
        help_text=_("Indicates whether registration is required.")
    )
    registration_deadline = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Registration Deadline"),
        help_text=_("The deadline for registering for the event (optional).")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("The timestamp when the event was created.")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At"),
        help_text=_("The timestamp when the event was last updated.")
    )
    featured = models.BooleanField(
        default=False,
        verbose_name=_("Featured Event"),
        help_text=_("Indicates whether this event is featured.")
    )

    tags = TaggableManager(
        blank=True,
        verbose_name=_('Tags'),
        help_text=_('A comma-separated list of tags'),
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name
