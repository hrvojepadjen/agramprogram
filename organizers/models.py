from django.db import models
from django.utils.translation import gettext_lazy as _


class OrganizerType(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Type Name"),
        help_text=_("The name of the organizer type.")
    )

    class Meta:
        verbose_name = _("Organizer Type")
        verbose_name_plural = _("Organizer Types")

    def __str__(self):
        return self.name


class CityDistrict(models.Model):
    """
    Represents a district within a city, which can be associated with events.
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("District Name"),
        help_text=_("The name of the city district.")
    )

    class Meta:
        verbose_name = _("City District")
        verbose_name_plural = _("City Districts")

    def __str__(self):
        return f"{self.name}"


class Organizer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the organizer.")
    )
    organizer_type = models.ForeignKey(
        OrganizerType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Organizer Type"),
        help_text=_("The type of the organizer.")
    )
    events = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Events"),
        help_text=_("Events organized by this organizer.")
    )
    location = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Location"),
        help_text=_("The address of the organizer.")
    )
    contact_email = models.EmailField(
        null=True,
        blank=True,
        verbose_name=_("Contact Email"),
        help_text=_("The contact email for the organizer.")
    )
    has_parking = models.BooleanField(
        default=False,
        verbose_name=_("Has Parking"),
        help_text=_("Indicates whether the organizer provides parking.")
    )
    pet_friendly = models.BooleanField(
        default=False,
        verbose_name=_("Pet Friendly"),
        help_text=_("Indicates whether pets are allowed.")
    )
    wheelchair_accessible_entry = models.BooleanField(
        default=False,
        verbose_name=_("Wheelchair Accessible Entry"),
        help_text=_("Indicates whether the entry is accessible for wheelchairs.")
    )
    wheelchair_accessible_wc = models.BooleanField(
        default=False,
        verbose_name=_("Wheelchair Accessible Restroom"),
        help_text=_("Indicates whether restrooms are accessible for wheelchairs.")
    )
    logo_url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_("Logo URL"),
        help_text=_("The URL of the organizer's logo.")
    )
    user = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Associated User"),
        help_text=_("The user associated with this organizer.")
    )
    city_district = models.ForeignKey(
        CityDistrict,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("City District"),
        help_text=_("The district where the event is taking place.")
    )

    class Meta:
        verbose_name = _("Organizer")
        verbose_name_plural = _("Organizers")

    def __str__(self):
        return self.name
